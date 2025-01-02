from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """
    Attributes:
        external_id (Union[Unset, str]):
        groups (Union[Unset, list['Group']]):
        name (Union[Unset, str]):
        organization_id (Union[Unset, UUID]):
    """

    external_id: Union[Unset, str] = UNSET
    groups: Union[Unset, list["Group"]] = UNSET
    name: Union[Unset, str] = UNSET
    organization_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        name = self.name

        organization_id: Union[Unset, str] = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if groups is not UNSET:
            field_dict["groups"] = groups
        if name is not UNSET:
            field_dict["name"] = name
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.group import Group

        d = src_dict.copy()
        external_id = d.pop("externalId", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Group.from_dict(groups_item_data)

            groups.append(groups_item)

        name = d.pop("name", UNSET)

        _organization_id = d.pop("organizationId", UNSET)
        organization_id: Union[Unset, UUID]
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        collection = cls(
            external_id=external_id,
            groups=groups,
            name=name,
            organization_id=organization_id,
        )

        collection.additional_properties = d
        return collection

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
