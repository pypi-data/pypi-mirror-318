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


class MetaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "meta"

    @property
    def original_file_name(self) -> "str":
        return "meta.svg"

    @property
    def title(self) -> "str":
        return "Meta"

    @property
    def primary_color(self) -> "str":
        return "#0467DF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Meta</title>
     <path d="M6.915 4.03c-1.968 0-3.683 1.28-4.871 3.113C.704 9.208 0
 11.883 0 14.449c0 .706.07 1.369.21 1.973a6.624 6.624 0 0 0 .265.86
 5.297 5.297 0 0 0 .371.761c.696 1.159 1.818 1.927 3.593 1.927 1.497 0
 2.633-.671 3.965-2.444.76-1.012 1.144-1.626
 2.663-4.32l.756-1.339.186-.325c.061.1.121.196.183.3l2.152 3.595c.724
 1.21 1.665 2.556 2.47 3.314 1.046.987 1.992 1.22 3.06 1.22 1.075 0
 1.876-.355 2.455-.843a3.743 3.743 0 0 0
 .81-.973c.542-.939.861-2.127.861-3.745
 0-2.72-.681-5.357-2.084-7.45-1.282-1.912-2.957-2.93-4.716-2.93-1.047
 0-2.088.467-3.053 1.308-.652.57-1.257 1.29-1.82
 2.05-.69-.875-1.335-1.547-1.958-2.056-1.182-.966-2.315-1.303-3.454-1.303zm10.16
 2.053c1.147 0 2.188.758 2.992 1.999 1.132 1.748 1.647 4.195 1.647 6.4
 0 1.548-.368 2.9-1.839 2.9-.58
 0-1.027-.23-1.664-1.004-.496-.601-1.343-1.878-2.832-4.358l-.617-1.028a44.908
 44.908 0 0 0-1.255-1.98c.07-.109.141-.224.211-.327 1.12-1.667
 2.118-2.602 3.358-2.602zm-10.201.553c1.265 0 2.058.791 2.675
 1.446.307.327.737.871 1.234 1.579l-1.02 1.566c-.757 1.163-1.882
 3.017-2.837 4.338-1.191 1.649-1.81 1.817-2.486 1.817-.524
 0-1.038-.237-1.383-.794-.263-.426-.464-1.13-.464-2.046
 0-2.221.63-4.535 1.66-6.088.454-.687.964-1.226 1.533-1.533a2.264
 2.264 0 0 1 1.088-.285z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.facebook.com/brand/resources/meta'''
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
