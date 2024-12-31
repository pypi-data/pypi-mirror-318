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


class VeritasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "veritas"

    @property
    def original_file_name(self) -> "str":
        return "veritas.svg"

    @property
    def title(self) -> "str":
        return "Veritas"

    @property
    def primary_color(self) -> "str":
        return "#B1181E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Veritas</title>
     <path d="M0 9.746l1.248
 3.8712c.1053.3243.4072.5332.7344.5332a.7684.7684 0
 00.7324-.5332l1.248-3.8711h-.6933L2.086 13.412a.1081.1081 0
 01-.1035.0762c-.0467 0-.0881-.028-.1054-.0762L.6934 9.7461H0zm5.3125
 0c-.6081 0-1.0996.4939-1.0996 1.1017v2.2011c0 .6078.4915 1.1016
 1.0996 1.1016h2.0918v-.6621H5.3125a.439.439 0
 01-.4395-.4395v-.7754h2.0918v-.6504H4.873v-.7753c0-.2431.1964-.4414.4395-.4414h2.0918V9.746H5.3125zm3.7598
 0a.9898.9898 0
 00-.9903.9903v3.414h.6602v-3.414c0-.1825.1475-.33.33-.33h1.4317a.5505.5505
 0 01.5137.3535.55.55 0
 01-.3164.7109l-1.1094.4082c-.4025.139-.615.578-.4766.9805a.7665.7665
 0 00.4141.4531l2.0742.9414v-.7226l-1.8144-.8028a.1306.1306 0
 01-.0703-.0781.1302.1302 0
 01.082-.166l1.1367-.3965c.6243-.2396.9366-.9402.6973-1.5645-.1851-.4815-.6442-.7773-1.1309-.7773H9.0723zm3.3086
 0v4.4044h.662V9.746h-.662zm1.2109
 0v.6602h1.2773v3.7442h.6602v-3.7441h1.2773V9.746h-3.2148zm4.707
 0a.7683.7683 0 00-.7324.5333l-1.25 3.871h.6953l1.1836-3.6679a.108.108
 0 01.1035-.0762c.0467 0 .0882.0283.1055.0762l1.1816
 3.668h.6954l-1.25-3.8711a.7702.7702 0 00-.7325-.5332zm3.334 0c-.6992
 0-1.2656.5665-1.2656 1.2657 0 .6993.5664 1.2656 1.2656
 1.2656l1.1016.002c.3344 0 .6054.2693.6054.6035a.6054.6054 0
 01-.6054.6055h-2.1465v.662h2.1465c.6992 0 1.2656-.5683
 1.2656-1.2675s-.5664-1.2656-1.2656-1.2656h-1.1016a.6054.6054 0
 01-.6055-.6055c0-.3344.271-.6054.6055-.6054h2.1465V9.746h-2.1465Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://my.veritas.com/cs/groups/partner/docu'''

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
