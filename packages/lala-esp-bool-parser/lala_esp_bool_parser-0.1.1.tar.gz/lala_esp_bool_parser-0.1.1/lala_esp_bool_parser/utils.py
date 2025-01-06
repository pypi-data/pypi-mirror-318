# SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

import typing as t

from packaging.version import (
    Version,
)


class InvalidInput(SystemExit):
    """Invalid input from user"""


class InvalidIfClause(SystemExit):
    """Invalid if clause in manifest file"""


def to_version(s: t.Any) -> Version:
    if isinstance(s, Version):
        return s

    try:
        return Version(str(s))
    except ValueError:
        raise InvalidInput(f'Invalid version: {s}')
