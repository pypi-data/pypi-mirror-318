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


class ApacheParquetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apacheparquet"

    @property
    def original_file_name(self) -> "str":
        return "apacheparquet.svg"

    @property
    def title(self) -> "str":
        return "Apache Parquet"

    @property
    def primary_color(self) -> "str":
        return "#50ABF1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Parquet</title>
     <path d="M10.953 20.391c-.95-1.013-.978-1.057-.807-1.248.27-.304
 11.811-10.868 11.977-10.964.143-.083 1.558.6 1.867.902.119.115-.8
 1.098-5.817 6.218-3.277 3.345-6.021 6.095-6.097
 6.112-.076.016-.582-.442-1.123-1.02zM8.333
 17.7c-.511-.515-.835-.92-.803-1.003.058-.152 6.693-5.515
 6.817-5.51.153.005 1.714 1.191 1.714 1.302 0 .116-6.67 6.073-6.8
 6.073-.038 0-.456-.388-.928-.862zM5.91
 15.227c-.4-.448-.652-.81-.598-.86.28-.26 3.164-2.26 3.26-2.26.154.002
 1.547 1.196 1.547 1.327 0 .161-3.124 2.566-3.334 2.566-.1
 0-.494-.348-.875-.773zm-1.988-2.04c-.574-.58-.642-.69-.512-.81.187-.174
 9.357-6.094 9.545-6.162.146-.053 1.417.716 1.417.858 0 .102-9.401
 6.685-9.63
 6.744-.091.023-.435-.241-.82-.63zm6.117-.935c-.379-.314-.687-.626-.684-.692.002-.066.337-.354.743-.64.406-.285
 2.227-1.587 4.046-2.894 1.82-1.307 3.383-2.376 3.474-2.376.245 0
 1.485.717 1.445.835-.057.173-8.012 6.336-8.179 6.337-.086
 0-.467-.256-.845-.57zm-7.963-.923c-.452-.478-.518-.593-.4-.701.103-.093
 5.783-3.449 6.47-3.821.114-.062 1.318.807 1.28.922-.05.15-6.456
 4.172-6.645 4.172-.09
 0-.408-.257-.705-.572Zm13.735.038c-.416-.298-.772-.59-.792-.65-.028-.083
 3.74-3.215 4.595-3.818.166-.118.297-.079
 1.01.301.45.24.818.485.817.545-.002.152-4.487 4.098-4.7
 4.135-.096.016-.515-.214-.93-.513zM.547 9.707 0
 9.156l.243-.158c.133-.086 2.841-1.563
 6.018-3.282l5.775-3.126.553.27c.303.15.552.322.552.384 0 .084-11.875
 7.018-12.02 7.018-.015
 0-.274-.249-.574-.553zm8.88-2.79c-.269-.2-.487-.418-.487-.483s1.083-.755
 2.406-1.534l2.405-1.417.617.33c.34.18.617.363.617.406 0 .122-4.715
 3.07-4.904
 3.067-.092-.001-.387-.167-.655-.368Zm4.816-.612c-.325-.2-.589-.418-.588-.484.002-.112
 1.64-1.209 1.909-1.279.123-.032 1.226.55
 1.315.694.027.044-.031.15-.128.237-.333.296-1.7 1.202-1.81
 1.199-.06-.002-.374-.167-.698-.367z" />
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
