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


class ThreadsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "threads"

    @property
    def original_file_name(self) -> "str":
        return "threads.svg"

    @property
    def title(self) -> "str":
        return "Threads"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Threads</title>
     <path d="M12.186
 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44 1.5 15.586
 1.472 12.01v-.017c.03-3.579.879-6.43 2.525-8.482C5.845 1.205 8.6.024
 12.18 0h.014c2.746.02 5.043.725 6.826 2.098 1.677 1.29 2.858 3.13
 3.509
 5.467l-2.04.569c-1.104-3.96-3.898-5.984-8.304-6.015-2.91.022-5.11.936-6.54
 2.717C4.307 6.504 3.616 8.914 3.589 12c.027 3.086.718 5.496 2.057
 7.164 1.43 1.783 3.631 2.698 6.54 2.717 2.623-.02 4.358-.631
 5.8-2.045 1.647-1.613 1.618-3.593
 1.09-4.798-.31-.71-.873-1.3-1.634-1.75-.192 1.352-.622 2.446-1.284
 3.272-.886 1.102-2.14 1.704-3.73
 1.79-1.202.065-2.361-.218-3.259-.801-1.063-.689-1.685-1.74-1.752-2.964-.065-1.19.408-2.285
 1.33-3.082.88-.76 2.119-1.207 3.583-1.291a13.853 13.853 0 0 1
 3.02.142c-.126-.742-.375-1.332-.75-1.757-.513-.586-1.308-.883-2.359-.89h-.029c-.844
 0-1.992.232-2.721 1.32L7.734 7.847c.98-1.454 2.568-2.256
 4.478-2.256h.044c3.194.02 5.097 1.975 5.287
 5.388.108.046.216.094.321.142 1.49.7 2.58 1.761 3.154 3.07.797
 1.82.871 4.79-1.548 7.158-1.85 1.81-4.094 2.628-7.277
 2.65Zm1.003-11.69c-.242 0-.487.007-.739.021-1.836.103-2.98.946-2.916
 2.143.067 1.256 1.452 1.839 2.784 1.767 1.224-.065 2.818-.543
 3.086-3.71a10.5 10.5 0 0 0-2.215-.221z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://about.meta.com/brand/resources/instag'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://about.meta.com/brand/resources/instag'''

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
