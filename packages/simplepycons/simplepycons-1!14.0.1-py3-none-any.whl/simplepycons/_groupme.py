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


class GroupmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "groupme"

    @property
    def original_file_name(self) -> "str":
        return "groupme.svg"

    @property
    def title(self) -> "str":
        return "GroupMe"

    @property
    def primary_color(self) -> "str":
        return "#00AFF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GroupMe</title>
     <path d="M11.1597
 6.57419H12.8398V8.16898H11.1597V6.57419ZM18.1997 0H5.80011C3.14898 0
 1 2.03979 1 4.55577V16.3243C1 18.8402 3.14898 20.88 5.80011
 20.88H9.92715L11.9786 24L14.0306 20.88H18.1997C20.8506 20.88 23
 18.8402 23 16.3243V4.55574C23 2.03976 20.8506 0 18.1997 0ZM7.56833
 8.16895H9.34755V6.57416H7.56833V4.85447H9.34755V3.16587H11.1597V4.85447H12.8398V3.16587H14.6519V4.85447H16.4308V6.57416H14.6519V8.16895H16.4308V9.88852H14.6519V11.5772H12.8398V9.88852H11.1597V11.5772H9.34755V9.88852H7.56833V8.16895ZM20.3122
 13.4321C20.3122 13.4321 17.9202 17.708 12.2406 17.708C12.1619 17.708
 12.0843 17.707 12.007 17.7057C11.9299 17.707 11.8522 17.708 11.7737
 17.708C6.09416 17.708 3.70211 13.4321 3.70211 13.4321C3.70211 13.4321
 3.54729 13.1536 3.54729 12.8534C3.53754 12.6368 3.64915 12.3263
 3.9421 12.1433C4.105 12.0417 4.259 11.9914 4.40179 11.9757C5.08566
 11.9069 5.48202 12.3295 5.80794 12.8121C6.16788 13.3447 8.24445
 15.678 12.007 15.7672C15.7698 15.678 17.8464 13.3447 18.2063
 12.8121C18.5322 12.3295 18.9429 11.9062 19.6125 11.9757C19.7553
 11.9914 19.9094 12.0417 20.0722 12.1433C20.3652 12.3263 20.4792
 12.5839 20.469 12.8532C20.446 13.2494 20.3122 13.4321 20.3122
 13.4321Z" />
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
