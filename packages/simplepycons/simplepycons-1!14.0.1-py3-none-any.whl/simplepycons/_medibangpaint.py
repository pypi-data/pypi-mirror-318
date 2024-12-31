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


class MedibangPaintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "medibangpaint"

    @property
    def original_file_name(self) -> "str":
        return "medibangpaint.svg"

    @property
    def title(self) -> "str":
        return "MediBang Paint"

    @property
    def primary_color(self) -> "str":
        return "#00DBDE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MediBang Paint</title>
     <path d="M15.516 0H6.478L4.417.164a5.158 5.158 0 0 0-3.184 1.827
 5.479 5.479 0 0 0-.981 2.06C-.068 5.336.015 6.992.015 8.548v7.284c0
 2.377.038 4.504 1.007 5.878a5.153 5.153 0 0 0 2.435 1.873c1.232.332
 2.509.467 3.783.401h6.967c.622 0 1.25.007 1.87.007 2.149 0 4.19-.092
 5.504-.921a5.073 5.073 0 0 0
 2.013-2.53c.459-1.308.398-3.127.398-4.871V9.415c0-3.264.115-5.748-1.335-7.565C21.208.033
 18.727 0 15.516 0Zm0 .327a23.237 23.237 0 0 1 4.167.237 4.316 4.316 0
 0 1 2.718 1.49 5.645 5.645 0 0 1 1.108 2.823c.143 1.284.195 2.576.156
 3.867v7.475c.005 1.52.011 3.092-.382 4.212a4.724 4.724 0 0 1-1.878
 2.36 5.749 5.749 0 0 1-2.307.724 23.456 23.456 0 0
 1-3.021.147l-1.87-.008H7.241a11.983 11.983 0 0 1-3.675-.381 4.828
 4.828 0 0 1-2.276-1.754 5.279 5.279 0 0 1-.81-2.414 26.103 26.103 0 0
 1-.137-3.272V8.548c0-.268 0-.545-.005-.812A15.618 15.618 0 0 1 .567
 4.13a5.19 5.19 0 0 1 .927-1.94A4.833 4.833 0 0 1
 4.464.491L5.852.382l.639-.055h9.025Zm2.147
 8.845-.174-.286-.26-.357a7.147 7.147 0 0
 0-.267-.331c-.029-.034-.055-.061-.085-.094.362 7.124-6.189
 10.879-10.683 7.917a6.694 6.694 0 0 0 5.716 3.224c3.665 0 6.68-3.015
 6.68-6.679 0-1.194-.32-2.366-.927-3.394ZM5.674
 14.978c.081.207.636.521.795.626 4.195 2.764 10.247-.825
 9.908-7.474-.007-.148-.006-.538-.089-.61a7.696 7.696 0 0
 0-1.44-.995c-1.103 3.961-6.324 6.303-9.404 4.362a6.615 6.615 0 0 0
 .23 4.091Zm-.075-4.598c.033.033.07.061.111.084 1.117.704 2.547.769
 3.922.385 2.116-.591 4.119-2.248
 4.735-4.458.014-.05.039-.156.028-.165a3.428 3.428 0 0
 1-.341-.296c-.679-.715-.826-.975-.382-2.603-3.168.512-6.771
 4.01-7.534 5.87-.003.007-.003.015-.005.022a6.7 6.7 0 0 0-.534 1.161Z"
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
