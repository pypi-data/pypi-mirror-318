#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
# Copyright (c) 2023-2025 Yunqi Inc. All rights reserved.
#

import re
from enum import Enum
from typing import List, Tuple

from clickzetta.zettapark.exceptions import ZettaparkInvalidVolumePathException

_NAME_PATTERN = "([a-z0-9_]+|`[a-z0-9_]+`)"
_PATH_PATTERN = (
    "^(vol(?:ume)?(:table|:user)?)"  # volume kind
    rf"://{_NAME_PATTERN}(?:\.{_NAME_PATTERN}(?:\.{_NAME_PATTERN})?)?"  # volume name
    "(/.*)"  # path
)
_PATH_REGEX = re.compile(_PATH_PATTERN, re.IGNORECASE)


class VolumeKind(Enum):
    EXTERNAL = "external"
    TABLE = "table"
    USER = "user"


class VolumePath:
    def __init__(self, volume_path: str) -> None:
        self._volume_path: str = volume_path
        self._kind, self._volume, self._path = _parse(volume_path)

    @property
    def kind(self) -> VolumeKind:
        return self._kind

    @property
    def volume_name(self) -> List[str]:
        return [x for x in self._volume]

    @property
    def path(self) -> str:
        return self._path


def _parse(path: str) -> Tuple[VolumeKind, List[str], str]:
    match = _PATH_REGEX.match(path)
    if not match:
        raise ZettaparkInvalidVolumePathException(
            f"Invalid volume path: '{path}'",
        )

    if match.group(2) and match.group(2).lower() == ":table":
        kind = VolumeKind.TABLE
    elif match.group(2) and match.group(2).lower() == ":user":
        kind = VolumeKind.USER
    else:
        kind = VolumeKind.EXTERNAL

    name = [match.group(3).strip("`")]
    if match.group(4):
        name.append(match.group(4).strip("`"))
    if match.group(5):
        name.append(match.group(5).strip("`"))

    path_ = match.group(6).replace("//", "/")

    return kind, name, path_
