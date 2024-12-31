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


class HThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "h3"

    @property
    def original_file_name(self) -> "str":
        return "h3.svg"

    @property
    def title(self) -> "str":
        return "H3"

    @property
    def primary_color(self) -> "str":
        return "#1E54B7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>H3</title>
     <path d="M8.2364
 6.1048c-.0992-.0445-.2566-.0838-.3729-.1728-.4858-.3746-.9596-.768-1.442-1.1478-.1728-.135-.195-.2788-.089-.4687.3097-.5576.5936-1.1324.9238-1.6763.1043-.1728.3096-.3319.5029-.3952.792-.2617
 1.5925-.5012 2.3999-.7116.1916-.0496.4499-.0086.6295.0839.5234.2685
 1.0246.5816
 1.5327.8826.2651.1574.2908.2327.1813.5217-.2155.5662-.4396
 1.1273-.6466
 1.697-.1095.2976-.3216.472-.609.5576-.8792.26-1.7602.5114-2.6411.7646-.101.0257-.207.036-.3695.065zm-6.1067
 4.9299c-.1317-.0838-.2943-.1437-.3918-.2583C1.3137 10.2769.91
 9.7586.4926 9.2523.3541 9.0846.3695 8.9119.467
 8.751c.4636-.7544.922-1.5105
 1.4146-2.246.113-.1677.337-.2977.5372-.3627.8176-.2634 1.6455-.4943
 2.4717-.7355.2583-.0753.491-.048.7082.1437.4413.39.8946.7697 1.3514
 1.1444.1915.1556.2275.3284.1265.5422-.3729.7834-.727 1.5772-1.1324
 2.3435-.1111.2121-.349.426-.5747.4978-1.0127.325-2.0407.602-3.0636.8929-.0462.0137-.0975.012-.1454.0171-.012.0188-.0206.0325-.0308.0462zm14.9281-9.1875c.1626.0462.337.0718.4876.1437.7167.342
 1.4266.6945 2.1365
 1.0486.2685.1334.4105.2822.3301.6448-.1368.6141-.231 1.2385-.3284
 1.8611-.048.3062-.2156.4961-.496.5782-1.052.308-2.1058.6073-3.1595.9015-.2823.0787-.5525.0086-.7954-.1522-.6877-.4585-1.3753-.9186-2.063-1.377-.1967-.1318-.2651-.296-.1796-.527.2275-.6226.4328-1.252.6808-1.8662.0633-.1556.231-.325.3866-.3746.9254-.2976
 1.8628-.5645
 2.7968-.8382.0616-.0188.13-.012.195-.017.0034-.0087.0068-.0172.0086-.0257zm-7.405
 10.8023c-.2002-.1095-.4345-.1848-.5953-.337-.609-.573-1.1923-1.1752-1.7927-1.7568-.2172-.212-.2668-.4379-.1437-.7099.3592-.7903.6996-1.589
 1.088-2.3657.0957-.1916.3181-.378.5234-.4447.9425-.3062 1.897-.573
 2.8498-.8416.26-.0736.52-.0377.7527.1248.6637.4653 1.3308.9289 1.9945
 1.3959.313.219.3712.3848.2668.7577-.2326.828-.472 1.6542-.6996
 2.482-.0992.3593-.3318.5817-.6774.6809-1.0776.3113-2.157.614-3.2364.9151-.094.0257-.1933.0274-.2908.0411a.8758.8758
 0 0 0-.0393.0582zM0
 16.098c.0907-.2292.1522-.4499.2583-.6466.4892-.9169.9921-1.827
 1.4882-2.7404.1847-.342.4584-.5696.833-.6756.946-.2686 1.8902-.5372
 2.8362-.8074.3575-.1027.6432-.0274.9049.2583.544.5918 1.1084 1.1632
 1.673 1.7345.2685.2703.3369.5679.2018.9186-.4294 1.1153-.8553
 2.2306-1.2881
 3.3424-.166.426-.4807.6877-.9237.8074-1.105.301-2.2084.609-3.3134.9135-.5371.1488-.756.0633-1.0503-.4037-.4618-.7339-.9288-1.4677-1.3856-2.205-.0906-.1505-.1505-.3181-.2343-.496Zm23.9857-6.1872c-.0565.9511-.106
 1.8697-.166
 2.7848-.0359.5337-.207.7356-.727.8793-1.1837.3284-2.369.6483-3.5528.9784-.4636.1283-.8741.0394-1.2436-.2583-.8946-.7184-1.7858-1.4403-2.6839-2.1553-.3301-.2634-.455-.5696-.337-.9921.2292-.8194.4362-1.6456.645-2.4718.0854-.337.2976-.5405.6191-.6346
 1.0076-.2925 2.0168-.5782 3.0243-.8673.3661-.1043.715-.0633
 1.0435.1283.9562.556 1.909 1.1153 2.8652
 1.6712.3712.219.5867.5183.5132.9374zM8.1612
 18.3251c.0923-.2976.1556-.5337.2377-.7646.3473-.9699.7133-1.9346
 1.0486-2.9097.171-.496.4841-.7834.9904-.9185 1.0212-.2686
 2.0339-.5645 3.05-.8536.4276-.1215.7971-.048 1.1426.248.8588.7356
 1.726 1.4608 2.5967 2.1844.4003.3336.5696.727.4687 1.2556-.2446
 1.2863-.4602 2.5795-.6928
 3.8693-.089.4892-.3797.8074-.8621.9374-1.3428.361-2.6873.7236-4.0336
 1.0742-.4875.1266-.8826-.0444-1.1956-.4327-.5714-.7082-1.1461-1.413-1.7209-2.1194-.2429-.2994-.5063-.585-.7218-.9015-.142-.2104-.2156-.4636-.308-.6689z"
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
        return '''https://github.com/uber/h3/blob/71e09dc002b21'''

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
