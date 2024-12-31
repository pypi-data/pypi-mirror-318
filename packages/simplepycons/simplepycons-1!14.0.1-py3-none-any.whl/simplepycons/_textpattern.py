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


class TextpatternIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "textpattern"

    @property
    def original_file_name(self) -> "str":
        return "textpattern.svg"

    @property
    def title(self) -> "str":
        return "Textpattern"

    @property
    def primary_color(self) -> "str":
        return "#FFDA44"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Textpattern</title>
     <path d="m3.638
 10.8h-.559s-.918-.776-1.872-1.692-1.207-1.387-1.207-1.387v-.559l7.162-7.162h.559s.744.61
 1.631 1.448 1.448 1.63 1.448 1.63v.559l-2.193 2.193 4.397
 4.117s2.431-2.431 3.272-3.271 1.736-2.719
 1.736-2.719l2.346-2.346.61-.413 3.032 3.033-.414.611-2.344
 2.344s-1.606.684-2.718 1.737-3.34 3.34-3.34 3.34 1.933 2.146 4.057
 4.27c2.146 2.146 4.484 4.271 4.651 4.426.334.309-.347 1.373-.906
 2.027s-.857.697-1.247.901c-.39.205-.836-.051-.836-.051s-2.056-2.261-4.082-4.304c-1.975-1.991-4.559-4.349-4.559-4.349s-6.646
 6.645-7.079 7.078c-.433.434-.597 1.089-.597
 1.089l-.649.65s-.701-.396-1.553-1.255-1.182-1.487-1.182-1.487l.646-.646s.598-.084
 1.088-.597 7.01-7.009 7.01-7.009l-4.119-4.398zm17.267
 13.04c-.02-.019-.034-.033 0 0zm-3.456-15.084.453-.453c.86-.86
 3.194-1.392 3.194-1.392l2.26-2.26.258-.381-2.682-2.682-.381.258-2.261
 2.261s-.942 1.925-1.802 2.784l-.423.423-.03.03-12.887
 12.887c-.491.492-1.147.655-1.147.655l-.409.41s.551.787 1.004
 1.24c.453.454.765.647.765.647l.462-.475s.246-.573.737-1.065zm-4.656
 1.406-3.798-3.577s-.626.197-1.088.815-.488 1.125-.066 1.547c.423.422
 3.085 3.082 3.085 3.082zm2.642 2.818s-.714.181-1.097.746-.359.927.052
 1.339c.412.412 2.378 2.199 3.888 3.718s3.746 3.864 4.004
 4.04c.26.177.26.177.26.177s.389-.303.668-.702.627-.981.462-1.132c-.166-.152-1.828-1.669-4.027-3.81s-4.21-4.376-4.21-4.376zm-15.136-5.693v.339s.369.523
 1.36 1.514 1.514 1.36 1.514
 1.36h.339l-.091-.257s-.766-.399-1.615-1.249c-.85-.85-1.25-1.616-1.25-1.616s2.058-2.009
 3.442-3.393c1.385-1.385 3.379-3.428 3.379-3.428s.737.429 1.587 1.279
 1.279 1.586 1.279
 1.586l.257.091v-.339s-.369-.523-1.36-1.514-1.514-1.36-1.514-1.36h-.339z"
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
