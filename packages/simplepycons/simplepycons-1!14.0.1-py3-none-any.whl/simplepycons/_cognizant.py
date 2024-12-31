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


class CognizantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cognizant"

    @property
    def original_file_name(self) -> "str":
        return "cognizant.svg"

    @property
    def title(self) -> "str":
        return "Cognizant"

    @property
    def primary_color(self) -> "str":
        return "#1A4CA1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cognizant</title>
     <path d="M1.955 9.425C.842 9.425 0 10.265 0 11.38c0 1.132.821
 1.953 1.953 1.953.73 0 1.374-.405
 1.725-1.084l.01-.02-.695-.368-.009.023c-.206.437-.588.686-1.046.686-.663
 0-1.18-.523-1.18-1.192 0-.686.515-1.202 1.197-1.202.442 0 .778.208 1
 .617l.01.022.668-.427-.012-.019a1.906 1.906 0 0
 0-1.666-.944zm20.78.189v.903h-.467v.673h.465v.876c0 .892.285 1.188
 1.155 1.188h.108v-.701c-.459
 0-.515-.066-.515-.493v-.87H24v-.673h-.515v-.903zm-9.858.002v.68h.75v-.68zm-4.727.845c-.619
 0-1.33.456-1.33 1.425 0 .963.738 1.422 1.315 1.424.356 0
 .647-.148.827-.362v.257c0 .356-.257.673-.662.673a.802.802 0 0
 1-.761-.465l-.662.373c.22.428.73.79 1.425.79.926 0 1.413-.625
 1.413-1.397v-2.662h-.75v.295a1.07 1.07 0 0 0-.815-.35zm9.599 0c-.619
 0-1.331.456-1.331 1.425 0 .963.739 1.422 1.32 1.424.356 0
 .646-.148.826-.362v.308h.75v-2.739h-.75v.266c-.18-.19-.459-.322-.815-.322zm-6.234.002a.941.941
 0 0 0-.756.362v-.308h-.744v2.739h.75V11.76c0-.46.236-.656.52-.656.334
 0
 .505.214.505.581v1.57h.76v-1.67c0-.706-.389-1.122-1.035-1.122zm9.602
 0a.941.941 0 0 0-.755.362v-.308h-.744l-.002
 2.739h.75V11.76c0-.46.236-.656.52-.656.336 0
 .505.214.505.581v1.57h.76v-1.67c0-.706-.387-1.122-1.034-1.122zm-15.9.01a1.42
 1.42 0 0 0-1.423 1.413l-.002.01a1.42 1.42 0 1 0
 1.425-1.423zm8.704.044v.662h1.42l-1.44
 1.408v.669h2.474v-.664h-1.468l1.44-1.402v-.673zm-1.055.008v2.738h.75v-2.738zm-4.58.622c.406
 0 .702.328.702.733 0 .405-.296.739-.701.739a.72.72 0 0
 1-.733-.739c0-.422.317-.733.733-.733zm9.598 0c.405 0
 .7.328.7.733.003.405-.293.739-.7.739a.72.72 0 0
 1-.733-.739c0-.422.319-.735.733-.733zm-12.671.026c.382 0
 .69.325.69.713a.704.704 0 0 1-.69.712c-.388 0-.684-.322-.684-.712
 0-.39.296-.713.684-.713z" />
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
