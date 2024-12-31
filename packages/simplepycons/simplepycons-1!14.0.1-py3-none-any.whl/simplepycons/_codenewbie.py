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


class CodenewbieIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codenewbie"

    @property
    def original_file_name(self) -> "str":
        return "codenewbie.svg"

    @property
    def title(self) -> "str":
        return "CodeNewbie"

    @property
    def primary_color(self) -> "str":
        return "#9013FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeNewbie</title>
     <path d="M12.071 0A12.023 12.023 0 0 0 2.31 5.011c-2.913
 4.075-2.879 9.774.068
 13.821.094.13.196.254.292.367.27.306.543.59.782.82.18.165.386.345.615.517.416.337.866.63
 1.343.873-.429-.2-.834-.401-1.177-.58-.075-.036-.139-.077-.207-.112-.22-.11-.422-.228-.616-.339a5.47
 5.47 0 0 1-.747-.527c-.153 1.044-.754 1.895-1.792 2-.975.096-.954
 1.383 0 1.5 2.647.33 5.45.648 8.22.648 1.68.014 3.359-.128
 5.013-.426.38-.098.758-.182 1.079-.27 5.512-1.53 9.055-6.856
 8.64-12.487a.683.683 0 0 0
 0-.11c-.61-4.85-3.896-9-8.697-10.301A11.676 11.676 0 0 0 12.07
 0zm-.108 3.025a.677.677 0 0 1 .396.14 11.07 11.07 0 0 1 1.86 1.677
 16.66 16.66 0 0 1 2.874-.246h.432c.95.027.962 1.5.027 1.5h-.443c-.618
 0-1.235.039-1.847.117a16.68 16.68 0 0 1 1.765 3.486c.947-.194
 1.91-.303 2.877-.326h.02c.95 0 .935 1.482-.02
 1.501-.802.023-1.6.11-2.387.264a26.43 26.43 0 0 1 .893
 4.221c.057.479-.285.715-.66.715a.83.83 0 0 1-.846-.715 29.483 29.483
 0 0 0-.23-1.411 23.662 23.662 0 0 0-.635-2.463 19.676 19.676 0 0
 0-.505-1.418 15.706 15.706 0 0
 0-1.93-3.577c-.263.069-.519.125-.782.2a15.29 15.29 0 0 0-1.805.616
 20.446 20.446 0 0 1 1.798 3.791c.626-.3 1.27-.562 1.93-.782l.713
 1.35a15.46 15.46 0 0 0-2.18.872 20.74 20.74 0 0 1 .782 5.25.7.7 0 0
 1-.74.726.723.723 0 0 1-.76-.727v-.228a18.878 18.878 0 0 0-.638-4.303
 15.612 15.612 0 0 0-.449-1.473A18.893 18.893 0 0 0 9.674 7.95a7.71
 7.71 0 0 0-.616.36c-.92.548-1.762 1.22-2.502 1.995a.685.685 0 0
 1-.503.232c-.563 0-1.073-.754-.563-1.29A13.44 13.44 0 0 1 8.514
 6.88c.096-.062.2-.117.304-.173-.221-.312-.46-.612-.712-.899a.832.832
 0 0 0-.07-.09c-.485-.554.023-1.306.57-1.306a.652.652 0 0 1
 .496.248c.38.442.74.899 1.079 1.376l.013.007a14.556 14.556 0 0 1
 1.923-.7c.13-.043.262-.08.396-.109a6.949 6.949 0 0 0-.85-.727.402.402
 0 0 0-.063-.048c-.646-.463-.243-1.434.363-1.434zm-1.386 9.299l.55
 1.44a16.386 16.386 0 0 0-2.656 2.157c-.159.13-.338.218-.5.215-.575
 0-1.088-.752-.56-1.28a18.44 18.44 0 0 1 3.166-2.532Z" />
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
