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


class OrgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "org"

    @property
    def original_file_name(self) -> "str":
        return "org.svg"

    @property
    def title(self) -> "str":
        return "Org"

    @property
    def primary_color(self) -> "str":
        return "#77AA99"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Org</title>
     <path d="M17.169 0c-.566.004-2.16 3.312-3.376 5.94a2.19 2.19 0
 01-.408-1.267c-.03-.582-1.089.237-.936
 1.275-.068-.035-1.26.227-1.26.23-.23-.93-.802-1.618-1.15-.563-.701
 1.663-.88 2.984.115 4.585-.908 4.058-6.948 6.053-6.32 9.33.175.004
 1.634 3.48 6.337 2.057 5.557-1.577 8.624 2.116 8.978
 2.375.52.526-1.348-4.573-5.302-6.865-2.339-1.276-.87-3.474-.703-4.25
 0 0 1.874 1.312 3.232-.692 1.227.316 2.05-.224 3.105.158.64.28
 3.336.11
 2.334-1.396-.148.129.07.27-.075.46-.043.056-.128.232-.408.315-.314.149-.83.27-1.43-.37-.434-.32-.748-.04-.992-.063.152-.098.577-.315
 1.264-.315.388 0 .594.336.854.338.174 0
 .685-.262.787-.365.63-.41.697-.278
 1.012-.905.17-.759-.215-.92-.332-1.129-.032-.483-.436-.67-.919-.326-1.106-.198-2.192-.105-2.728-.15-1.175-.164-2.153-.786-2.153-.786.143-.19.075-.6-.842-.628-.315-.104-.45-.2-.745-.307.61-1.37.674-2.007
 1.418-4.004.261-1.053 1.039-2.685.643-2.682zm-4.297
 8.093c.03-.086.443.138.952.176.395.03.805.048
 1.296-.025.03-.005.172.095-.15.194-.02.01-.062-.01-.065.196 0
 .022-.01.04-.02.046-.15.152-.708.223-1.065.1-.436-.17-.482-.316-.517-.443-.305-.147-.47-.123-.43-.244zM9.685
 10.2C8.86 9 8.929 8.36 8.96 7.256 7.961 8.288 6.855 8.3 5.18
 8.58c-1.299.234-3.657 2.447-4.025 4.742-.043.608-.08 2.183.424
 3.498.492 1.13.828 1.727 1.844 2.335-.882-3.169 5.296-5.33
 6.263-8.955z" />
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
