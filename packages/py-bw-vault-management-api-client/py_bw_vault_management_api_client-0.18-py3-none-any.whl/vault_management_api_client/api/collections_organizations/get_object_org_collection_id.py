from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    organization_id: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/object/org-collection/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 500:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: UUID,
) -> Response[Any]:
    """Retrieve a Collection from a specified Organization.

     Retrieve an existing collection from a specified Organization by specifying the unique Collection
    identifier (e.g. `3a84be8d-12e7-4223-98cd-ae0000eabdec`) in the path and an Organization identifier
    as a query parameter .

    Args:
        id (UUID):
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: UUID,
) -> Response[Any]:
    """Retrieve a Collection from a specified Organization.

     Retrieve an existing collection from a specified Organization by specifying the unique Collection
    identifier (e.g. `3a84be8d-12e7-4223-98cd-ae0000eabdec`) in the path and an Organization identifier
    as a query parameter .

    Args:
        id (UUID):
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
