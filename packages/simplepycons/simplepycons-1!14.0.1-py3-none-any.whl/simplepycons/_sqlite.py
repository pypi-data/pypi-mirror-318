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


class SqliteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sqlite"

    @property
    def original_file_name(self) -> "str":
        return "sqlite.svg"

    @property
    def title(self) -> "str":
        return "SQLite"

    @property
    def primary_color(self) -> "str":
        return "#003B57"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SQLite</title>
     <path d="M21.678.521c-1.032-.92-2.28-.55-3.513.544a8.71 8.71 0 0
 0-.547.535c-2.109 2.237-4.066 6.38-4.674 9.544.237.48.422 1.093.544
 1.561a13.044 13.044 0 0 1
 .164.703s-.019-.071-.096-.296l-.05-.146a1.689 1.689 0 0
 0-.033-.08c-.138-.32-.518-.995-.686-1.289-.143.423-.27.818-.376
 1.176.484.884.778 2.4.778
 2.4s-.025-.099-.147-.442c-.107-.303-.644-1.244-.772-1.464-.217.804-.304
 1.346-.226 1.478.152.256.296.698.422 1.186.286 1.1.485 2.44.485
 2.44l.017.224a22.41 22.41 0 0 0 .056 2.748c.095 1.146.273 2.13.5
 2.657l.155-.084c-.334-1.038-.47-2.399-.41-3.967.09-2.398.642-5.29
 1.661-8.304 1.723-4.55 4.113-8.201 6.3-9.945-1.993 1.8-4.692 7.63-5.5
 9.788-.904 2.416-1.545 4.684-1.931 6.857.666-2.037 2.821-2.912
 2.821-2.912s1.057-1.304
 2.292-3.166c-.74.169-1.955.458-2.362.629-.6.251-.762.337-.762.337s1.945-1.184
 3.613-1.72C21.695 7.9 24.195 2.767 21.678.521m-18.573.543A1.842 1.842
 0 0 0 1.27 2.9v16.608a1.84 1.84 0 0 0 1.835 1.834h9.418a22.953 22.953
 0 0 1-.052-2.707c-.006-.062-.011-.141-.016-.2a27.01 27.01 0 0
 0-.473-2.378c-.121-.47-.275-.898-.369-1.057-.116-.197-.098-.31-.097-.432
 0-.12.015-.245.037-.386a9.98 9.98 0 0 1
 .234-1.045l.217-.028c-.017-.035-.014-.065-.031-.097l-.041-.381a32.8
 32.8 0 0 1
 .382-1.194l.2-.019c-.008-.016-.01-.038-.018-.053l-.043-.316c.63-3.28
 2.587-7.443 4.8-9.791.066-.069.133-.128.198-.194Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sqlite/sqlite/blob/43e8627'''

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
