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


class NetgearIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "netgear"

    @property
    def original_file_name(self) -> "str":
        return "netgear.svg"

    @property
    def title(self) -> "str":
        return "NETGEAR"

    @property
    def primary_color(self) -> "str":
        return "#2C262D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NETGEAR</title>
     <path d="M11.496 12.459h.678c-.035.362-.296.545-.67.545-.566
 0-.849-.496-.849-.982 0-.479.244-.991.811-.991.347 0
 .598.2.716.499l.817-.324c-.285-.588-.813-.88-1.493-.88-1.068
 0-1.746.672-1.746 1.691 0 .987.699 1.657 1.74 1.657.555 0 1.017-.186
 1.341-.616.295-.391.329-.782.338-1.24h-1.683v.641ZM6.86
 11.122h.833v2.449h.874v-2.449h.834v-.692H6.86v.692Zm-4.565
 1.229h-.009L.861 10.43H0v3.141h.861v-1.924H.87l1.425
 1.924h.861V10.43h-.861v1.921Zm15.414-1.921-1.157
 3.141h.889l.19-.578h1.149l.189.578h.889l-1.156-3.141h-.993ZM4.174
 13.571h2.098v-.691H5.036v-.543h1.185v-.69H5.036v-.525h1.236v-.692H4.174v3.141Zm9.761
 0h2.099v-.691h-1.237v-.543h1.185v-.69h-1.185v-.525h1.237v-.692h-2.099v3.141Zm8.954-2.174c0-.67-.497-.967-1.15-.967h-1.34v3.141h.86v-1.208h.062l.785
 1.208h1.046l-.987-1.287c.47-.079.724-.453.724-.887Zm-5.054.971.358-1.096h.024l.359
 1.096h-.741Zm3.646-.53h-.222v-.782h.247c.282 0
 .522.049.522.391s-.265.391-.547.391Zm2.133-1.408c-.202
 0-.386.157-.386.378 0 .218.186.38.386.38.202 0 .386-.16.386-.38
 0-.225-.18-.378-.386-.378Zm0 .688c-.164 0-.315-.13-.315-.31
 0-.183.149-.311.316-.311.164 0 .316.132.316.311 0
 .183-.15.31-.317.31Zm.184-.404c0-.104-.101-.122-.174-.122h-.161v.416h.11v-.164h.033l.075.164h.121l-.089-.182c.049-.016.085-.054.085-.112Zm-.185.061h-.04v-.111h.033c.037
 0 .079.006.079.057 0 .045-.039.054-.072.054Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.powershift.netgear.de/images/powe'''

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
