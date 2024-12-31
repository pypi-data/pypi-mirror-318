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


class RIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "r"

    @property
    def original_file_name(self) -> "str":
        return "r.svg"

    @property
    def title(self) -> "str":
        return "R"

    @property
    def primary_color(self) -> "str":
        return "#276DC3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>R</title>
     <path d="M12 2.746c-6.627 0-12 3.599-12 8.037 0 3.897 4.144 7.144
 9.64 7.88V16.26c-2.924-.915-4.925-2.755-4.925-4.877 0-3.035
 4.084-5.494 9.12-5.494 5.038 0 8.757 1.683 8.757 5.494 0 1.976-.999
 3.379-2.662 4.272.09.066.174.128.258.216.169.149.25.363.372.544
 2.128-1.45 3.44-3.437 3.44-5.631 0-4.44-5.373-8.038-12-8.038zm-2.111
 4.99v13.516l4.093-.002-.002-5.291h1.1c.225 0
 .321.066.549.25.272.22.715.982.715.982l2.164 4.063
 4.627-.002-2.864-4.826s-.086-.193-.265-.383a2.22 2.22 0
 00-.582-.416c-.422-.214-1.149-.434-1.149-.434s3.578-.264
 3.578-3.826c0-3.562-3.744-3.63-3.744-3.63zm4.127
 2.93l2.478.002s1.149-.062 1.149 1.127c0 1.165-1.149 1.17-1.149
 1.17h-2.478zm1.754 6.119c-.494.049-1.012.079-1.54.088v1.807a16.622
 16.622 0
 002.37-.473l-.471-.891s-.108-.183-.248-.394c-.039-.054-.08-.098-.111-.137z"
 />
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
