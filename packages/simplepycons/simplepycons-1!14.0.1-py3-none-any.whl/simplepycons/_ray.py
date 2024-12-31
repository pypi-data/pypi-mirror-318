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


class RayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ray"

    @property
    def original_file_name(self) -> "str":
        return "ray.svg"

    @property
    def title(self) -> "str":
        return "Ray"

    @property
    def primary_color(self) -> "str":
        return "#028CF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ray</title>
     <path d="M16.153 12.826c-.63-.183-1.03.15-1.378.846-.58
 1.13-1.643 1.644-2.888
 1.594-1.245-.05-2.257-.63-2.788-1.776-.233-.498-.498-.664-1.046-.68-.93-.017-1.643.016-2.174
 1.062-.631 1.261-2.258 1.693-3.619 1.261a3.234 3.234 0 0 1-2.257-3.22
 3.198 3.198 0 0 1 2.29-3.02 3.276 3.276 0 0 1 3.702
 1.327c.216.315.216.863.597.93.648.1 1.328.033 1.992.033.299 0
 .316-.266.399-.465.58-1.295 1.61-1.959 2.987-1.975 1.361-.017
 2.39.647 2.955 1.892.215.465.48.598.946.548.166-.017.332.016.498 0
 .464-.083 1.062.282
 1.344-.448.282-.73-.382-.913-.68-1.245-.847-.946-1.81-1.793-2.673-2.706-.415-.465-.763-.614-1.41-.415-1.876.614-3.619-.431-4.15-2.357-.448-1.676.714-3.535
 2.44-3.917a3.293 3.293 0 0 1 3.95
 2.457c.017.05.017.083.033.133.117.564.117 1.145-.132
 1.626-.283.531-.133.83.249 1.195a152.61 152.61 0 0 1 3.286
 3.27c.299.299.498.349.913.2 1.51-.565 2.97-.1 3.884 1.161a3.266 3.266
 0 0 1-.067 3.801c-.896 1.195-2.357 1.643-3.834
 1.079-.381-.15-.58-.1-.846.182a163.619 163.619 0 0 1-3.403
 3.386c-.299.3-.415.532-.232.98a3.198 3.198 0 0 1-1.278 3.917A3.298
 3.298 0 0 1 9.646 23c-1.062-1.062-1.228-2.688-.415-4.033a3.196 3.196
 0 0 1 3.835-1.294c.498.182.78.083 1.145-.283 1.012-1.045 2.058-2.058
 3.087-3.103.266-.266.68-.449.432-1.03-.233-.547-.631-.414-1.03-.431zM11.97
 4.942c.913.016 1.643-.714 1.66-1.627v-.05a1.646 1.646 0 0 0-1.76-1.56
 1.63 1.63 0 0 0-1.543 1.527 1.638 1.638 0 0 0 1.577 1.71zm.033
 5.41a1.658 1.658 0 0 0-1.676 1.61v.084a1.73 1.73 0 0 0 1.643
 1.66c.847.016 1.643-.78 1.677-1.627a1.648 1.648 0 0
 0-1.577-1.71c-.017-.016-.05-.016-.067-.016zm7.088 1.694c.016.896.747
 1.61 1.626 1.643a1.723 1.723 0 0 0 1.66-1.726 1.666 1.666 0 0
 0-1.66-1.61 1.623 1.623 0 0 0-1.643
 1.577c.017.05.017.083.017.116zM3.24 10.353a1.692 1.692 0 0 0-1.66
 1.626c-.017.847.863 1.727 1.693 1.71a1.687 1.687 0 0 0 1.626-1.743
 1.615 1.615 0 0 0-1.643-1.593Zm8.68 12c.98.033 1.71-.647
 1.727-1.593a1.646 1.646 0 0 0-1.51-1.793 1.646 1.646 0 0 0-1.793
 1.51v.233a1.609 1.609 0 0 0 1.543 1.66c0-.017.017-.017.033-.017z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ray-project/ray/blob/65229'''

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
