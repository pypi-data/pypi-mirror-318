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


class RenovateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "renovate"

    @property
    def original_file_name(self) -> "str":
        return "renovate.svg"

    @property
    def title(self) -> "str":
        return "Renovate"

    @property
    def primary_color(self) -> "str":
        return "#308BE3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Renovate</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.371
 12-12S18.63 0 12 0zM9.973 5.046L8.827 3.9l1.146-1.146 3.33 3.33-1.146
 1.147-1.085-1.086L9.858 7.36 8.766 6.267 9.98 5.053zM6.445
 3.933l1.147 1.146-1.147 1.144L5.3 5.077zM2.98 9.689L1.833
 8.543l1.146-1.146 1.146 1.146zm2.283 2.323l-1.17-1.17 1.146-1.146
 1.147 1.146L7.568 9.66l-1.123-1.12L5.3 7.391l1.146-1.146 2.27 2.269
 1.143-1.144 1.062 1.062-1.18 1.181-3.438 3.439zm3.726 3.406a.35.35 0
 01-.494 0l-1.58-1.578a.35.35 0 010-.494l6.668-6.669a.35.35 0 01.495
 0l1.577 1.578a.35.35 0 010 .494zM19.81
 19.01c-.24.248-.46.513-.76.7-.325.204-.951.15-1.22-.133-.127-.134-.263-.26-.392-.39-.877-.876-1.749-1.755-2.63-2.627-.274-.272-.433-.593-.347-.965.038-.157.134-.32.258-.504-.227-.225-.527-.549-.764-.802a1.687
 1.687 0 01-.298-.42c-.236-.499-.096-.932.272-1.31.422-.43.853-.855
 1.28-1.282l2.238-2.236c.045-.044.09-.084.13-.13.105-.13.105-.259.006-.39-.03-.04-.068-.075-.105-.112-.399-.399-.797-.797-1.196-1.193-.035-.036-.075-.07-.112-.106-.092-.082-.235-.077-.338-.005-.072.052-.138.115-.222.186l-.549-.535c.361-.6
 1.163-.731 1.671-.258.504.467.99.952 1.458 1.454a1.132 1.132 0
 01-.033 1.556l-.738.738-2.824 2.822a1.515 1.515 0
 00-.085.09c-.159.175-.164.339.003.51.248.258.504.509.776.783.23-.164.457-.26.726-.256.305.005.553.122.764.333.52.523
 1.043 1.043 1.564 1.564.464.464.911.942 1.394 1.385.392.36.525
 1.064.073 1.533z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.renovatebot.com/logo-brand-guide'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://avatars1.githubusercontent.com/u/3865'''

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
