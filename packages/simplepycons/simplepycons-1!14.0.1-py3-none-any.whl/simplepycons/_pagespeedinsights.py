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


class PagespeedInsightsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pagespeedinsights"

    @property
    def original_file_name(self) -> "str":
        return "pagespeedinsights.svg"

    @property
    def title(self) -> "str":
        return "PageSpeed Insights"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PageSpeed Insights</title>
     <path d="M22.363 1.636H1.635C.732 1.636 0 2.37.001 3.273L0
 20.727v.003c0 .903.733 1.634 1.635 1.634h20.73c.904 0 1.635-.734
 1.635-1.637V3.273c.016-.89-.76-1.64-1.637-1.637zM3.979
 2.886c.492-.507 1.279.28.77.772-.491.508-1.278-.279-.77-.771zM1.8
 2.89c.507-.509 1.28.265.772.771-.493.502-1.274-.28-.772-.771zm21.7
 17.838c.012.611-.524 1.148-1.137 1.136H1.635A1.137 1.137 0 0 1 .5
 20.727L.501 4.91H23.5v15.819zM11
 16.159l5.946-4.577c.235-.2.576.129.389.372l-.002-.002-3.936
 6.35a1.638 1.638 0 0
 1-2.448.405c-.785-.668-.811-1.835.05-2.548zm4.763-.75c.09-.168
 2.002-3.181 2.06-3.35 2.056 1.813 3.029 4.382 2.898
 7.026h-3.819c.073-1.39-.29-2.678-1.139-3.676zm-8.679
 3.682H3.278c-.357-7.022 7.148-11.735 13.39-7.92l-3.461
 2.618c-3.3-.762-6.364 1.71-6.123 5.302z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/web/fundamental'''

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
