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


class ArangodbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arangodb"

    @property
    def original_file_name(self) -> "str":
        return "arangodb.svg"

    @property
    def title(self) -> "str":
        return "ArangoDB"

    @property
    def primary_color(self) -> "str":
        return "#DDE072"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ArangoDB</title>
     <path d="M13.885
 3.75c-.32.007-.536.032-.61.041-.878.106-2.81.49-4.466
 2.088-.921.89-1.501 2.153-1.783
 2.826.251-.072.502-.13.75-.164.94-.131 1.8-.013 2.431.219.89-.158
 1.474-.228 1.782-.227.953.004 2.003-.008 2.775.65.208.178.82.542.725
 1.515-.084.867-.474 1.933-1.428 2.982-.574.632-1.686 1.444-3.059
 2.15-.995.511-2.412 1.313-4.469
 1.426-.331.019-.708.041-1.105.04-1.012-.004-2.48-.138-3.545-1.249-.221-.231-1.31-1.458-1.002-2.93.248-1.185
 1.229-1.798 2.016-2.292.447-.281 1.05-.512 1.861-.754.585-.63
 1.274-1.017 1.975-1.262-1.394.312-2.784.652-3.788 1.15-1.15.557-2.236
 1.082-2.707 2.237-.287.707-.263 1.42-.191 1.892 0 0 .31 3.096 2.441
 4.674 1.784 1.323 4.413 1.812 6.374 1.276 1.543-.294 3.015-1.738
 4.24-3.004l.006.004c.392.186 1.295.584 2.027.963 1.692.873 2.864
 1.054 3.47 1.16 1.317.23 3.368-.292 4.341-1.383.932-1.045
 1.203-2.454.98-3.711-.067-.386-.066-1.073-.349-2.016-.222-.737-.333-1.104-.494-1.496-.31-.758-.705-1.373-1.295-2.137-1.382-1.784-2.072-2.679-3.2-3.39-1.834-1.16-3.74-1.297-4.703-1.278zm.713
 1.135c.814.033 2.014.046 3.051.725.603.397 1.182.68 2.338 2.21 1.56
 2.069 1.711 2.301 2.293 3.405.443.84.822 2.55.65 3.885-.05.387-.09
 1.209-.95 2.021-1.157
 1.093-3.13.97-3.337.946-.629-.077-1.113-.371-2.582-.934l-1.816-.744c-.121-.048-.245-.115-.37-.18.417-.499
 1.182-1.488
 1.497-2.111.231-.466.385-.985.488-1.37.078-.308.195-.765.244-1.204.025-.229.045-.463.049-.663.004-.207-.001-.244-.01-.402a4.156
 4.156 0 0 0-.201-.926 2.408 2.408 0 0 0-.457-.748 2.623 2.623 0 0
 0-.51-.367c-.208-.113-.474-.216-.646-.283-.32-.125-.585-.196-1.067-.256a5.006
 5.006 0 0
 0-.451-.016c-.547.005-1.274.08-2.338.237-.68.095-1.357.208-2.024.334l.002-.006c.69-1.402
 1.67-2.392 3.35-2.983 1.075-.377 2.198-.595 2.797-.57zm.272
 2.566a2.08 2.08 0 0 0-.721.112c.378.093.743.284
 1.064.426.255.138.49.313.633.462.249.261.46.616.569.93.099.29.206.71.226
 1.06.009.15.016.22.012.438a8.02 8.02 0 0
 1-.053.711c-.054.488-.178.965-.256 1.272a7.829 7.829 0 0 1-.383
 1.144c.239.004.47-.002.602-.025.937-.164 1.561-1.126
 1.752-1.904.268-1.102-.285-2.02-.654-2.633-.349-.577-.963-1.384-2.073-1.834a2.09
 2.09 0 0 0-.718-.159zM7.844 9.035a4.64 4.64 0 0
 0-1.511.457c-.53.254-.99.648-1.573 1.335-.65.815-1.112 2.387-.76
 2.81.18.218.275.24.34.283.901.436 1.724 1.035 3.068
 1.114h1.118c.234.002.545-.05.632-.059 1.547-.254 3.605-1.349
 3.526-2.88-.03-.573-.683-1.512-1.127-1.935-.431-.41-1.147-.788-1.454-.917-.266-.131-.576-.167-.888-.213-.47-.078-.972-.048-1.371.005z"
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
