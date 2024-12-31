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


class KeycdnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keycdn"

    @property
    def original_file_name(self) -> "str":
        return "keycdn.svg"

    @property
    def title(self) -> "str":
        return "KeyCDN"

    @property
    def primary_color(self) -> "str":
        return "#047AED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KeyCDN</title>
     <path d="M2.3043 19.0607c.2259.01.4538.04.6667.12v-.003l.032.012
 2.8091-2.7391.102.137c.146.1998.2999.3798.4638.5597l.06.068c.043.043.077.086.12.13l.3259.3249.077.07.07.06a7.4626
 7.4626 0 004.6534 1.7753 7.5146 7.5146 0
 004.0087-1.0396l.216.224c.2499.2658.5068.5327.7557.7997a8.8581 8.8581
 0 01-5.0154 1.3995 8.8341 8.8341 0 01-5.4612-2.0623l.01-.015-1.8024
 1.7764A2.2463 2.2463 0 110 21.305a2.2453 2.2453 0
 012.2453-2.2453h.058zM19.4737 7.4765a8.8321 8.8321 0 011.2796 4.8264
 8.7872 8.7872 0 01-2.2073 5.6152l.01.01 1.1066
 1.1766c.4459-.06.8918.094 1.2017.4199a1.3935 1.3935 0 01-.052 1.9663
 1.3935 1.3935 0 01-1.9664-.052 1.3826 1.3826 0 01-.3519-1.2196
 336.5811 336.5811 0 00-1.9493-2.0693l-.11-.12.128-.103a6.9212 6.9212
 0 00.9277-.8846 7.4256 7.4256 0 001.8793-4.7755 7.4376 7.4376 0
 00-.9267-3.8118l1.0297-.9796zM3.8267 2.226c.395-.006.7648.15
 1.0397.432.31.3258.4399.7817.353 1.2195L7.3475 6.111l-.128.104a6.9208
 6.9208 0 00-.9276.8847 7.4906 7.4906 0 00-.9617
 8.5942l-1.0217.9957A8.7602 8.7602 0 013.021
 11.838c.044-2.0673.8498-4.0646 2.2033-5.6201L4.0517 4.9933a1.4005
 1.4005 0 01-1.2026-.42 1.3955 1.3955 0
 01.052-1.9673c.2169-.204.4968-.3349.7937-.3699.044-.006.09-.007.133-.01zM21.746.4427a2.2473
 2.2473 0 11-.6998 4.3806l-.002.002-.033-.012-3.049
 2.894-.102-.1379a7.1777 7.1777 0
 00-.5328-.6268l-.034-.043-.2659-.2659-.12-.103-.077-.07-.06-.0499-.0769-.07a7.4556
 7.4556 0 00-4.6185-1.7514A7.4336 7.4336 0 008.0724
 5.629l-.9797-1.0216a8.8371 8.8371 0 015.0154-1.3996 8.7912 8.7912 0
 015.4622 2.0694h.017l2.0194-1.9164A2.2463 2.2463 0
 0121.75.4438zM11.956 5.4581c.254 0 .5069.02.7598.05 3.6228.4548 6.19
 3.7608 5.7441 7.3846a6.6239 6.6239 0 01-7.3846 5.7451 6.6239 6.6239 0
 01-5.7461-7.3846c.4318-3.3619 3.257-5.7831 6.6258-5.7951zm-.1
 2.839c-1.4655.117-2.5271 1.2267-2.5651 2.6992.027 1.0537.5648 1.9394
 1.5045 2.4252l-.5118 2.3993h3.4219l-.5099-2.3993c.9347-.5068
 1.4896-1.3455
 1.5046-2.4222-.02-1.5215-1.1977-2.6671-2.7052-2.7051l-.14.004zm.052-.015h-.01z"
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
