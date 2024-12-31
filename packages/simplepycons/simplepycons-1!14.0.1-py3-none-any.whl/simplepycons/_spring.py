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


class SpringIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spring"

    @property
    def original_file_name(self) -> "str":
        return "spring.svg"

    @property
    def title(self) -> "str":
        return "Spring"

    @property
    def primary_color(self) -> "str":
        return "#6DB33F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spring</title>
     <path d="M21.8537 1.4158a10.4504 10.4504 0 0 1-1.284
 2.2471A11.9666 11.9666 0 1 0 3.8518 20.7757l.4445.3951a11.9543
 11.9543 0 0 0
 19.6316-8.2971c.3457-3.0126-.568-6.8649-2.0743-11.458zM5.5805
 20.8745a1.0174 1.0174 0 1 1-.1482-1.4323 1.0396 1.0396 0 0 1 .1482
 1.4323zm16.1991-3.5806c-2.9385 3.9263-9.2601 2.5928-13.2852 2.7904 0
 0-.7161.0494-1.4323.1481 0 0 .2717-.1234.6174-.2469 2.8398-.9877
 4.1732-1.1853 5.9018-2.0743 3.2349-1.6545 6.4698-5.2844
 7.1118-9.0379-1.2347 3.6053-4.9881 6.7167-8.3959
 7.9761-2.3459.8643-6.5685 1.7039-6.5685
 1.7039l-.1729-.0988c-2.8645-1.4076-2.9632-7.6304 2.2718-9.6306
 2.2966-.889 4.4696-.395 6.9637-.9877 2.6422-.6174 5.7043-2.5929
 6.939-5.1857 1.3828 4.1732 3.062 10.643.0493 14.6434z" />
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
