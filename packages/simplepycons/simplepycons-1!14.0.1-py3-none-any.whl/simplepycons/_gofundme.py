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


class GofundmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gofundme"

    @property
    def original_file_name(self) -> "str":
        return "gofundme.svg"

    @property
    def title(self) -> "str":
        return "GoFundMe"

    @property
    def primary_color(self) -> "str":
        return "#00B964"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoFundMe</title>
     <path d="M21.6236 4.0792l-4.2223 3.0705c-.6695.4892-.8127
 1.4224-.3309 2.0922.4892.6698 1.4221.8128
 2.0921.3312l4.2219-3.0706c.67-.4892.8127-1.4224.3313-2.0922a1.4883
 1.4883 0 0 0-2.092-.3312zm-9.6483-1.1816c-.8278 0-1.4978.6698-1.4978
 1.4976v2.5212c0 .8279.67 1.4977 1.4978 1.4977.8279 0 1.4974-.6698
 1.4974-1.4977V4.3952c0-.8278-.6695-1.4976-1.4974-1.4976zM.2877
 4.4103c-.4892.6698-.3387 1.603.3308 2.0922L4.841 9.573c.6695.4891
 1.6029.3386 2.092-.3312.4893-.6698.3387-1.603-.3313-2.0922L2.3798
 4.0792c-.6773-.4817-1.6107-.3387-2.092.331zm3.695 7.7893C6.1051
 10.303 8.905 9.144 11.9753 9.144c3.0705 0 5.8702 1.159 7.9926
 3.0555zm14.5556 1.6335c-1.3473
 0-2.236.4433-2.8004.9926-.5948.587-1.0232 1.5058-1.0232 2.6497 0
 1.302.5646 2.1445 1.0089 2.5885.843.843 1.926 1.0385 2.829 1.0385
 1.4827 0 2.2804-.4586
 2.7843-.9478.5043-.4892.7234-1.024.8284-1.4078H19.825c-.1056.2107-.279.3687-.4296.459-.3083.1656-.7368.1814-.797.1814-.5492
 0-.8583-.1883-1.0088-.3388-.2933-.286-.4296-.7757-.4296-1.1445h5.095v-.2634c0-.7601-.12-1.9567-1.0833-2.8749-.8132-.7676-1.8358-.9325-2.6334-.9325zm.0601
 1.5577c.241 0 .6845.0448
 1.008.3684.1881.1882.3384.4744.399.7378h-2.77c.0455-.3085.2038-.5572.3694-.7378.2561-.2634.5797-.3684.9936-.3684zm-16.851-1.3549h2.446v.8279c.5795-.7
 1.377-.9483 2.047-.9483.4893 0 .9482.1054
 1.3171.3086.5044.2634.783.6397.948.9783.2786-.4892.6251-.7827.9335-.9482.4892-.2785.9632-.3387
 1.4226-.3387.5038 0 1.3317.0753 1.8961.6247.61.5945.6397 1.4073.6397
 1.8814v4.4553h-2.4459v-3.379c0-.7226-.0753-1.2117-.3533-1.4676-.1359-.1204-.324-.2258-.6397-.2258-.2786
 0-.5044.0753-.7228.2785-.414.3988-.4437.9633-.4437
 1.302v3.507H6.346v-3.3791c0-.6548-.0454-1.1816-.324-1.4676-.2106-.2258-.4891-.2784-.7374-.2784-.2634
 0-.474.0451-.6695.2483-.429.414-.429 1.0687-.429
 1.4977v3.3791H1.74v-6.856Z" />
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
