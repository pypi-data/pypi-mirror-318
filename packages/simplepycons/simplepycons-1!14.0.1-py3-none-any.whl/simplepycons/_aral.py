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


class AralIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aral"

    @property
    def original_file_name(self) -> "str":
        return "aral.svg"

    @property
    def title(self) -> "str":
        return "ARAL"

    @property
    def primary_color(self) -> "str":
        return "#0063CB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ARAL</title>
     <path d="M5.393 10.02l-.48
 1.959.99.001-.51-1.96zm3.892.082v1.187c.549-.002.958.03
 1.229-.033.27-.062.404-.217.404-.592
 0-.334-.12-.469-.385-.523-.264-.055-.672-.028-1.248-.04zm5.326-.079l-.48
 1.96h.99l-.51-1.96zM11.996 0L0 11.998 12.004 24 24 12.004 11.996
 0zM5.393 8.896c.366 0 .606.117.775.295.169.18.267.421.35.67l1.07
 3.211s.134.276.144.567c.01.29-.104.599-.6.666-.355-.054-.536-.156-.657-.35-.122-.194-.184-.482-.305-.91H4.645c-.147.468-.195.757-.295.941-.1.184-.254.263-.616.317-.508-.054-.636-.369-.636-.67
 0-.301.129-.588.129-.588l1.015-3.152c.08-.246.176-.495.348-.682.172-.187.42-.315.803-.315zm9.191.002c.366
 0 .607.117.775.295.17.18.267.421.35.67l1.072
 3.211s.135.276.145.567c.01.29-.104.599-.6.666-.356-.054-.536-.156-.658-.35-.122-.194-.186-.482-.307-.91h-1.525c-.147.468-.193.757-.293.941-.1.184-.256.263-.617.317-.509-.054-.635-.367-.635-.668
 0-.301.127-.59.127-.59l1.016-3.152c.075-.233.17-.484.343-.674.174-.19.424-.323.807-.323zm3.346.002c.308
 0 .483.114.58.291.097.178.117.418.117.672v3.207c.215.005 1.23 0 1.23
 0 .29 0
 .53.02.694.106.164.086.252.239.244.504-.01.361-.18.517-.406.582-.226.065-.509.039-.744.039h-1.766c-.375
 0-.536-.165-.604-.436-.067-.27-.04-.645-.04-1.062v-2.94c-.014-.254.02-.496.126-.674.107-.177.288-.289.569-.289zm-8.645.104h1.098c.254
 0 .51-.002.767.084.259.086.52.26.786.613.28.378.35.933.222
 1.414-.128.481-.456.889-.972.969.187.348.804 1.283.804
 1.283s.066.11.078.266c.012.155-.03.357-.25.539-.388.147-.633.106-.78.03-.149-.078-.2-.192-.2-.192s-.562-.964-.91-1.633h-.643v1.338s.01.154-.064.305c-.075.15-.236.298-.578.285-.327
 0-.488-.155-.567-.309C7.997 13.842 8 13.69 8
 13.69V9.861c0-.334.006-.549.17-.68.164-.13.486-.177 1.115-.177z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Aral_'''

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
