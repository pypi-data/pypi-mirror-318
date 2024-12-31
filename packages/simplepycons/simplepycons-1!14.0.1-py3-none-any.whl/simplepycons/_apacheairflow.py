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


class ApacheAirflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apacheairflow"

    @property
    def original_file_name(self) -> "str":
        return "apacheairflow.svg"

    @property
    def title(self) -> "str":
        return "Apache Airflow"

    @property
    def primary_color(self) -> "str":
        return "#017CEE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Airflow</title>
     <path d="M17.195 16.822l4.002-4.102C23.55 10.308 23.934 5.154 24
 .43a.396.396 0 0 0-.246-.373.392.392 0 0 0-.437.09l-6.495
 6.658-4.102-4.003C10.309.45 5.154.066.43 0H.423a.397.397 0 0
 0-.277.683l6.658 6.494-4.003 4.103C.45 13.692.065 18.846 0
 23.57a.398.398 0 0 0 .683.282l6.494-6.657 3.934 3.837.17.165c2.41
 2.353 7.565 2.737 12.288 2.803h.006a.397.397 0 0 0
 .277-.683l-6.657-6.495zm-.409-9.476c.04.115.05.24.031.344-.17.96-1.593
 2.538-4.304 3.87a.597.597 0 0 0-.08-.079c1.432-3.155 1.828-5.61
 1.175-7.322l3.058 2.984.12.203zm-.131 9.44a.73.73 0 0
 1-.347.031c-.96-.171-2.537-1.594-3.87-4.307a.656.656 0 0 0
 .08-.078l-.001.001c3.155 1.432 5.61 1.83 7.324 1.174l-2.969
 3.043M23.568.392a.05.05 0 0 1 .052-.011c.018.006.03.024.029.043-.065
 4.655-.437 9.726-2.703 12.05-1.53 1.565-4.326
 1.419-8.283-.377.006-.037.021-.07.02-.108 0-.044-.017-.082-.026-.123
 2.83-1.39 4.315-3.037
 4.506-4.115.057-.322-.009-.542-.102-.688l6.507-6.67V.392zM.393.43A.045.045
 0 0 1 .382.38C.39.36.403.343.425.35c4.655.065 9.727.438 12.05
 2.703l.002.002c1.56 1.527 1.415 4.323-.379
 8.28-.033-.005-.062-.02-.097-.02h-.008c-.045.001-.084.019-.126.027-1.39-2.83-3.037-4.314-4.115-4.506-.323-.057-.542.01-.688.103L.393.43zm11.94
 11.563a.331.331 0 0 1-.327.335H12a.332.332 0 0
 1-.004-.661c.172.016.333.144.335.326h.002zm-5.12 4.661a.722.722 0 0
 1-.03-.345c.17-.96 1.595-2.54
 4.309-3.873.013.016.019.035.033.05.013.012.03.017.044.028-1.434
 3.158-1.83 5.613-1.177 7.326l-3.041-2.967m-.006-9.659a.735.735 0 0 1
 .345-.031c.961.17 2.54 1.594 3.871 4.306a.597.597 0 0
 0-.079.08c-2.167-.983-4.007-1.484-5.498-1.484-.68
 0-1.289.103-1.825.308L7.128 7.35M.43
 23.607c-.018.018-.038.015-.052.01-.019-.007-.028-.021-.028-.043.065-4.654.437-9.725
 2.703-12.049 1.527-1.565 4.325-1.419
 8.286.378-.006.035-.02.067-.02.104 0 .043.018.083.026.124-2.831
 1.391-4.317 3.04-4.51 4.117-.057.322.01.542.103.688L.43
 23.607zm23.144.042c-4.655-.065-9.726-.437-12.05-2.703l-.005-.006c-1.56-1.526-1.412-4.322.383-8.279.033.005.064.02.098.02h.009c.043
 0 .08-.018.122-.027 1.39 2.832 3.036 4.317 4.115
 4.51.083.014.16.021.23.021a.776.776 0 0 0 .45-.133l6.68
 6.516c.02.02.016.04.01.052a.042.042 0 0 1-.042.029z" />
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
