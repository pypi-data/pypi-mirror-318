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


class CohostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cohost"

    @property
    def original_file_name(self) -> "str":
        return "cohost.svg"

    @property
    def title(self) -> "str":
        return "cohost"

    @property
    def primary_color(self) -> "str":
        return "#83254F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>cohost</title>
     <path d="M15.306
 3.3449c-1.711-.0223-3.5155.2213-5.4157.7305-2.1819.5847-4.082
 1.4033-5.699 2.4592C2.574 7.5906 1.3988 8.844.666 10.2908c-.7329
 1.447-.8611 3.0584-.3848 4.8364.4737 1.768 1.3905 3.099 2.75 3.9906
 1.3594.8917 3.0042 1.394 4.9353 1.51 1.931.1159 3.9878-.1186
 6.1697-.7033 1.9645-.5264 3.6986-1.2507
 5.203-2.172-1.2805.086-3.208-.1-4.248-1.2658-.3806-.4267-.5702-.9619-.5702-1.6056
 0-.6474.1896-1.1847.5702-1.6095.3807-.4249.8935-.7437
 1.539-.9552.6456-.2115 1.3656-.3164 2.1601-.3164.7504 0 2.2412.109
 3.2733.8926.1537.1167.2925.2454.418.3848.2557.284.427.6164.5117.9982.12-.1956.231-.3947.334-.5977.7365-1.4534.868-3.0646.3945-4.8325-.4737-1.768-1.3927-3.0936-2.7558-3.9789-.4473-.2905-.9258-.5389-1.4335-.7461-1.2534-.5116-2.6405-.7549-4.2264-.7755Zm-6.7536
 8.655c.6216 0 1.1947.0558 1.7207.1661.526.1104.9764.2533
 1.3534.4317.377.1784.6511.37.8203.5723l-1.412.9259c-.206-.2244-.5182-.403-.9375-.5372-.4193-.1342-.9297-.2012-1.5293-.2012-.2942
 0-.5908.0224-.8905.0684-.2998.046-.5741.124-.8242.2344s-.4529.2662-.6055.4649c-.1526.1986-.2285.4506-.2285.756
 0
 .3015.0759.5493.2285.746.1526.1969.3554.353.6055.4689.25.1158.5244.1983.8242.246.8389.134
 1.7483.081
 2.4217-.1484.4322-.147.7356-.3165.9121-.5078l1.4472.922c-.1508.1618-.4181.3335-.7988.5156-.3806.182-.838.3359-1.375.461-.8718.203-2.0731.2818-3.322.0293-.5186-.1048-.987-.27-1.4063-.4981-.4193-.228-.7536-.5268-1.0019-.8946-.2482-.3679-.373-.814-.373-1.34
 0-.5334.1248-.9858.373-1.3536.2483-.3679.5826-.6625
 1.002-.8868.4192-.2244.8876-.3872 1.4061-.4884A8.2896 8.2896 0 0 1
 8.5524 12zm10.238 1.3791c-.7688
 0-1.3665.1338-1.795.4004-.4284.2667-.6425.6345-.6425 1.1017 0
 .4635.2141.8295.6426 1.1017.4284.2722 1.026.4102 1.7948.4102.7687 0
 1.366-.1383 1.789-.4141.423-.276.6328-.6417.6328-1.0978
 0-.4672-.2119-.835-.6367-1.1017-.4248-.2666-1.0201-.4004-1.785-.4004z"
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
