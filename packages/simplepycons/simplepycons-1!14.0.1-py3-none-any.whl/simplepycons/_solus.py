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


class SolusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "solus"

    @property
    def original_file_name(self) -> "str":
        return "solus.svg"

    @property
    def title(self) -> "str":
        return "Solus"

    @property
    def primary_color(self) -> "str":
        return "#5294E2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Solus</title>
     <path d="M7.453 0c-.18.587-.369 1.167-.565 1.75A11.638 11.638 0 0
 0 0 12.364a11.638 11.638 0 0 0 .516 3.403l-.339.598L0
 16.73l.279.143a3.448 3.448 0 0 0 .741.222A11.638 11.638 0 0 0 2
 18.868c4.034.343 8.55.512 12.446-.056 3.192-.463 5.94-1.423
 7.735-3.117.252-.233.474-.474.674-.722.019-.038.037-.053.06-.076.011
 0 .026-.037.038-.052.015 0 .03-.038.041-.057.008 0
 .015-.038.023-.038.33-.444.587-.892.801-1.31l.181-.365-.365-.365a5.936
 5.936 0 0 0-.361-.35A11.638 11.638 0 0 0 11.635.722a11.638 11.638 0 0
 0-3.211.463C7.96.508 7.596.041 7.453 0zm.365 1.637C9.06 3.82 10.13
 5.06 11.454 7.457c.132 1.524.67 9.45.727
 10.181-.392-.037-2.485-.24-5.104-.515-1.43-.147-2.899-.316-4.092-.49l-1.9-.447c2.149-3.787
 5.551-9.727 6.737-14.548zm4.543 6.18s4.991 3.927 7.092 8.73c-2.56
 1.26-4.916 1.098-6.361 1.09 1.023-2.634 1.023-6.21-.73-9.82zm3.456
 2.184a45.14 45.14 0 0 1 2.91.907c1.768.629 3.417 1.49 4.365
 2.364a6.956 6.956 0 0 1-2.91
 2.91c.151-1.495-.39-2.933-1.456-4.002-.787-.787-1.822-1.453-2.91-2.183zm6.707
 6.478c-2.352 1.667-5.126 2.68-7.965 3.112a41.026 41.026 0 0
 1-3.715.34h-.323a53.48 53.48 0 0 1-3.727 0 85.763 85.763 0 0
 1-4.178-.23h-.003c2.555 3.255 6.993 4.893 11.092 4.102a11.367 11.367
 0 0 0 4.498-1.852 11.638 11.638 0 0 0 .007
 0c.312-.214.614-.444.903-.685a11.638 11.638 0 0 0 .038-.037 11.555
 11.555 0 0 0 3.376-4.762zM2.511 19.584a11.638 11.638 0 0 0
 .023.038c-.008 0-.015-.038-.023-.038z" />
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
