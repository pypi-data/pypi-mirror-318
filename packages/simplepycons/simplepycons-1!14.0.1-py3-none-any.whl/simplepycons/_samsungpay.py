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


class SamsungPayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "samsungpay"

    @property
    def original_file_name(self) -> "str":
        return "samsungpay.svg"

    @property
    def title(self) -> "str":
        return "Samsung Pay"

    @property
    def primary_color(self) -> "str":
        return "#1428A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Samsung Pay</title>
     <path d="m6.703 17.387.617-1.5-1.205-2.795h.724l.817
 1.98.776-1.98h.711l-1.752 4.295Zm-2.492-1.295c-.708
 0-1.445-.569-1.445-1.528 0-.975.712-1.531 1.455-1.531.387 0
 .735.16.946.411v-.352h.677v2.94h-.677v-.382a1.222 1.222 0 0
 1-.956.442Zm-4.206-.06v-3.666h1.258c.759 0 1.32.581 1.32 1.305 0
 .728-.562 1.312-1.325 1.312H.69v1.05zm4.315-.562c.503 0
 .88-.407.88-.914 0-.497-.377-.906-.88-.906a.886.886 0 0 0-.888.906c0
 .512.386.914.888.914zM.69 14.348h.52c.408 0 .686-.3.686-.677a.66.66 0
 0 0-.685-.672H.69Zm.557-4.063C.603 10.285 0 10.055 0
 9.29v-.265h.92l.002.333c0 .187.13.31.344.31.228 0
 .305-.117.333-.232a.44.44 0 0 0-.005-.252C1.417 8.74.198 8.538.049
 7.837a1.192 1.192 0 0 1-.007-.463c.09-.56.588-.76 1.198-.76.485 0
 1.156.114 1.156.861v.242h-.854v-.213c0-.187-.12-.31-.32-.31-.215
 0-.289.122-.313.232a.435.435 0 0 0 .002.18c.098.401 1.4.615 1.545
 1.333.014.072.044.266.002.562-.081.573-.59.784-1.21.784zm11.154-.018c-.638
 0-1.234-.227-1.234-.984V9.02h.911v.328c0 .185.129.31.341.31.227 0
 .303-.117.331-.23a.438.438 0 0
 0-.005-.25c-.175-.44-1.382-.641-1.529-1.336a1.166 1.166 0 0
 1-.008-.458c.09-.554.585-.753 1.188-.753.48 0 1.143.115
 1.143.855v.24h-.846v-.212c0-.185-.116-.307-.315-.307-.212
 0-.289.12-.313.23a.435.435 0 0 0 .005.176c.096.398 1.385.61 1.529
 1.32.015.073.044.265.003.558-.081.567-.586.776-1.2.776zm3.224-.013c-.63
 0-1.138-.21-1.198-.85a2.792 2.792 0 0 1-.008-.223V6.72h.867v2.538c0
 .044 0 .093.008.13.017.085.092.248.331.248.238 0
 .311-.163.328-.248a.718.718 0 0 0 .008-.13V6.72h.867v2.461a2.94 2.94
 0 0 1-.008.224c-.06.64-.564.849-1.195.849zm7.156-.037c-.608
 0-1.148-.221-1.205-.846a2.518 2.518 0 0
 1-.014-.227V7.702c0-.061.009-.17.016-.227.077-.641.595-.846
 1.203-.846.608 0 1.14.203
 1.203.846.011.11.008.227.008.227v.114h-.864v-.193s0-.08-.01-.13c-.016-.075-.082-.25-.345-.25-.249
 0-.322.166-.34.25a.816.816 0 0 0-.014.162v1.567a.89.89 0 0 0
 .008.13c.016.092.104.25.352.25s.333-.158.349-.25a.722.722 0 0 0
 .008-.13v-.497h-.352v-.5H24v.92c0
 .064-.003.112-.013.226-.057.625-.598.846-1.206.846zm-19.745-.065.636-3.432h1.526l.633
 3.432h-.922l-.456-3.114-.02.002-.47 3.112Zm3.48 0L6.59 6.72h1.4l.421
 2.625h.021l.422-2.625h1.399l.075 3.432h-.857l-.02-3.083H9.43l-.573
 3.083h-.87L7.414 7.07h-.018l-.021 3.083Zm11.268-.036V6.72h1.273l.79
 2.693h.018l-.047-2.693h.851v3.396h-1.221l-.849-2.787h-.018l.047
 2.787z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://pay.samsung.com/developers/resource/b'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://pay.samsung.com/developers/resource/b'''

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
