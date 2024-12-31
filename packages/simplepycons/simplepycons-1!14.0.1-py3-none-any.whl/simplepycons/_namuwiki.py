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


class NamuWikiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "namuwiki"

    @property
    def original_file_name(self) -> "str":
        return "namuwiki.svg"

    @property
    def title(self) -> "str":
        return "Namu Wiki"

    @property
    def primary_color(self) -> "str":
        return "#008275"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Namu Wiki</title>
     <path d="M12 0C5.3724 0 0 5.372 0 12c0 6.6278 5.3723 12 12 12
 6.6278 0 12-5.3722 12-12 0-6.628-5.3722-12-12-12zM6.4902
 5.9219c1.1467-.0082 2.0869.918 2.0957 2.0644.005.6836-.324
 1.2912-.832 1.6739l1.7871 4.2207
 2.959-1.252-.3848-.9082c-.0923.013-.1852.0228-.2812.0234-1.1466.0088-2.0868-.9182-2.0957-2.0644-.0087-1.1472.9177-2.085
 2.0644-2.0938 1.1466-.0081 2.087.9168 2.0957 2.0625.0048.655-.2955
 1.2423-.7675 1.627l1.125 2.6562 3.5293-1.496a2.0834 2.0834 0 0
 1-.045-.4122c-.0085-1.147.9178-2.0868 2.0645-2.0957 1.1465-.0088
 2.0851.9163 2.0937 2.0625.0085 1.1473-.9162 2.0879-2.0625
 2.0957-.6053.0044-1.1519-.2535-1.5351-.664l-3.6133 1.5293.496
 1.1738a.5542.5542 0 0 1-.2929.7266.5546.5546 0 0
 1-.7265-.295l-1.2305-2.9082-4.8828
 2.0664c.0112.0845.0189.1702.0195.2559.0085 1.147-.9178 2.0863-2.0644
 2.0957-1.146.0081-2.0875-.9174-2.0957-2.0644-.0088-1.1465.9176-2.0861
 2.0644-2.0957.6647-.005 1.258.3045
 1.6426.789l.9043-.3828-1.7969-4.2441a1.9538 1.9538 0 0
 1-.2012.0117c-1.1467.0092-2.087-.916-2.0957-2.0625-.0087-1.1462.9159-2.087
 2.0625-2.0957zM6.5
 7.1406c-.4749.0036-.8573.3933-.8535.8672.0035.475.3925.8572.8672.8535.474-.0031.8573-.3927.8535-.8672-.0037-.4745-.393-.8574-.8672-.8535zm5.3125
 1.6621c-.4749.0043-.859.3928-.8555.8672.0033.4745.3932.8571.8672.8535.4749-.0034.859-.3908.8555-.8652-.0035-.4739-.393-.8585-.8672-.8555zm7.957
 2.3438c-.4537.0267-.8137.4075-.8105.8672.0034.4743.3924.8565.8672.8535.474-.0036.8565-.3922.8535-.8672-.0044-.474-.393-.8567-.8672-.8535-.0148.0001-.0283-.0009-.043
 0zM5.9844 15.125c-.4749.0049-.8576.393-.8535.8672a.8613.8613 0 0 0
 .8652.8555c.4739-.0036.8568-.3935.8535-.8672-.0036-.474-.3911-.8586-.8652-.8555z"
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
        return '''https://namu.wiki/w/%ED%8C%8C%EC%9D%BC:%EB%82'''

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
