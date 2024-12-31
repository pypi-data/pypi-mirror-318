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


class ChainguardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chainguard"

    @property
    def original_file_name(self) -> "str":
        return "chainguard.svg"

    @property
    def title(self) -> "str":
        return "Chainguard"

    @property
    def primary_color(self) -> "str":
        return "#4445E7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chainguard</title>
     <path d="M23.9962
 16.329c-.1088-1.123-3.3873-1.488-5.717-2.501.5096-1.0168
 1.2826-2.168.9488-4.2865C18.7817 6.7253 16.3572 1.741 12
 1.741c-4.3571 0-6.7817 4.9807-7.228 7.8005-.3338 2.1184.4428
 3.2697.9488 4.2864-2.3262 1.0132-5.6046 1.3816-5.717 2.501-.102 1.038
 1.8904 1.417 4.1357 1.2824-.5657.6908-1.0084 1.3461-.9733
 1.8173.0562.79.896 1.3036 2.2207 1.3036 1.4829 0 3.774-.9388
 4.3186-3.4751 0 0-.225 1.0166-.102 1.9908.1476 1.162 1.019 3.0111
 2.3965 3.0111 1.3774 0 2.2489-1.8492
 2.3964-3.0111.123-.9742-.1018-1.9909-.1018-1.9909.5446 2.5364 2.8321
 3.4752 4.3185 3.4752 1.3247 0 2.1645-.5137
 2.2207-1.3036.0352-.4712-.411-1.13-.9733-1.8173 2.2453.1346
 4.2377-.2445 4.1358-1.2824zM7.4355
 5.953c-.26-.2232-.1897-.705.1547-1.077.3443-.3719.8362-.4959
 1.0962-.2727s.1898.705-.1545
 1.077c-.3444.3719-.8363.4923-1.0964.2727Zm2.3719 6.419c-1.0717
 0-1.9397-.875-1.9397-1.9555s.868-1.9555 1.9397-1.9555c1.0717 0
 1.9396.875 1.9396 1.9555 0 1.077-.868 1.9554-1.9396
 1.9554zm1.1841-7.7014c-.7555.34-1.5601.2232-1.799-.2586-.239-.4853.1792-1.1513.9346-1.4914.7555-.34
 1.5602-.2232 1.7991.2586.239.4818-.1792 1.1513-.9347 1.4914Zm5.218
 7.7013c-1.0716 0-1.9396-.875-1.9396-1.9554 0-1.0805.868-1.9555
 1.9397-1.9555 1.0717 0 1.9397.875 1.9397 1.9555 0 1.077-.868
 1.9554-1.9397 1.9554zm.1582-1.9696.7133-.8466a1.2052 1.2052 0 0
 0-.8714-.372c-.6746 0-1.2193.5491-1.2193 1.2293 0 .6801.5447 1.2292
 1.2193 1.2292.6747 0 1.2193-.5491 1.2193-1.2292v-.0107zm-5.3445
 0v.0107c0 .6802-.5447 1.2292-1.2194 1.2292-.6746
 0-1.2192-.549-1.2192-1.2292 0-.6801.5446-1.2292 1.2192-1.2292.3409 0
 .65.1417.8715.372l-.7133.8466Z" />
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
