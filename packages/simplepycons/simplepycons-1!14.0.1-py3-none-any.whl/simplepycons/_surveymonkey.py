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


class SurveymonkeyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "surveymonkey"

    @property
    def original_file_name(self) -> "str":
        return "surveymonkey.svg"

    @property
    def title(self) -> "str":
        return "SurveyMonkey"

    @property
    def primary_color(self) -> "str":
        return "#00BF6F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SurveyMonkey</title>
     <path d="M21.1627 13.1843a2.8517 2.8517 0 0
 0-.6778.0841c-.8438-3.3181-3.5478-5.8376-6.9172-6.4452a8.3933 8.3933
 0 0 0-.4407-.0668c.0259-.8255.0636-1.7791
 1.2781-2.6369l-.1918-.4838s-2.3708.7349-2.6391
 2.7598c-.1175-.5507-1.2209-1.2403-1.7673-1.3707l-.2717.4384s.7242.3621.9009
 1.361c-3.3691.6056-6.0743 3.1229-6.9204
 6.4398-1.5194-.376-3.056.5508-3.432 2.0703-.376 1.5194.5508 3.056
 2.0703 3.432a2.8346 2.8346 0 0 0 1.7195-.1142 8.6821 8.6821 0 0 0
 .9203
 1.7123l2.3524-1.5852c-.6381-.8071-1.0206-1.9884-1.0873-3.1736-.07-1.2931.2446-2.5755
 1.0701-3.3298 1.7016-1.4483 3.5561-.7877
 4.7135.6002h.3114c1.1606-1.388 3.0173-2.0475 4.7135-.6002.8244.7543
 1.1401 2.0378 1.0701 3.3298-.0656 1.1853-.4481 2.3664-1.0873
 3.1736l2.3524 1.5852a8.6854 8.6854 0 0 0 .9224-1.7123c1.4551.5751
 3.1009-.1384 3.676-1.5935s-.1384-3.1009-1.5935-3.676a2.8349 2.8349 0
 0 0-1.0448-.1983zM2.7861 16.8482a.8362.8362 0 0 1 0-1.6724.8442.8442
 0 0 1 .4688.1444c.0071.4391.0369.8776.0894
 1.3136-.1472.1346-.3738.2329-.5582.2144zm18.4273 0a.8361.8361 0 0
 1-.5582-.2155 12.679 12.679 0 0 0 .0894-1.3136.8352.8352 0 0 1
 1.304.6929c.0078.4574-.3823.8581-.8352.8362z" />
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
