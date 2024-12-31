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


class BitriseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitrise"

    @property
    def original_file_name(self) -> "str":
        return "bitrise.svg"

    @property
    def title(self) -> "str":
        return "Bitrise"

    @property
    def primary_color(self) -> "str":
        return "#683D87"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitrise</title>
     <path d="M23.5154
 13.4558c-.2744-1.8854-.692-3.7828-.9904-5.0477-.358-1.5035-1.6349-2.5775-3.1742-2.673-1.5155-.0955-4.0215-.2028-7.3627-.2028-3.3413
 0-5.8472.1074-7.3627.2028-1.5394.0955-2.8163 1.1695-3.1743
 2.673-.2983 1.265-.716 3.1623-.9904 5.0477-.191 1.2769-.3341
 2.7685-.4535 4.463-.0596.9427.2506 1.8496.8831 2.5537.6324.704 1.4916
 1.1217 2.4463 1.1575 2.0763.0955 5.2625.2148 8.6634.2148 3.401 0
 6.587-.1193 8.6634-.2148.9427-.0477 1.8139-.4535
 2.4463-1.1575.6325-.704.9427-1.611.883-2.5537-.1312-1.6945-.2863-3.198-.4773-4.463zm-1.6467
 5.9188c-.3342.37-.7876.5848-1.2888.6086-2.0644.0955-5.2148.2148-8.5918.2148-3.3771
 0-6.5274-.1193-8.5919-.2148-.5011-.0239-.9546-.2386-1.2887-.6086-.3342-.3699-.5012-.8472-.4654-1.3484.1074-1.6468.2506-3.1026.4415-4.3317.2625-1.8258.6683-3.6754.9666-4.9045.191-.7995.8592-1.3604
 1.6826-1.42C6.2244 7.2745 8.6945 7.167 12 7.167c3.2935 0 5.7756.1074
 7.2673.2029.8114.0477 1.4916.6205 1.6825 1.42.2864 1.2291.6921
 3.0787.9666 4.9045.179 1.2291.3222 2.685.4415 4.3317 0
 .5012-.167.9785-.4892 1.3484zM11.988 4.1958c.5608 0 1.0262-.4535
 1.0262-1.0143 0-.561-.4534-1.0263-1.0262-1.0263-.5609
 0-1.0263.4535-1.0263 1.0263 0 .5489.4654 1.0143 1.0263 1.0143zm5.9665
 7.84c-.9069 0-1.6468.7399-1.6468
 1.6468h3.2936c0-.907-.728-1.6468-1.6468-1.6468zm-11.933 0c-.907
 0-1.6468.7399-1.6468
 1.6468h3.2935c0-.907-.728-1.6468-1.6468-1.6468zm5.9665 5.9665c1.4677
 0 2.661-1.1933 2.661-2.661h-5.334c0 1.4558 1.1933 2.661 2.673 2.661z"
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
