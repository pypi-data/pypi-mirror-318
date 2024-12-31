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


class HellofreshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hellofresh"

    @property
    def original_file_name(self) -> "str":
        return "hellofresh.svg"

    @property
    def title(self) -> "str":
        return "HelloFresh"

    @property
    def primary_color(self) -> "str":
        return "#99CC33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HelloFresh</title>
     <path d="M9.7894
 22.2329c-.9661-.0974-2.0001-.326-3.042-.7589-.5912-.2456-1.1673-.5843-1.2123-.6109-.362-.2057-.6568-.457-1.2135-.7269-.7048-.3416-1.3836-.5276-2.1106-.611-.9842-.0661-1.038.0124-1.319-.0745-.1676-.0545-.3188-.1205-.495-.2848-.0526-.049-.125-.1304-.1607-.1808-.125-.1763-.1744-.3314-.194-.3997-.0284-.0981-.0424-.1563-.0423-.3324
 0-.1565.0152-.2397.035-.3116.0763-.2788.173-.3408.4299-.8472.3285-.6476.5238-1.285.6176-1.9564a5.7292
 5.7292 0 0 0
 .0554-1.017c-.015-.5062-.0383-.6133-.0392-1.0444-.0026-1.2549.2374-2.3546.5533-3.2859.2061-.6079.3889-1.007.6046-1.4333.5845-1.1551
 1.5013-2.4784 2.9354-3.6924.7732-.6545 1.9737-1.5002 3.5538-2.1176
 1.3446-.5253 2.5225-.7015 3.064-.7614.664-.087 1.8067-.1234
 2.975.0535.9966.151 2.2445.4867 3.5131 1.2.4312.2424.6815.4377
 1.014.6296.814.4697 1.6498.7054 2.4477.8015.424.051 1.0618.0047
 1.302.0666.1477.0381.2551.0862.3896.1755.1135.0755.3629.2761.4912.6485.061.1772.1243.6076-.0987.9911-.0365.063-.1066.183-.1557.2669-.0491.0838-.1423.2622-.2072.3964-.6611
 1.3677-.6465 2.5461-.6009 3.263.0534.84.05 2.2341-.5417
 3.9644-.1037.3032-.3364.9313-.7023 1.6143-.8281 1.5455-1.876
 2.6331-2.5374 3.2256-1.474 1.3204-2.9634 2.038-3.9265
 2.4021-.8975.3393-1.5834.5095-2.3024.6327-.6934.1188-1.8193.2425-3.0802.1154z"
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
        return '''https://www.hellofreshgroup.com/en/newsroom/p'''

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
