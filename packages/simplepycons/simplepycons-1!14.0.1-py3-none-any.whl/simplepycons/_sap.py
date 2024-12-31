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


class SapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sap"

    @property
    def original_file_name(self) -> "str":
        return "sap.svg"

    @property
    def title(self) -> "str":
        return "SAP"

    @property
    def primary_color(self) -> "str":
        return "#0FAAFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SAP</title>
     <path d="M0 6.064v11.872h12.13L24 6.064zm3.264
 2.208h.005c.863.001 1.915.245 2.676.633l-.82
 1.43c-.835-.404-1.255-.442-1.73-.467-.708-.038-1.064.215-1.069.488-.007.332.669.633
 1.305.838.964.306 2.19.715 2.377 1.9L7.77 8.437h2.046l2.064
 5.576-.007-5.575h2.37c2.257 0 3.318.764 3.318 2.519 0 1.575-1.09
 2.514-2.936 2.514h-.763l-.01
 2.094-3.588-.003-.25-.908c-.37.122-.787.189-1.23.189-.456
 0-.885-.071-1.263-.2l-.358.919-2
 .006.09-.462c-.029.025-.057.05-.087.074-.535.43-1.208.629-2.037.644l-.213.002a5.075
 5.075 0 0 1-2.581-.675l.73-1.448c.79.467 1.286.572
 1.956.558.347-.007.598-.07.761-.239a.557.557 0 0 0
 .156-.369c.007-.376-.53-.553-1.185-.756-.531-.164-1.135-.389-1.606-.735-.559-.41-.825-.924-.812-1.65a1.99
 1.99 0 0 1 .566-1.377c.519-.537 1.357-.863 2.363-.863zm10.597
 1.67v1.904h.521c.694 0 1.247-.23 1.248-.964
 0-.709-.554-.94-1.248-.94zm-5.087.767l-.748
 2.362c.223.085.481.133.757.133.268 0 .52-.047.742-.126l-.736-2.37z"
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
