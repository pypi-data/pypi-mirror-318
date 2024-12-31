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


class KaliLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kalilinux"

    @property
    def original_file_name(self) -> "str":
        return "kalilinux.svg"

    @property
    def title(self) -> "str":
        return "Kali Linux"

    @property
    def primary_color(self) -> "str":
        return "#557C94"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kali Linux</title>
     <path d="M12.778 5.943s-1.97-.13-5.327.92c-3.42 1.07-5.36
 2.587-5.36 2.587s5.098-2.847 10.852-3.008zm7.351
 3.095l.257-.017s-1.468-1.78-4.278-2.648c1.58.642 2.954 1.493 4.021
 2.665zm.42.74c.039-.068.166.217.263.337.004.024.01.039-.045.027-.005-.025-.013-.032-.013-.032s-.135-.08-.177-.137c-.041-.057-.049-.157-.028-.195zm3.448
 8.479s.312-3.578-5.31-4.403a18.277 18.277 0 0
 0-2.524-.187c-4.506.06-4.67-5.197-1.275-5.462 1.407-.116 3.087.643
 4.73
 1.408-.007.204.002.385.136.552.134.168.648.35.813.445.164.094.691.43
 1.014.85.07-.131.654-.512.654-.512s-.14.003-.465-.119c-.326-.122-.713-.49-.722-.511-.01-.022-.015-.055.06-.07.059-.049-.072-.207-.13-.265-.058-.058-.445-.716-.454-.73-.009-.016-.012-.031-.04-.05-.085-.027-.46.04-.46.04s-.575-.283-.774-.893c.003.107-.099.224
 0 .469-.3-.127-.558-.344-.762-.88-.12.305 0 .499 0
 .499s-.707-.198-.82-.85c-.124.293 0 .469 0
 .469s-1.153-.602-3.069-.61c-1.283-.118-1.55-2.374-1.43-2.754 0
 0-1.85-.975-5.493-1.406-3.642-.43-6.628-.065-6.628-.065s6.45-.31
 11.617 1.783c.176.785.704 2.094.989 2.723-.815.563-1.733 1.092-1.876
 2.97-.143 1.878 1.472 3.53 3.474 3.58 1.9.102 3.214.116 4.806.942
 1.52.84 2.766 3.4 2.89 5.703.132-1.709-.509-5.383-3.5-6.498 4.181.732
 4.549 3.832 4.549 3.832zM12.68
 5.663l-.15-.485s-2.484-.441-5.822-.204C3.37 5.211 0 6.38 0
 6.38s6.896-1.735 12.68-.717Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
