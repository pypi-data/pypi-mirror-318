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


class ProxmoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "proxmox"

    @property
    def original_file_name(self) -> "str":
        return "proxmox.svg"

    @property
    def title(self) -> "str":
        return "Proxmox"

    @property
    def primary_color(self) -> "str":
        return "#E57000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proxmox</title>
     <path d="M4.928 1.825c-1.09.553-1.09.64-.07 1.78 5.655 6.295
 7.004 7.782 7.107 7.782.139.017 7.971-8.542
 8.058-8.801.034-.07-.208-.312-.519-.536-.415-.312-.864-.433-1.712-.467-1.59-.104-2.144.242-4.115
 2.455-.899 1.003-1.66 1.833-1.66 1.833-.017
 0-.76-.813-1.642-1.798S8.473 2.1 8.127
 1.91c-.796-.45-2.421-.484-3.2-.086zM1.297 4.367C.45 4.695 0 5.007 0
 5.248c0 .121 1.331 1.678 2.94 3.459 1.625 1.78 2.939 3.268 2.939
 3.302 0 .035-1.331 1.522-2.94 3.303C1.314 17.11.017 18.683.035
 18.822c.086.467 1.504 1.055 2.541 1.055 1.678-.018 2.058-.312
 5.603-4.202 1.78-1.954 3.233-3.614 3.233-3.666
 0-.069-1.435-1.694-3.199-3.63-2.3-2.508-3.423-3.632-3.96-3.874-.812-.398-2.126-.467-2.956-.138zm18.467.12c-.502.26-1.764
 1.505-3.943 3.891-1.763 1.937-3.199 3.562-3.199 3.631 0 .07 1.453
 1.712 3.234 3.666 3.544 3.89 3.925 4.184 5.602 4.202 1.038 0
 2.455-.588
 2.542-1.055.017-.156-1.28-1.712-2.905-3.493-1.608-1.78-2.94-3.285-2.94-3.32
 0-.034 1.332-1.539 2.94-3.32C22.72 6.91 24.017 5.352 24
 5.214c-.087-.45-1.366-.968-2.473-1.038-.795-.034-1.21.035-1.763.312zM7.954
 16.973c-2.144 2.369-3.908 4.374-3.943
 4.46-.034.07.208.312.52.537.414.311.864.432 1.711.467 1.574.103
 2.161-.26 4.15-2.508.864-.968 1.608-1.78 1.625-1.78s.761.812 1.643
 1.798c2.023 2.248 2.559 2.576 4.132 2.49.848-.035 1.297-.156
 1.712-.467.311-.225.553-.467.519-.536-.087-.26-7.92-8.819-8.058-8.801-.069
 0-1.867 1.954-4.011 4.34z" />
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
