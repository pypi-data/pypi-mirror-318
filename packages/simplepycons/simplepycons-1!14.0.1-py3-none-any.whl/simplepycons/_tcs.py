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


class TataConsultancyServicesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tcs"

    @property
    def original_file_name(self) -> "str":
        return "tcs.svg"

    @property
    def title(self) -> "str":
        return "Tata Consultancy Services"

    @property
    def primary_color(self) -> "str":
        return "#EE3984"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tata Consultancy Services</title>
     <path d="M24
 16.262c0-1.305-.522-2.174-1.827-3.088l-1.785-1.24c-.033-.022-.06-.045-.092-.068-.629-.473-.91-.912-.91-1.43
 0-.696.567-1.13 1.371-1.13 1.022 0 1.503.477 2.111.477.479 0
 .805-.326.805-.804
 0-.348-.174-.631-.631-.848-.718-.348-1.503-.48-2.35-.48-.892
 0-1.676.262-2.241.697a.984.984 0 0 0 0-.001 3.64 3.64 0 0
 0-.326.283l-.008.01c-.65.695-1.19 1.714-1.623 3.145l-.501 1.652c-.893
 2.912-2.306 4.304-4.504 4.304-2.415
 0-3.938-1.675-3.938-4.153v.026-.025c0-2.468 1.509-4.159
 3.69-4.174l.03-.002a4.857 4.857 0 0 1
 2.089.457c.282.13.522.174.74.174.1 0
 .192-.017.279-.041.362-.103.592-.408.592-.83
 0-.326-.196-.653-.653-.87-.827-.414-1.894-.653-3.046-.653-.86
 0-1.653.152-2.359.436-2.117.851-3.452 2.886-3.452
 5.545l.002-.024-.001.024c0 .931.169 1.783.479 2.536-.452.985-1.143
 1.509-2.046 1.509-1.087 0-1.804-.63-1.806-2.06V9.477h2.546c.588 0
 .979-.348.979-.848s-.39-.848-.98-.848H2.09V5.563c0-.653-.435-1.088-1.044-1.088C.435
 4.475 0 4.911 0 5.563v10.285c0 2.393 1.37 3.655 3.7
 3.655.486.001.97-.08 1.43-.24h.005a3.49 3.49 0 0 0 1.81-1.514c1.034
 1.117 2.565 1.775 4.48 1.775.999 0 1.868-.195
 2.65-.607h.003c1.588-.827 2.72-2.502 3.503-5.068l.457-1.5a2.984 2.984
 0 0 1-.162-.234c.308.492.785.953 1.468 1.43l1.631
 1.13c.244.17.463.34.668.51.289.322.378.67.378 1.078 0 .935-.74
 1.566-1.807 1.566-1.022 0-1.893-.522-2.371-.522s-.806.325-.806.804c0
 .348.174.63.632.848.631.304 1.653.566 2.567.566 1.153 0 2.111-.348
 2.785-.957a1.59 1.59 0 0 0 .156-.161A3.104 3.104 0 0 0 24 16.262z" />
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
        yield from [
            "TCS",
        ]
