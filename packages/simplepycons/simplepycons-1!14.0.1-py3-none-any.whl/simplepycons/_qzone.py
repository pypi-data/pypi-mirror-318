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


class QzoneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qzone"

    @property
    def original_file_name(self) -> "str":
        return "qzone.svg"

    @property
    def title(self) -> "str":
        return "Qzone"

    @property
    def primary_color(self) -> "str":
        return "#FECE00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qzone</title>
     <path d="M23.9868
 9.2012c-.032-.099-.127-.223-.334-.258-.207-.036-7.352-1.4063-7.352-1.4063s-.105-.022-.198-.07c-.092-.047-.127-.167-.127-.167S12.4472.954
 12.3491.7679c-.099-.187-.245-.238-.349-.238-.104
 0-.251.051-.349.238C11.5531.954 8.0245 7.3 8.0245
 7.3s-.035.12-.128.167c-.092.047-.197.07-.197.07S.5546 8.9071.3466
 8.9421c-.208.036-.302.16-.333.258a.477.477 0 00.125.4491L5.5013
 15.14s.072.08.119.172c.016.104.005.21.005.21s-1.1891 7.243-1.2201
 7.451c-.031.208.075.369.159.4301.083.062.233.106.421.013.189-.093
 6.813-3.2614
 6.813-3.2614s.098-.044.201-.061c.103-.017.201.061.201.061s6.624
 3.1684 6.813 3.2614c.188.094.338.049.421-.013a.463.463 0
 00.159-.43c-.021-.14-.93-5.6778-.93-5.6778.876-.5401 1.4251-1.0392
 1.8492-1.7473-2.5944.9692-6.0069 1.7173-9.4163
 1.8663-.9152.041-2.4104.097-3.4735-.015-.6781-.071-1.1702-.144-1.2432-.438-.053-.2151.054-.4601.5451-.8312a2640.8625
 2640.8625 0 012.8614-2.1553c1.2852-.9681 3.5595-2.4703 3.5595-2.7314
 0-.285-2.1443-.781-4.0376-.781-1.9452
 0-2.2753.132-2.8114.168-.488.034-.769.005-.804-.138-.06-.2481.183-.3891.588-.5682.7091-.314
 1.8603-.594 1.9843-.626.194-.052 3.0824-.8051 5.6188-.5351 1.3181.14
 3.2444.668 3.2444 1.2762 0 .342-1.7212 1.4942-3.2254
 2.5973-1.1492.8431-2.2173 1.5612-2.2173 1.6883 0 .342 3.5334 1.2411
 6.6899
 1.01l.003-.022c.048-.092.119-.172.119-.172l5.3627-5.4907a.477.477 0
 00.127-.449z" />
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
