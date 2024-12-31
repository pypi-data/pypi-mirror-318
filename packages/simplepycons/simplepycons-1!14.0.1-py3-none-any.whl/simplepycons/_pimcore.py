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


class PimcoreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pimcore"

    @property
    def original_file_name(self) -> "str":
        return "pimcore.svg"

    @property
    def title(self) -> "str":
        return "Pimcore"

    @property
    def primary_color(self) -> "str":
        return "#6428B4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pimcore</title>
     <path d="M24 10.579c0 .262-.212.474-.474.474H22.19c-.047
 0-.084.038-.084.084v.547H24v.158c0
 .262-.212.474-.474.474h-1.421v.547c0 .046.038.084.084.084H24v.158c0
 .261-.212.474-.474.474h-1.579a.4737.4737 0
 01-.474-.474v-2.211c0-.261.212-.474.474-.474H24v.159m-5.589.474a.095.095
 0 00-.095.095V12h1.421c.27 0
 .487-.227.473-.5-.014-.253-.228-.448-.481-.448h-1.318m2.431.46c.005.44-.246.821-.614
 1.004l.614 1.063h-.547c-.113
 0-.217-.06-.273-.158l-.456-.789h-1.25v.474c0
 .262-.212.474-.474.474h-.158v-2.684c0-.262.212-.474.474-.474h1.549c.61-.001
 1.128.48 1.135 1.09m-5.368 1.435c.522 0
 .947-.425.947-.947s-.425-.947-.947-.947c-.329
 0-.619.169-.789.424l-.348.523.345.52c.17.257.461.427.792.427m0-2.526c.872
 0 1.579.707 1.579 1.579s-.707 1.579-1.579 1.579c-.55
 0-1.034-.281-1.316-.707l-.2-.3-.43.648c-.396.597-1.074.991-1.844.991-1.221
 0-2.211-.99-2.211-2.211 0-1.221.99-2.211 2.211-2.211.767 0 1.442.39
 1.839.983l.056.084-.379.573-.207-.313c-.284-.419-.764-.695-1.308-.695-.871
 0-1.579.708-1.579 1.579s.708 1.579 1.579 1.579c.549 0 1.033-.281
 1.316-.707l1.156-1.742c.282-.427.766-.709 1.317-.709m-7.393.13l-1.067
 1.067a.0948.0948 0 01-.134 0l-1.065-1.065a.4468.4468 0
 00-.763.316v2.711h.158c.261 0
 .474-.212.474-.474v-1.69c0-.037.045-.056.072-.03l.856.856c.185.185.485.185.67
 0l.856-.856a.0422.0422 0 01.072.03v2.163h.158c.261 0
 .474-.212.474-.474v-2.242c0-.244-.198-.442-.442-.442h-.007c-.117
 0-.229.047-.312.13m-4.134 3.028c.262 0
 .474-.212.474-.474v-2.684h-.158c-.262
 0-.474.212-.474.474v2.684h.158M2.039 12c.255 0
 .475-.195.487-.45.013-.272-.204-.498-.473-.498H.726c-.052
 0-.095.043-.095.095V12h1.408m-.015-1.579c.619 0 1.146.507 1.134
 1.126-.011.601-.502 1.084-1.105 1.084H.632v.474c0
 .261-.212.474-.474.474H0v-2.684c0-.262.212-.474.474-.474h1.55" />
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
