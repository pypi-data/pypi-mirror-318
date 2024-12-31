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


class AlienwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alienware"

    @property
    def original_file_name(self) -> "str":
        return "alienware.svg"

    @property
    def title(self) -> "str":
        return "Alienware"

    @property
    def primary_color(self) -> "str":
        return "#541BAE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alienware</title>
     <path d="M20.382
 9.4054c-.0649-.6486-.1297-1.3622-.2595-2.0108-.1297-.6487-.2594-1.2973-.5189-1.946-.1297-.3243-.2595-.6486-.3892-.908-.1297-.3244-.3243-.5838-.454-.9082-.1946-.2594-.3892-.5838-.5838-.8432-.1946-.2595-.454-.519-.7135-.7135-.454-.3892-.973-.7784-1.5568-1.1027-.5838-.3244-1.2324-.5838-1.881-.7135C13.3765.0649
 12.7278 0 12.0143 0c-.7135 0-1.3621.0649-2.0108.2595C9.355.3892
 8.7712.6486 8.1874.973c-.6487.3243-1.1676.7135-1.6865
 1.1675-.2595.1946-.454.454-.7135.7136l-.5838.7783c-.1297.3244-.3243.5838-.454.9081l-.3892.973c-.1946.6487-.3892
 1.2973-.519 1.946-.1297.6486-.1946 1.2973-.2594 2.0108-.0649.7135 0
 1.2973 0 1.946 0 .6486.0648 1.2972.1946
 2.0107l.1946.973c.0648.3243.1946.6486.3243.973.454 1.2324 1.1676 2.4
 1.881 3.5027.3893.5838.7785 1.1027 1.1676 1.6216.3892.519.7784 1.1027
 1.2325
 1.5568.1946.2594.454.454.7135.7135.2594.1946.519.3892.8432.5837.2595.1946.5838.3244.9081.4541.1298.0649.3244.1297.4541.1297.1946
 0 .3243.0649.519.0649.1945 0 .3242 0 .5188-.0649.1946 0
 .3244-.0648.454-.1297.3244-.1297.6487-.2595.9082-.454.2595-.1946.5838-.3892.8432-.5838.2595-.1946.519-.454.7136-.7135.454-.519.8432-1.0379
 1.2324-1.5568.3892-.519.7784-1.1027 1.1676-1.6216.7135-1.1027
 1.427-2.2703
 1.881-3.5027.1298-.3244.2595-.6487.3244-.973.0648-.3243.1946-.6486.1946-.973.1297-.6486.1945-1.2973.1945-2.0108
 0-.6486 0-1.3621-.0648-2.0108zM4.8144 12.0649s3.6973.8432 6.0973
 5.8378c-.0649 0-6.4216-.1297-6.0973-5.8378zm8.3676
 5.8378c2.3351-4.9946 6.0973-5.8378 6.0973-5.8378.3243 5.708-6.0973
 5.8378-6.0973 5.8378z" />
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
