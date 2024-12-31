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


class FlywayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flyway"

    @property
    def original_file_name(self) -> "str":
        return "flyway.svg"

    @property
    def title(self) -> "str":
        return "Flyway"

    @property
    def primary_color(self) -> "str":
        return "#CC0200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flyway</title>
     <path d="m3.02 21.055 1.12-.23c1.054-.219 2.114-.415
 3.161-.66a4.955 4.952 0 0 0 3.696-3.915 6.06 6.057 0 0 0
 .085-1.153l.366-.09a4.936 4.933 0 0 0 3.75-3.717 3.8 3.798 0 0 0
 .128-1.06c-.002-.096 0-.193 0-.305.094-.023.18-.047.267-.067a4.552
 4.549 0 0 0 2.68-1.755 5.772 5.769 0 0 0
 1.005-4.854c-.021-.088-.035-.179-.061-.264a.63.629 0 0
 0-.728-.432l-3.184.652-3.485.716-4.002.822q-2.186.449-4.373.893a1.125
 1.125 0 0
 1-.422.06c-.007-.074-.017-.14-.017-.204-.001-1.12.002-2.243-.005-3.364a.324.324
 0 0 1 .174-.307 8.493 8.488 0 0 1 1.9-.86A17.205 17.194 0 0 1
 7.827.315C8.373.23 8.922.181 9.47.12a26.795 26.777 0 0 1
 3.526-.102c.496.01.992.051 1.487.097.542.051 1.085.11
 1.623.192a14.482 14.472 0 0 1 4.007
 1.124c.262.123.509.28.764.422a.215.215 0 0 1 .122.223c-.004.054 0 .11
 0 .163v19.519c0 .347.045.28-.262.472a8.437 8.432 0 0 1-1.961.857
 16.78 16.769 0 0
 1-2.851.63c-.6.08-1.2.146-1.804.207-.277.03-.556.035-.835.043-.564.015-1.128.041-1.691.03-.636-.014-1.272-.059-1.907-.099a20.054
 20.041 0 0 1-2.519-.332 13.423 13.415 0 0
 1-3.224-.976c-.273-.13-.53-.29-.797-.435a.246.246 0 0
 1-.144-.248c.008-.23 0-.46.003-.69
 0-.049.01-.096.016-.163zm9.985-10.652a1.248 1.248 0 0 1-.09.55 2.624
 2.622 0 0 1-2.045 1.84c-1.3.28-2.607.537-3.912.805l-.57.114a1.147
 1.146 0 1 0 .403 2.256c.595-.11 1.186-.242
 1.779-.363.064-.014.128-.022.209-.035a2.584 2.582 0 0 1-.55
 1.41A2.801 2.8 0 0 1 6.516
 18c-1.103.223-2.206.45-3.308.676-.052.01-.106.013-.156.02-.048-.146-.061-10.38-.014-10.63l14.048-2.883a1.523
 1.522 0 0 1-.016.18 3.438 3.436 0 0 1-.738 1.502 2.399 2.397 0 0
 1-1.426.804c-1.11.216-2.218.45-3.326.677l-.96.196a1.168 1.168 0 0
 0-.953 1.057 1.147 1.147 0 0 0 .875 1.186 1.747 1.746 0 0 0
 .807-.054c.492-.1.983-.203 1.475-.304.053-.01.108-.014.18-.023z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/flyway/flywaydb.org/blob/8'''

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
