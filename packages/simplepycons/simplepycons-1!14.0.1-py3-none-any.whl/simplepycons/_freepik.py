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


class FreepikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freepik"

    @property
    def original_file_name(self) -> "str":
        return "freepik.svg"

    @property
    def title(self) -> "str":
        return "Freepik"

    @property
    def primary_color(self) -> "str":
        return "#1273EB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Freepik</title>
     <path d="M4.315 6.939c-.702.702-1.204 1.505-1.706
 2.308l-.702-.402c-.1-.401-.602-.702-1.004-.702-.602.1-.903.502-.903
 1.104 0 .501.502.903 1.004.803.1 0 .2 0 .3-.1l.703.4c-.401.904-.702
 1.807-.803 2.81l1.204.201c.402-2.107 1.305-4.014 2.81-5.52Zm12.544
 7.626c-1.204 0-2.107-1.003-2.107-2.107 0-1.204 1.004-2.107
 2.107-2.107 1.205 0 2.108 1.003 2.108 2.107 0 1.204-.903 2.107-2.108
 2.107zm-7.325 1.506a2.912 2.912 0 0 1-2.91-2.91c0-1.707 1.304-3.011
 2.91-3.011a2.912 2.912 0 0 1 2.91 2.91c0 1.606-1.305 3.01-2.91
 3.01zm3.311-10.337a9.422 9.422 0 0 0-9.433 9.434c0 .702.1 1.304.2
 2.007 1.004.802 4.216 1.405 8.33 1.204 4.516-.301 8.23-1.505
 10.437-3.412 0-.301
 0-.602-.1-.903-.603-4.817-4.617-8.33-9.434-8.33Zm-.803 13.749c-.602
 0-1.204.1-1.806.1-1.405
 0-2.71-.1-3.914-.3-.602-.101-1.304-.302-2.007-.503 1.606 2.91 4.817
 4.918 8.43 4.918 4.415 0 8.229-3.011 9.232-7.125a16.828 16.828 0 0
 1-3.813 1.806c-1.806.602-3.914 1.003-6.122 1.104zM23.182
 7.34c.501-.1.903-.502.803-1.104-.1-.502-.502-.903-1.004-.803-.502.1-.803.502-.803
 1.004l-.702.602c-.703-.703-1.405-1.305-2.208-1.806l-.602 1.003a11.225
 11.225 0 0 1 4.014
 4.616l1.104-.501c-.402-.904-.903-1.706-1.505-2.51l.602-.601c.1.1.2.1.3.1zM12.845
 3.326h-.803l-.1-1.004c.301-.2.502-.602.401-1.003-.1-.602-.602-1.104-1.204-1.004-.602.1-1.003.602-1.003
 1.305.1.401.3.702.602.903l.1 1.004c-1.104.2-2.208.501-3.211
 1.003l.502 1.104a10.425 10.425 0 0 1 4.616-1.104c.803 0 1.505.1
 2.308.301l.2-1.204c-.702-.2-1.505-.301-2.408-.301Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Freep'''

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
