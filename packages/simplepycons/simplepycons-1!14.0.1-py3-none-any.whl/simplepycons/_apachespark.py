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


class ApacheSparkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachespark"

    @property
    def original_file_name(self) -> "str":
        return "apachespark.svg"

    @property
    def title(self) -> "str":
        return "Apache Spark"

    @property
    def primary_color(self) -> "str":
        return "#E25A1C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Spark</title>
     <path d="M10.812 0c-.425.013-.845.215-1.196.605a3.593 3.593 0
 00-.493.722c-.355.667-.425 1.415-.556 2.143a551.9 551.9 0 00-.726
 4.087c-.027.16-.096.227-.244.273C5.83 8.386 4.06 8.94 2.3
 9.514c-.387.125-.773.289-1.114.506-1.042.665-1.196 1.753-.415
 2.71.346.422.79.715 1.284.936 1.1.49 2.202.976 3.3
 1.47.019.01.036.013.053.019h-.004l1.306.535c0 .023.002.045 0 .073-.2
 2.03-.39 4.063-.58 6.095-.04.419-.012.831.134 1.23.317.87 1.065 1.148
 1.881.701.372-.204.666-.497.937-.818 1.372-1.623 2.746-3.244
 4.113-4.872.111-.133.205-.15.363-.098.349.117.697.231
 1.045.347h.001c.02.012.045.02.073.03l.142.042c1.248.416 2.68.775
 3.929 1.19.4.132.622.164
 1.045.098.311-.048.592-.062.828-.236.602-.33.995-.957.988-1.682-.005-.427-.154-.813-.35-1.186-.82-1.556-1.637-3.113-2.461-4.666-.078-.148-.076-.243.037-.375
 1.381-1.615 2.756-3.236
 4.133-4.855.272-.32.513-.658.653-1.058.308-.878-.09-1.57-1-1.741a2.783
 2.783 0 00-1.235.069c-1.974.521-3.947 1.041-5.918
 1.57-.175.047-.26.015-.355-.144a353.08 353.08 0 00-2.421-4.018 4.61
 4.61 0 00-.652-.849c-.371-.37-.802-.549-1.227-.536zm.172
 3.703a.592.592 0 01.189.211c.87 1.446 1.742 2.89 2.609
 4.338.07.118.135.16.277.121 1.525-.41 3.052-.813
 4.579-1.217.367-.098.735-.193 1.103-.289a.399.399 0 01-.1.2c-1.259
 1.48-2.516 2.962-3.779 4.438-.11.13-.12.22-.04.37.937 1.803 1.768
 3.309 2.498
 4.76l-3.696-1.019c-.538-.18-1.077-.358-1.615-.539-.163-.055-.25-.03-.36.1-1.248
 1.488-2.504 2.97-3.759 4.454a.398.398 0
 01-.18.132c.035-.378.068-.757.104-1.136.149-1.572.297-3.144.451-4.716-.03-.318.117-.405-.322-.545-1.493-.593-3.346-1.321-4.816-1.905a.595.595
 0 01.24-.134c1.797-.57 3.595-1.14
 5.394-1.705.127-.04.199-.092.211-.233.013-.148.05-.294.076-.441.241-1.363.483-2.726.726-4.088.068-.386.14-.771.21-1.157z"
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
