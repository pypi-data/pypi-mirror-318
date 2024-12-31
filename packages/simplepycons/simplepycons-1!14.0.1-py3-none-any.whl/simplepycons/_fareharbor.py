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


class FareharborIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fareharbor"

    @property
    def original_file_name(self) -> "str":
        return "fareharbor.svg"

    @property
    def title(self) -> "str":
        return "FareHarbor"

    @property
    def primary_color(self) -> "str":
        return "#0A6ECE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FareHarbor</title>
     <path d="M2.4746 3.9355c.0004.0135.002.0276.002.041 0 .7804-.6318
 1.4122-1.4122 1.4122-.0197
 0-.039-.0012-.0585-.002v1.4746c.0195-.0018.0385-.0058.0585-.0058.3534
 0 .6387.2873.6387.6406a.6379.6379 0 0 1-.6387.6387c-.02
 0-.039-.004-.0585-.0059v1.168c.0195-.0018.0385-.0059.0585-.0059a.6379.6379
 0 0 1 .6387.6387c0 .3533-.2853.6406-.6387.6406-.02
 0-.039-.004-.0585-.0059v1.166c.0195-.0018.0385-.0059.0585-.0059.3534
 0 .6387.2873.6387.6407a.6379.6379 0 0 1-.6387.6386c-.02
 0-.039-.004-.0585-.0059v1.4317c.0195-.0008.0388-.004.0585-.004.7804 0
 1.4122.6338 1.4122 1.4141v.0117h19.0879v-.0117c0-.7803.6317-1.414
 1.412-1.414.0064 0
 .0114.0019.0176.002v-1.4258c-.0063.0002-.0112.002-.0175.002-.3534
 0-.6407-.2854-.6407-.6387a.6412.6412 0 0 1 .6407-.6406c.0064 0
 .0112.0018.0175.002v-1.1582c-.0063.0002-.0112.002-.0175.002a.6412.6412
 0 0 1-.6407-.6406c0-.3534.2873-.6387.6407-.6387.0064 0
 .0112.0018.0175.002V8.1327c-.0063.0002-.0112.002-.0175.002-.3534
 0-.6407-.2854-.6407-.6387a.6412.6412 0 0 1 .6407-.6406c.0064 0
 .0112.0017.0175.002V5.3886h-.0175c-.7804 0-1.4121-.6318-1.4121-1.4121
 0-.0135.0016-.0276.002-.041zm9.5176.832c.035.0001.07.0088.1016.0274l3.3906
 2.0059a.1996.1996 0 0 1 .121.1836.2015.2015 0 0
 1-.2011.2011h-.8204v3.6094h1.0176v1.0567l-.6406.6015v1.795h5.371c.187
 0
 .34-.174.34-.3887V6.039c0-.2148-.153-.3887-.34-.3887h-4.7948V5.248h4.795c.4082
 0 .7402.355.7402.791v7.8204c0 .436-.332.791-.7403.791H3.6836c-.4082
 0-.7402-.355-.7402-.791V6.039c0-.4361.332-.791.7402-.791h4.7187v.4023H3.6836c-.1868
 0-.3398.174-.3398.3887v7.8203c0
 .2147.153.3886.3398.3886h5.3281v-1.8046l-.6308-.5918v-1.0567h1.0175V7.1855H8.582a.2032.2032
 0 0 1-.1953-.1484.1993.1993 0 0 1
 .0918-.2246l3.4121-2.0176a.1977.1977 0 0 1 .1016-.0273zm0
 .4337-2.6777 1.582h5.3535zm7.1445 1.662a.203.203 0 0 1
 .166.1485.2001.2001 0 0 1-.1406.2461l-3.2305.877a.2007.2007 0 0
 1-.0527.0078.2008.2008 0 0 1-.1934-.1485.2002.2002 0 0 1
 .1407-.246l3.2304-.879a.1993.1993 0 0 1 .0801-.0058zM5.0312
 6.916a.202.202 0 0 1 .0801.0059l2.9278.8261a.201.201 0 0
 1-.0547.3946.1996.1996 0 0 1-.0547-.0078l-2.9258-.8262a.201.201 0 0
 1-.1387-.248.1983.1983 0 0 1
 .166-.1446Zm4.7696.2695v3.6094h1.996v-.6094c-.5804-.0931-1.0253-.5967-1.0253-1.203
 0-.6064.4449-1.11 1.0254-1.2032v-.5938zm2.3984 0v.5977c.5734.0992
 1.0117.5979 1.0117 1.1992 0 .6014-.4383 1.102-1.0117
 1.2012v.6113h1.9824V7.1855Zm-.207.9786c-.451 0-.8184.3674-.8184.8183
 0
 .451.3674.8184.8184.8184s.8164-.3674.8164-.8184-.3654-.8183-.8164-.8183zm-7.8477.6308h3.4297a.1998.1998
 0 0 1 .1992.2012.1999.1999 0 0 1-.1992.2012H4.1445a.2015.2015 0 0
 1-.2011-.2012.2015.2015 0 0 1 .2011-.2012zm12.1465
 0h3.4297a.2015.2015 0 0 1 .2012.2012.2015.2015 0 0
 1-.2012.2012H16.291a.2015.2015 0 0 1-.2012-.2012.2015.2015 0 0 1
 .2012-.2012zm-8.2832.9024a.2011.2011 0 0 1 .17.1425.2009.2009 0 0
 1-.1348.25l-2.7207.8204a.2043.2043 0 0 1-.0586.0078.2021.2021 0 0
 1-.1934-.1426.2008.2008 0 0 1 .1348-.25l2.7226-.8203a.2033.2033 0 0 1
 .0801-.0078zm7.8496 0a.204.204 0 0 1
 .0801.0078l3.0762.9238a.2009.2009 0 0 1 .1347.25.2018.2018 0 0
 1-.1933.1426.1912.1912 0 0 1-.0567-.0078l-3.0761-.9238a.201.201 0 0
 1-.1348-.25.2007.2007 0 0 1 .17-.1426zm-7.0762
 1.5v.4804l.5157.4825h5.3886l.5157-.4825v-.4804H9.3984Zm.631
 1.3652v1.1563l3.0038-1.1563Zm4.121 0-4.0937
 1.5762c-.009.0034-.0184.0018-.0274.0039v.1054h2.5352l2.6113-1.1074v-.5781Zm1.0254
 1.0137-1.6074.6718h1.6074zM0
 17.6172v2.4121h.5078v-.9336h1.1777v-.4824H.5078v-.5137h1.336v-.4824zm9.5195
 0v2.4121h.4844v-1.0117h1.002v1.0117h.5058v-2.4121h-.5058v.9433h-1.002v-.9433zm10.9434.3476c-.6406
 0-1.1074.4721-1.1074 1.0489v.0059c0 .5766.461 1.0449 1.1015
 1.0449.6407 0 1.1055-.4742
 1.1055-1.0508v-.0059c0-.5766-.459-1.043-1.0996-1.043zm-17.5645.0215-.8906
 2.043h.4668l.1895-.455h.877l.1894.455h.4785l-.8906-2.043zm9.9805
 0-.8887
 2.043h.4649l.1894-.455h.879l.1894.455h.4766l-.8887-2.043ZM4.707
 18v2.0293h.457v-.6504h.3575l.4453.6504H6.5l-.5059-.7246c.264-.0955.4454-.3015.4454-.629V18.67c0-.4173-.2939-.6699-.7832-.6699Zm2.4395
 0v2.0293h1.582v-.3984h-1.127v-.4258h.9786v-.3965h-.9785v-.4121h1.1113V18Zm7.541
 0v2.0293h.457v-.6504h.3594l.4453.6504h.5332l-.5078-.7246c.264-.0955.4453-.3015.4453-.629V18.67c0-.4173-.2938-.6699-.7832-.6699Zm2.3828
 0v2.0293h.9863c.4686 0
 .7774-.1857.7774-.5566v-.006c0-.2723-.1485-.4082-.3887-.498.1483-.081.2735-.2085.2735-.4375v-.0059c0-.3187-.2616-.5253-.6856-.5253Zm5.1348
 0v2.0293h.457v-.6504h.3594l.4453.6504H24l-.5078-.7246c.264-.0955.4453-.3015.4453-.629V18.67c0-.4173-.2938-.6699-.7832-.6699Zm-1.748.377c.3678
 0 .6269.289.6269.6367v.0059c0 .3476-.2534.6328-.6211.6328-.3677
 0-.629-.2909-.629-.6387v-.0059c0-.3478.2555-.6308.6231-.6308zm-2.9434.0136h.4511c.1928
 0 .3008.0758.3008.209v.006c0
 .1506-.1285.2148-.33.2148h-.422zm-12.3496.0117h.453c.2225 0
 .3595.0998.3595.291v.006c0 .171-.1272.287-.3496.287h-.463Zm9.9804
 0h.4551c.2224 0 .3574.0998.3574.291v.006c0
 .171-.1271.287-.3496.287h-.4629zm7.5176 0h.455c.2225 0
 .3575.0998.3575.291v.006c0
 .171-.1271.287-.3496.287h-.4629zm-19.5605.1192.2773.6582h-.5527Zm9.9824
 0 .2754.6582h-.5508zm4.4297.67h.5293c.2343 0
 .3379.0844.3379.2206v.006c0 .1506-.1225.2187-.3243.2187h-.543z" />
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
