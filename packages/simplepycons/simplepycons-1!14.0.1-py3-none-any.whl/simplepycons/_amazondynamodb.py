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


class AmazonDynamodbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazondynamodb"

    @property
    def original_file_name(self) -> "str":
        return "amazondynamodb.svg"

    @property
    def title(self) -> "str":
        return "Amazon DynamoDB"

    @property
    def primary_color(self) -> "str":
        return "#4053D6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon DynamoDB</title>
     <path d="M16.606 20.705v-2.371c-1.263 1.082-3.884 1.795-7.066
 1.795-3.184 0-5.805-.714-7.068-1.797v2.369c0 1.168 2.903 2.47 7.068
 2.47 4.16 0 7.06-1.3 7.066-2.466zm.001-6.765l.817-.005v.005c0
 .517-.258.998-.75 1.441.601.54.75 1.071.75 1.449a1661.7 1661.7 0 0 0
 0 3.87c0 1.881-3.389 3.3-7.884 3.3-4.471
 0-7.846-1.404-7.88-3.27a583.119 583.119 0 0
 1-.003-3.909c.001-.375.15-.9.745-1.437-.592-.538-.743-1.062-.746-1.435v-3.892c.002-.377.153-.903.747-1.438-.593-.54-.744-1.062-.747-1.435
 0-1.357-.002-2.735.002-3.897C1.674 1.412 5.056 0 9.54 0c2.159 0
 4.233.356 5.689.974l-.315.766c-1.36-.58-3.319-.91-5.374-.91-4.165
 0-7.067 1.3-7.067 2.47 0 1.168 2.902 2.47 7.067 2.47.115 0 .222 0
 .334-.005l.033.828c-.122.006-.245.006-.367.006-3.184
 0-5.805-.714-7.068-1.798v2.38c.005.45.45.843.821 1.093 1.116.736
 3.114 1.239 5.34
 1.342l-.037.829c-2.254-.105-4.23-.59-5.5-1.332-.318.245-.623.573-.623.952
 0 1.168 2.902 2.47 7.067 2.47.411 0 .812-.014
 1.203-.042l.06.826c-.41.03-.833.045-1.263.045-3.184
 0-5.805-.713-7.068-1.797v2.368c.005.462.449.855.821 1.104 1.275.842
 3.67 1.366 6.247 1.366h.182v.83H9.54c-2.62
 0-4.99-.507-6.444-1.359-.317.245-.623.574-.623.954 0 1.168 2.902 2.47
 7.067 2.47 4.159 0 7.058-1.298
 7.066-2.465v-.007c0-.377-.303-.705-.62-.948a5.732 5.732 0 0
 1-.662.336l-.316-.764c.3-.128.56-.266.776-.412.376-.254.823-.651.823-1.1zm4.377-6.915h-2.717a.406.406
 0 0 1-.332-.173.42.42 0 0 1-.055-.375l1.204-3.597h-5.403l-2.583
 4.974h2.623c.128 0 .248.06.325.164a.418.418 0 0 1 .069.36l-2.249
 8.365zm1.249-.128l-10.89 11.608a.408.408 0 0 1-.498.075.418.418 0 0
 1-.192-.471l2.534-9.426h-2.766a.407.407 0 0 1-.349-.2.418.418 0 0
 1-.012-.407l3.014-5.804a.408.408 0 0 1 .36-.222h6.22c.132 0
 .256.065.332.174a.422.422 0 0 1 .055.374l-1.204 3.598h3.1c.164 0
 .31.099.375.251a.422.422 0 0 1-.08.45zM3.085 20.723a8.107 8.107 0 0 0
 1.72.72l.233-.794a7.32 7.32 0 0
 1-1.546-.645zm1.72-5.984l.233-.795a7.262 7.262 0 0
 1-1.546-.646l-.407.72a8.051 8.051 0 0 0
 1.72.72zm-1.72-7.427l.407-.719c.418.244.939.462
 1.546.646l-.232.794a8.046 8.046 0 0 1-1.72-.72Z" />
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
        yield from [
            "AWS DynamoDB",
        ]
