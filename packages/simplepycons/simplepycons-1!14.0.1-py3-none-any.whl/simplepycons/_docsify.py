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


class DocsifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "docsify"

    @property
    def original_file_name(self) -> "str":
        return "docsify.svg"

    @property
    def title(self) -> "str":
        return "Docsify"

    @property
    def primary_color(self) -> "str":
        return "#2ECE53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Docsify</title>
     <path d="M12 2.862c-6.617 0-12 5.383-12 12 0 1.964.49 3.406 1.5
 4.408 1.706 1.696 4.619 1.868 8.05 1.868.43 0 .87-.002
 1.315-.005a217.6 217.6 0 0 1 2.765 0c3.792.024 7.066.044
 8.88-1.758C23.511 18.378 24 16.9 24
 14.862c0-6.617-5.383-12-12-12zm-8.852 8.154a.393.393 0 1 1
 0-.787.393.393 0 0 1 0 .787zM5.113 8.48c-.55.637-1.01 1.361-1.01
 1.361-.06.092-.167.099-.24.017l-.26-.29a.251.251 0 0
 1-.02-.303s1.11-1.559 1.806-2.186c.25-.225.248-.239.891-.692.643-.453
 1.4-.826 1.4-.826a.272.272 0 0 1
 .308.059l.26.29c.075.082.056.186-.04.235 0 0-1.772.887-2.353
 1.509-.394.422-.192.19-.742.826zm1.576 2.143a1.377 1.377 0 1 1 2.754
 0 1.377 1.377 0 0 1-2.754 0zm5.41 7.929c-1.902
 0-3.443-1.542-3.443-3.443s1.644-.854 3.545-.854 3.34-1.047
 3.34.854-1.541 3.443-3.443 3.443zM16.72 12a1.377 1.377 0 1 1 0-2.754
 1.377 1.377 0 0 1 0 2.754z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/docsifyjs/docsify/blob/d01'''

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
