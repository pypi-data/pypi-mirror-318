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


class WebexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webex"

    @property
    def original_file_name(self) -> "str":
        return "webex.svg"

    @property
    def title(self) -> "str":
        return "Webex"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Webex</title>
     <path d="M21.78 7.376c.512 1.181.032 2.644-1.11
 3.106-2.157.888-3-1.295-3-1.295-.236-.55-.727-1.496-1.335-1.496-.204
 0-.503 0-.94.844-.229.443-.434 1.185-.616
 1.84l-.09.32c-.373-1.587-.821-3.454-1.536-4.816-.195-.38-.42-.74-.673-1.08a5.135
 5.135 0 0 1 1.743-1.337 4.891 4.891 0 0 1 2.112-.463c1.045 0
 2.765.338 4.227 2.227.167.206.317.424.448.654.278.441.52.904.726
 1.383l.043.113zM.02 8.4C-.15 7.105.8 5.845 1.953 5.755c1.794-.157
 2.36 1.385 2.455 1.89l.022.137c.07.44.29 1.838.48 2.744.078.4.244
 1.013.353 1.416l.006.022.026.092c.11.4.232.799.362 1.193.185.548.399
 1.085.641 1.61.47.955.93 1.45 1.367 1.45.203 0 .512 0
 .96-.878.283-.59.512-1.208.684-1.845.373 1.598.811 3.128 1.495
 4.456.205.406.444.794.715 1.16a5.124 5.124 0 0 1-1.742 1.338 4.88
 4.88 0 0 1-2.112.461c-1.548 0-3.727-.698-5.339-4.005a22.407 22.407 0
 0 1-1.078-2.824 26.848 26.848 0 0 1-.693-2.656 48.56 48.56 0 0
 1-.215-1.114C.191 9.603.074 8.872.02
 8.4zm22.047-2.645-.202-.022h-.052c.222.392.421.797.597
 1.215l.053.113c.322.76.346 1.614.068 2.391a3.079 3.079 0 0 1-1.552
 1.749 2.93 2.93 0 0 1-1.228.28 3.115 3.115 0 0 1-.854-.135c-.299
 1.182-.768 2.634-1.195 3.511-.427.877-.93 1.451-1.378 1.451-.192
 0-.501 0-.95-.877a10.746 10.746 0 0 1-.683-1.845 38.722 38.722 0 0
 1-.396-1.575 12.67 12.67 0 0
 1-.136-.598l-.002-.01c-.406-1.778-.865-3.645-1.655-5.142A8.263 8.263
 0 0 0 11.52 4.8a5.136 5.136 0 0 0-1.748-1.34A4.892 4.892 0 0 0 7.654
 3c-1.036 0-2.754.338-4.217 2.228.466.223.867.562
 1.164.984.305.433.499.933.565 1.458.076.563.256 1.654.47
 2.688l.001.007c.021.11.042.221.073.342.126-.34.25-.642.38-.955l.112-.271.128-.293c.235-.55.726-1.496
 1.324-1.496.213 0 .513 0 .95.844.296.606.532 1.239.706
 1.89.138.507.276 1.047.394 1.587.04.148.07.296.101.444l.006.028c.427
 1.879.875 3.69 1.644 5.187.159.317.34.622.545.911.15.215.31.422.48.62
 1.27 1.45 2.733 1.8 3.843 1.8 1.548 0 3.738-.698 5.35-4.006.822-1.7
 1.515-4.208
 1.772-5.48.256-1.27.449-2.419.534-3.115.04-.307.023-.618-.051-.918-.075-.299-.205-.579-.382-.825a2.247
 2.247 0 0 0-.653-.607 2.143 2.143 0 0 0-.826-.296z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://resources.webex.com/webex/brand-excha'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/momentum-design/momentum-u
i/blob/970c5bec962a3f72e17e0b7ed69f2c38d298c405/icons-rebrand/svg/webe'''

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
