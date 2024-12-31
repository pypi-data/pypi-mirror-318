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


class ApacheDruidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachedruid"

    @property
    def original_file_name(self) -> "str":
        return "apachedruid.svg"

    @property
    def title(self) -> "str":
        return "Apache Druid"

    @property
    def primary_color(self) -> "str":
        return "#29F1FB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Druid</title>
     <path d="M8.932 20.806c-.369 0-.738.007-1.109
 0-.35-.007-.587-.206-.623-.5a.587.587 0 0 1 .53-.636c.79-.062
 1.582-.063 2.372-.003a.548.548 0 0 1
 .522.602c-.024.326-.253.526-.616.54zM1.792 8.345c-.392
 0-.782.008-1.173.002-.327-.006-.577-.22-.614-.512-.037-.293.146-.544.499-.615.192-.032.388-.045.583-.039a81.515
 81.515 0 0 1 1.597 0c.163 0
 .325.019.483.056.288.073.445.318.411.617-.034.298-.214.477-.515.487-.424.014-.848.004-1.272.004zm7.588
 8.417H4.292a2.464 2.464 0 0
 1-.326-.007c-.294-.04-.48-.209-.508-.506-.029-.298.11-.501.391-.606.179-.065.365-.051.549-.051
 3.347 0 6.695.005 10.042-.006 1.174-.004 2.187-.439 2.993-1.3.69-.738
 1.053-1.63
 1.16-2.635.085-.788-.027-1.513-.516-2.156-.544-.718-1.28-1.078-2.163-1.082-3.163-.013-6.328-.005-9.487-.01-.336
 0-.673-.027-1.007-.058-.29-.027-.45-.201-.469-.492-.021-.317.141-.545.429-.6a1.55
 1.55 0 0 1 .29-.015h10.177c1.71.004 3.187 1.038 3.726 2.654.383
 1.147.246 2.304-.182 3.416-.824 2.135-2.762 3.448-5.055
 3.454-1.652.005-3.304 0-4.956 0zm2.906-13.568c1.533 0 3.066-.008
 4.598 0 2.935.018 5.629 1.892 6.653 4.626.442 1.181.538 2.403.412
 3.657-.185 1.842-.735 3.552-1.776 5.084-1.608 2.365-3.873 3.68-6.679
 4.118-.95.148-1.905.13-2.86.13-.397
 0-.61-.181-.633-.51-.025-.351.196-.621.587-.645.434-.026.87-.004
 1.305-.016 2.641-.072 4.928-.982 6.74-2.935 1.269-1.37 1.912-3.039
 2.13-4.878.151-1.275.135-2.544-.37-3.752-.773-1.85-2.159-2.983-4.068-3.509-.74-.204-1.5-.243-2.26-.247-2.837-.017-5.675-.007-8.511-.007-.12
 0-.24.004-.359-.006a.57.57 0 0 1-.517-.536.557.557 0 0 1
 .456-.557c.13-.018.261-.024.392-.019h4.762Z" />
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
