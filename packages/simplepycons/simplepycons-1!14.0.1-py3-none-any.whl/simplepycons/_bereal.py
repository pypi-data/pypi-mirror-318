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


class BerealIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bereal"

    @property
    def original_file_name(self) -> "str":
        return "bereal.svg"

    @property
    def title(self) -> "str":
        return "BeReal"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BeReal</title>
     <path d="M6.501 10.727c.593 0 1.029.196
 1.307.587.279.393.418.857.418 1.391v.312H5.674a.97.97 0 0 0
 .343.596c.182.148.422.223.718.223.172 0
 .327-.023.464-.066.163-.055.324-.119.48-.192l.297.733a1.73 1.73 0 0
 1-.644.296c-.252.063-.46.093-.62.093-.656
 0-1.172-.18-1.55-.537-.377-.36-.565-.84-.565-1.441
 0-.603.17-1.086.51-1.45.342-.364.806-.545 1.394-.545Zm8.835 0c.593 0
 1.028.196 1.307.587.278.393.417.857.417
 1.391v.312h-2.552c.038.235.16.447.344.596.182.148.421.223.718.223.171
 0 .326-.023.464-.066a4.53 4.53 0 0 0 .48-.192l.297.733a1.728 1.728 0
 0 1-.644.296 2.67 2.67 0 0 1-.62.093c-.656
 0-1.173-.18-1.55-.537-.377-.36-.566-.84-.566-1.441
 0-.603.17-1.086.512-1.45.34-.364.805-.545 1.393-.545Zm3.875.041c.974
 0 1.603.502 1.603
 1.26v2.579h-1.027v-.561h-.02c-.215.385-.616.62-1.111.62-.756
 0-1.265-.473-1.265-1.136v-.008c0-.683.53-1.083
 1.465-1.144l.931-.055v-.231c0-.335-.217-.541-.618-.541-.383
 0-.615.18-.664.421l-.007.03h-.939l.004-.04c.056-.696.653-1.194
 1.648-1.194Zm4.789 2.8v1.039h-1.04v-1.039H24ZM1.982 9.308c.515 0
 .934.114 1.257.34.322.225.484.607.484 1.14 0
 .198-.046.376-.137.534-.09.16-.21.296-.355.41.24.125.436.294.59.506.153.213.23.483.23.81
 0 .489-.171.871-.512
 1.146-.34.275-.795.413-1.362.413H0V9.308h1.982Zm8.702 0c.578 0
 1.072.133 1.483.398.411.265.617.675.617 1.231 0
 .327-.085.609-.254.846a1.714 1.714 0 0 1-.652.549l1.304
 2.275h-1.077l-1.124-2.025a3.626 3.626 0 0
 1-.367.015h-.585v2.01H9.022V9.308h1.662ZM22.448
 9.3v5.307h-1.076V9.3h1.076Zm-2.66
 3.661-.777.049c-.397.025-.605.192-.605.46v.007c0
 .277.229.442.584.442.46 0 .797-.294.797-.688l.001-.27ZM2.17
 12.285H1.007v1.489h1.092c.27 0 .488-.063.652-.188a.622.622 0 0 0
 .246-.53c0-.25-.076-.44-.226-.572-.151-.132-.352-.199-.601-.199Zm4.308-.694a.75.75
 0 0
 0-.523.19c-.14.128-.232.315-.273.558h1.584c-.052-.253-.146-.442-.281-.564a.73.73
 0 0 0-.507-.184Zm8.834 0a.75.75 0 0
 0-.523.19c-.14.128-.231.315-.273.558h1.585c-.053-.253-.146-.442-.281-.564a.73.73
 0 0 0-.508-.184Zm-4.659-1.441h-.624v1.62h.64c.301 0
 .551-.06.749-.182.198-.122.296-.324.296-.604
 0-.297-.093-.51-.28-.639-.188-.13-.448-.195-.781-.195Zm-8.819
 0h-.827v1.316h.749c.281 0 .5-.053.66-.16.158-.105.238-.273.238-.501
 0-.25-.073-.422-.219-.515-.146-.093-.346-.14-.601-.14Z" />
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
