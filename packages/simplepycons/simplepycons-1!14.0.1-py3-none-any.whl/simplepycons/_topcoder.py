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


class TopcoderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "topcoder"

    @property
    def original_file_name(self) -> "str":
        return "topcoder.svg"

    @property
    def title(self) -> "str":
        return "Topcoder"

    @property
    def primary_color(self) -> "str":
        return "#29A7DF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Topcoder</title>
     <path d="M12.004 7.555c-1.87 0-3.88.979-5.559 2.678 1.741.384
 3.587.997 5.046 1.662l.513.23c.204-.09.367-.163.513-.23 1.464-.667
 3.318-1.282 5.064-1.667-1.645-1.796-3.508-2.673-5.577-2.673zm8.751
 2.723c-.675.016-1.44.101-2.282.254.608.784 1.26 2 1.928 3.503a43.559
 43.559 0 0 1 .981 2.4c.305-.06.58-.232.825-.542 1.393-1.761
 2.038-3.366 1.708-4.349-.26-.776-1.152-1.19-2.515-1.258a8.77 8.77 0 0
 0-.645-.008zm-17.506 0a8.844 8.844 0 0
 0-.646.008c-1.365.068-2.258.481-2.518 1.258-.33.983.315 2.588 1.708
 4.35.258.325.549.499.873.55.15-1.468 1.501-4.253 2.868-5.911a14.877
 14.877 0 0 0-2.285-.254zm14.69.352c-1.184.197-3.63.971-5.15
 1.638l-.036.017a10.22 10.22 0 0 1 1.798.599c1.268.55 1.504.694 5.169
 3.06.206.134.37.227.587.32.194.084.383.143.566.174a42.717 42.717 0 0
 0-1.316-3.092c-.46-.96-.906-1.758-1.323-2.338-.1-.14-.2-.266-.295-.378zm-11.866.004c-1.35
 1.538-2.758 4.38-2.927 5.802.361-.061.79-.24
 1.222-.49.317-.185.65-.394 1.054-.659.243-.16 1.153-.768 1.087-.724
 1.939-1.29 3.253-1.982 4.678-2.288-1.589-.69-3.798-1.417-5.114-1.64z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.topcoder.com/thrive/articles/How%'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.topcoder.com/thrive/articles/How%'''

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
