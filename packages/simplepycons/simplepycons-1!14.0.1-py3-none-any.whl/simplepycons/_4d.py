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


class FourDIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "4d"

    @property
    def original_file_name(self) -> "str":
        return "4d.svg"

    @property
    def title(self) -> "str":
        return "4D"

    @property
    def primary_color(self) -> "str":
        return "#004088"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>4D</title>
     <path d="M20.64 0v24H3.36V0h17.28zM10.49 11.827c-.115.138-5.882
 6.789-5.983 6.9-.058.07-.187.194-.187.36 0
 .153.187.208.36.208h4.4v-1.067H5.83c.49-.61 3.38-3.824
 3.696-4.226v5.34c0 .194-.005.965-.043
 1.602-.029.43-.13.637-.661.693-.23.027-.533.041-.662.041-.072
 0-.115.083-.115.18 0 .097.072.167.23.167.777 0 1.539-.042 1.942-.042
 1.236 0 2.646.097 3.178.097 2.618 0 4.099-.97 4.746-1.607.791-.776
 1.539-2.093 1.539-3.81
 0-1.622-.662-2.758-1.38-3.465-1.54-1.565-3.913-1.565-5.682-1.565-.56
 0-1.035.027-1.064.027-.388.042-.345-.124-.59-.138-.158-.014-.258.055-.474.305zm1.898.443c1.108
 0 2.719.166 4.027 1.372.604.554 1.367 1.676 1.367 3.408 0 1.414-.288
 2.66-1.194 3.409-.849.706-1.812.984-3.265.984-1.122
 0-1.683-.291-1.87-.54-.115-.153-.172-.694-.186-1.04
 0-.097-.015-.29-.015-.568h1.021c.245 0
 .317-.055.389-.18.1-.18.244-.735.244-.86
 0-.11-.057-.166-.13-.166-.086
 0-.273.139-.647.139h-.877v-5.584c0-.152.058-.222.173-.277.115-.056.676-.097.963-.097z"
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
