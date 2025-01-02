from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMoveItemidOrganizationIdBody")


@_attrs_define
class PostMoveItemidOrganizationIdBody:
    """
    Attributes:
        array (Union[Unset, list[UUID]]):
    """

    array: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array: Union[Unset, list[str]] = UNSET
        if not isinstance(self.array, Unset):
            array = []
            for array_item_data in self.array:
                array_item = str(array_item_data)
                array.append(array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array is not UNSET:
            field_dict["array"] = array

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        array = []
        _array = d.pop("array", UNSET)
        for array_item_data in _array or []:
            array_item = UUID(array_item_data)

            array.append(array_item)

        post_move_itemid_organization_id_body = cls(
            array=array,
        )

        post_move_itemid_organization_id_body.additional_properties = d
        return post_move_itemid_organization_id_body

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
