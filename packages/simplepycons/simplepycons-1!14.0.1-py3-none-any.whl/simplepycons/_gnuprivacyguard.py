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


class GnuPrivacyGuardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gnuprivacyguard"

    @property
    def original_file_name(self) -> "str":
        return "gnuprivacyguard.svg"

    @property
    def title(self) -> "str":
        return "GNU Privacy Guard"

    @property
    def primary_color(self) -> "str":
        return "#0093DD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GNU Privacy Guard</title>
     <path d="M2.968 11.583h1.274v-3.82A7.76 7.76 0 0 1 12.005 0a7.76
 7.76 0 0 1 7.762
 7.763v3.783c-.018.01-.037.028-.056.037l-.01.01-.008.009h-.01l-.01.01-.009.009H19.636l-.018.018h-.02l-.018.01h-.01l-.009.01-.009.009h-.01l-.009.009-.009.01-.01.009-.009.009-.028.019-.019.01-.028.018-.018.01-.02.009-.027.018-.019.01-.01.009-.027.019-.02.01-.046.027-.019.01-.018.009-.02.01h-.008l-.057.027h-.019c-.018.01-.037.02-.065.038h-.01l-.009.01-.028.018-.018.01-.029.018-.018.01h-.01l-.028.018-.018.01-.02.009c-.018.01-.046.019-.065.028l-.018.01-.02.009-.037.018-.037.02-.047.018-.047.019-.019.009-.037.019-.019.01c-1.545.739-4.017
 1.516-8.708 1.853-3.362.244-5.403 1.723-6.724 3.502zm4.842
 0h8.371v-3.82a4.184 4.184 0 0 0-4.186-4.186A4.184 4.184 0 0 0 7.81
 7.763zm13.222 1.461V24H5.572c1.704-.946 2.968-.852 5.075-.787
 2.865.094 6.03-1.105 7.585-2.696
 1.554-1.592-.14-.375-1.901.074-1.76.45-5.17.497-7.454-.103 7.173.094
 9.973-2.219 11.555-4.307
 1.583-2.079-.683-.365-2.153.356-1.47.72-4.036 1.227-6.864.852
 4.27-.01 7.52-2.144 9.607-4.345z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gn'''

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
