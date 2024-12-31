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


class CephIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ceph"

    @property
    def original_file_name(self) -> "str":
        return "ceph.svg"

    @property
    def title(self) -> "str":
        return "Ceph"

    @property
    def primary_color(self) -> "str":
        return "#EF5C55"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ceph</title>
     <path d="M11.959.257A11.912 11.912 0 003.503 3.76 11.92 11.92 0
 000 12.217a11.934 11.934 0 001.207 5.243c.72 1.474 1.888 2.944 3.208
 4.044.86-.47 1.35-.99 1.453-1.545.1-.533-.134-1.107-.737-1.805a9.031
 9.031 0 01-2.219-5.937c0-4.988 4.058-9.047 9.047-9.047h.08c4.99 0
 9.048 4.059 9.048 9.047a9.03 9.03 0 01-2.218 5.936c-.599.693-.84
 1.292-.735 1.83.108.556.595 1.068 1.449 1.522 1.322-1.1 2.489-2.57
 3.209-4.046A11.898 11.898 0 0024 12.217a11.929 11.929 0
 00-3.503-8.457A11.923 11.923 0 0012.04.257h-.041zm-.005 4.837a7.072
 7.072 0 00-3.76 1.075A7.202 7.202 0 006.15 8.093a7.164 7.164 0
 00-1.161 2.65 7.188 7.188 0 00.04 3.125 7.14 7.14 0 001.22
 2.607c.154.207.326.396.509.597l.185.202.005.006c.007.007.017.016.026.027.635.738.957
 1.533.957 2.36a3.4 3.4 0 01-1.788 2.989 11.924 11.924 0 002.685
 1.087c.14-.088.614-.441 1.077-1.083a4.899 4.899 0 00.94-2.99 6.595
 6.595 0 00-.49-2.37 6.717 6.717 0
 00-1.302-2.033l-.002-.004-.124-.142c-.21-.245-.428-.497-.602-.792a4.104
 4.104 0 01-.462-1.135 4.258 4.258 0 01-.024-1.85 4.25 4.25 0
 01.686-1.564 4.216 4.216 0 013.432-1.773H12.042a4.202 4.202 0 013.432
 1.773c.33.466.568 1.007.686 1.565a4.27 4.27 0 01-.023
 1.849c-.093.39-.249.772-.463
 1.135-.173.295-.391.547-.602.792l-.123.142-.004.004a6.736 6.736 0
 00-1.301 2.033 6.607 6.607 0 00-.49 2.37 4.897 4.897 0 00.94
 2.99c.463.642.937.995 1.076 1.083a11.776 11.776 0 002.687-1.087 3.399
 3.399 0
 01-1.789-2.988c0-.817.313-1.59.956-2.359.009-.012.02-.022.027-.03l.006-.004.184-.204c.183-.2.355-.39.51-.596a7.14
 7.14 0 001.22-2.608 7.21 7.21 0 00.04-3.124 7.185 7.185 0
 00-1.16-2.65 7.203 7.203 0 00-2.044-1.924 7.074 7.074 0
 00-3.762-1.075h-.09zM12 9.97a2.365 2.365 0 00-2.362 2.361A2.364 2.364
 0 0012 14.691c1.301 0 2.36-1.059 2.36-2.36A2.364 2.364 0 0012 9.968z"
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
        return '''https://github.com/ceph/ceph/blob/b106a03dcdd
aee80493825e85bc5e399ab4d8746/src/pybind/mgr/dashboard/frontend/src/as'''

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
