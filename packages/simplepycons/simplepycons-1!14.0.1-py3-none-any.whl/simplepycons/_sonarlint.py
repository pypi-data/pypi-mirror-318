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


class SonarlintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonarlint"

    @property
    def original_file_name(self) -> "str":
        return "sonarlint.svg"

    @property
    def title(self) -> "str":
        return "SonarLint"

    @property
    def primary_color(self) -> "str":
        return "#CB2029"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SonarLint</title>
     <path d="M12 0C5.412 0 0 5.342 0 12c0 6.66 5.411 12 12 12 6.59 0
 12-5.41 12-12 0-6.658-5.41-12-12-12zm0 2.22A9.77 9.77 0 0 1 21.78 12
 9.768 9.768 0 0 1 12 21.78 9.77 9.77 0 0 1 2.22 12 9.771 9.771 0 0 1
 12 2.22zM5.203 9.988c-.763 0-1.179.763-1.456 1.387 0
 0-.208.555-.347.763-.07.277-.486 1.18-.14
 1.665.209.277.486-.139.694-.347.139-.208.418-.833.418-.833.346-.555.485-.832.831-.832.347
 0 .555.278.832.902.347.625.695 1.388 1.458 1.388s1.179-.763
 1.456-1.388c.278-.555.485-.902.832-.902s.556.278.833.902c.347.625.694
 1.388 1.457 1.388.763 0 1.179-.763
 1.456-1.388.278-.555.485-.902.832-.902s.556.278.833.902c.347.625.694
 1.388 1.457 1.388.763 0 1.179-.763
 1.456-1.388.277-.555.486-.902.833-.902s.555.278.832.902c0 0
 .139.277.347.624.07.138.416.693.693.693.278 0
 .347-.832.07-1.525-.278-.625-.485-1.11-.485-1.11-.347-.624-.694-1.387-1.457-1.387-.763
 0-1.18.763-1.458 1.387-.277.555-.485.901-.831.901-.347
 0-.555-.277-.832-.9-.347-.625-.695-1.388-1.458-1.388s-1.179.763-1.456
 1.387c-.278.555-.485.901-.832.901s-.556-.277-.833-.9c-.347-.625-.694-1.388-1.457-1.388-.763
 0-1.179.763-1.456
 1.387-.278.555-.485.901-.832.901s-.556-.277-.833-.9c-.347-.625-.694-1.388-1.457-1.388z"
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
