from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiUpload")


@_attrs_define
class ApiUpload:
    """File uploaded with `POST /api/v3/uploads`, to reference by its `upload_id` in the calls that take a document, such
    as the PEC transfer documents

    """

    upload_id: int
    mimetype: None | str
    """ MIME type associated with the extension of the file, for example `application/pdf` """
    filename: str
    """ Name given to the file by the service when storing it """
    original_filename: None | str
    """ Name of the file as uploaded by the client """
    file_extension: None | str
    """ Extension of the file name, in lowercase, for example `pdf` """
    upload_date: datetime.datetime
    """ Date and time of the upload """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        mimetype: None | str
        mimetype = self.mimetype

        filename = self.filename

        original_filename: None | str
        original_filename = self.original_filename

        file_extension: None | str
        file_extension = self.file_extension

        upload_date = self.upload_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "mimetype": mimetype,
                "filename": filename,
                "original_filename": original_filename,
                "file_extension": file_extension,
                "upload_date": upload_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        def _parse_mimetype(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mimetype = _parse_mimetype(d.pop("mimetype"))

        filename = d.pop("filename")

        def _parse_original_filename(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_filename = _parse_original_filename(d.pop("original_filename"))

        def _parse_file_extension(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_extension = _parse_file_extension(d.pop("file_extension"))

        upload_date = datetime.datetime.fromisoformat(d.pop("upload_date"))

        api_upload = cls(
            upload_id=upload_id,
            mimetype=mimetype,
            filename=filename,
            original_filename=original_filename,
            file_extension=file_extension,
            upload_date=upload_date,
        )

        api_upload.additional_properties = d
        return api_upload

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
