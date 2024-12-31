#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class TaskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "task"

    @property
    def original_file_name(self) -> "str":
        return "task.svg"

    @property
    def title(self) -> "str":
        return "Task"

    @property
    def primary_color(self) -> "str":
        return "#29BEB0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Task</title>
     <path d="M1.857 18.013 11.736 24V12.456L1.857 6.468Zm20.286
 0V6.468l-9.879 5.988V24Zm-.246-12.014L12 0 2.103 5.999 12 11.998Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/go-task/task/blob/84ad0056'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
