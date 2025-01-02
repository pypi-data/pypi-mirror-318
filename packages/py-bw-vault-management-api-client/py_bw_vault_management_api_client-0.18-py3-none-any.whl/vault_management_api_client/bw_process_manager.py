import json
import logging
import os
import shlex
import shutil
import subprocess
import time
import urllib


class BwProcess:
    def __init__(self, bw_cli_path, extra_env_vars=None):
        full_path = shutil.which(bw_cli_path)
        if not full_path:
            raise ValueError(f"{bw_cli_path} does not exists or is not executable")
        self.__bw = full_path
        self.__bw_process = None
        self.__bw_env_vars = {}
        if extra_env_vars:
            self.__bw_env_vars.update(extra_env_vars)

    def __construct_env(self, extra_env_vars=None):
        env = {}
        env.update(os.environ)
        env.update(self.__bw_env_vars)
        env.update(extra_env_vars or {})
        return env

    def run(self, *args, parse_output=False, timeout=30, extra_env_vars=None):
        logging_args = list(args)
        try:
            i = logging_args.index("login")
            for j in range(i + 1, len(logging_args)):
                logging_args[j] = "..."
        except ValueError:
            pass
        logging.info("Running %s", shlex.join(logging_args))
        args = [self.__bw, "--nointeraction", *list(args)]
        try:
            output = subprocess.check_output(args, timeout=timeout, env=self.__construct_env(extra_env_vars))
        except Exception as e:
            if isinstance(e, subprocess.CalledProcessError):
                logging.error("Failed to run %s. Exited with code %d", logging_args, e.returncode)
            else:
                logging.error("Failed to run %s. %s", logging_args, e)
            raise e
        if parse_output:
            return json.loads(output)

    def start_serve(
            self, password: str, host: str, port: int, *,
            username : str | None = None, clientid : str | None = None, clientsecret : str | None = None):
        if username:
            if clientid or clientsecret:
                raise ValueError("If username is set, clientid and/or clientsecret should not be set!")
        else:
            if (not clientid) or (not clientsecret):
                raise ValueError("If username is not set, both clientid and clientsecret must be set!")

        status_output = self.run("status", parse_output=True)
        assert status_output["status"] == "unauthenticated", f"Unexpected status: {status_output}"

        if username:
            self.run("login", username, "--passwordenv", "BW_PASSWORD", extra_env_vars={"BW_PASSWORD": password})
        else:
            self.run("login", "--apikey", extra_env_vars={"BW_CLIENTID": clientid, "BW_CLIENTSECRET": clientsecret})
            self.run("unlock", "--passwordenv", "BW_PASSWORD", extra_env_vars={"BW_PASSWORD": password})

        self.__bw_process = subprocess.Popen(
            [self.__bw, "serve", "--nointeraction", "--hostname", host, "--port", str(port)],
            bufsize=0,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            env=self.__construct_env(),
        )
        logging.info("Started bw serve with pid %d", self.__bw_process.pid)

        for _ in range(300):
            time.sleep(0.1)
            logging.info("Checking if bw serve is up")
            if self.__bw_process.poll() is not None:
                self.terminate_serve()
                outs, errs = self.__bw_process.communicate(timeout=15)
                souts, serrs = str(outs), str(errs)
                raise AssertionError(
                    f"bw serve (PID: {self.__bw_process.pid}) unexpectedly reports as terminated"
                    f"exit code: {self.__bw_process.returncode}, stdout: {souts}, stderr: {serrs}"
                )
            try:
                urllib.request.urlopen(f"http://{host}:{port}/", timeout=1)
            except urllib.error.HTTPError:
                # url responds with a 404
                logging.info("bw serve up")
                break
            except urllib.error.URLError:
                pass
        else:
            self.terminate_serve()
            outs, errs = self.__bw_process.communicate(timeout=15)
            souts, serrs = str(outs), str(errs)
            raise AssertionError(
                f"bw serve failed to start (PID: {self.__bw_process.pid}). "
                f"exit code: {self.__bw_process.returncode}, stdout: {souts}, stderr: {serrs}"
            )

    def terminate_serve(self):
        logging.info("Terminating bw serve")
        self.__bw_process.terminate()
        try:
            self.__bw_process.communicate(timeout=10)
            logging.info("bw serve (PID: %d) terminated", self.__bw_process.pid)
        except subprocess.TimeoutExpired:
            logging.warn("bw serve didn't terminate, killing it")
            self.__bw_process.kill()
        self.__bw_process = None
        self.run("logout")
