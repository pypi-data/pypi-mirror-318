from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_template_reprompt import ItemTemplateReprompt
from ..models.item_template_type import ItemTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.item_card import ItemCard
    from ..models.item_identity import ItemIdentity
    from ..models.item_login import ItemLogin
    from ..models.item_secure_note import ItemSecureNote


T = TypeVar("T", bound="ItemTemplate")


@_attrs_define
class ItemTemplate:
    """
    Attributes:
        card (Union[Unset, ItemCard]):
        collection_ids (Union[Unset, list[UUID]]):
        favorite (Union[Unset, bool]):
        fields (Union[Unset, list['Field']]):
        folder_id (Union[Unset, UUID]):
        identity (Union[Unset, ItemIdentity]):
        login (Union[Unset, ItemLogin]):
        name (Union[Unset, str]):
        notes (Union[Unset, str]):
        organization_id (Union[Unset, UUID]):
        reprompt (Union[Unset, ItemTemplateReprompt]):
        secure_note (Union[Unset, ItemSecureNote]):
        type_ (Union[Unset, ItemTemplateType]):
    """

    card: Union[Unset, "ItemCard"] = UNSET
    collection_ids: Union[Unset, list[UUID]] = UNSET
    favorite: Union[Unset, bool] = UNSET
    fields: Union[Unset, list["Field"]] = UNSET
    folder_id: Union[Unset, UUID] = UNSET
    identity: Union[Unset, "ItemIdentity"] = UNSET
    login: Union[Unset, "ItemLogin"] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    organization_id: Union[Unset, UUID] = UNSET
    reprompt: Union[Unset, ItemTemplateReprompt] = UNSET
    secure_note: Union[Unset, "ItemSecureNote"] = UNSET
    type_: Union[Unset, ItemTemplateType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        collection_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = []
            for collection_ids_item_data in self.collection_ids:
                collection_ids_item = str(collection_ids_item_data)
                collection_ids.append(collection_ids_item)

        favorite = self.favorite

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        folder_id: Union[Unset, str] = UNSET
        if not isinstance(self.folder_id, Unset):
            folder_id = str(self.folder_id)

        identity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        login: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.login, Unset):
            login = self.login.to_dict()

        name = self.name

        notes = self.notes

        organization_id: Union[Unset, str] = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        reprompt: Union[Unset, int] = UNSET
        if not isinstance(self.reprompt, Unset):
            reprompt = self.reprompt.value

        secure_note: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secure_note, Unset):
            secure_note = self.secure_note.to_dict()

        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card is not UNSET:
            field_dict["card"] = card
        if collection_ids is not UNSET:
            field_dict["collectionIds"] = collection_ids
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if fields is not UNSET:
            field_dict["fields"] = fields
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if identity is not UNSET:
            field_dict["identity"] = identity
        if login is not UNSET:
            field_dict["login"] = login
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if reprompt is not UNSET:
            field_dict["reprompt"] = reprompt
        if secure_note is not UNSET:
            field_dict["secureNote"] = secure_note
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.field import Field
        from ..models.item_card import ItemCard
        from ..models.item_identity import ItemIdentity
        from ..models.item_login import ItemLogin
        from ..models.item_secure_note import ItemSecureNote

        d = src_dict.copy()
        _card = d.pop("card", UNSET)
        card: Union[Unset, ItemCard]
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = ItemCard.from_dict(_card)

        collection_ids = []
        _collection_ids = d.pop("collectionIds", UNSET)
        for collection_ids_item_data in _collection_ids or []:
            collection_ids_item = UUID(collection_ids_item_data)

            collection_ids.append(collection_ids_item)

        favorite = d.pop("favorite", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = Field.from_dict(fields_item_data)

            fields.append(fields_item)

        _folder_id = d.pop("folderId", UNSET)
        folder_id: Union[Unset, UUID]
        if isinstance(_folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = UUID(_folder_id)

        _identity = d.pop("identity", UNSET)
        identity: Union[Unset, ItemIdentity]
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = ItemIdentity.from_dict(_identity)

        _login = d.pop("login", UNSET)
        login: Union[Unset, ItemLogin]
        if isinstance(_login, Unset):
            login = UNSET
        else:
            login = ItemLogin.from_dict(_login)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        _organization_id = d.pop("organizationId", UNSET)
        organization_id: Union[Unset, UUID]
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        _reprompt = d.pop("reprompt", UNSET)
        reprompt: Union[Unset, ItemTemplateReprompt]
        if isinstance(_reprompt, Unset):
            reprompt = UNSET
        else:
            reprompt = ItemTemplateReprompt(_reprompt)

        _secure_note = d.pop("secureNote", UNSET)
        secure_note: Union[Unset, ItemSecureNote]
        if isinstance(_secure_note, Unset):
            secure_note = UNSET
        else:
            secure_note = ItemSecureNote.from_dict(_secure_note)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ItemTemplateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ItemTemplateType(_type_)

        item_template = cls(
            card=card,
            collection_ids=collection_ids,
            favorite=favorite,
            fields=fields,
            folder_id=folder_id,
            identity=identity,
            login=login,
            name=name,
            notes=notes,
            organization_id=organization_id,
            reprompt=reprompt,
            secure_note=secure_note,
            type_=type_,
        )

        item_template.additional_properties = d
        return item_template

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
