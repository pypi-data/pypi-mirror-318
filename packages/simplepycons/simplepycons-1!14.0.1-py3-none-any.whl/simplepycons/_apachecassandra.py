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


class ApacheCassandraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachecassandra"

    @property
    def original_file_name(self) -> "str":
        return "apachecassandra.svg"

    @property
    def title(self) -> "str":
        return "Apache Cassandra"

    @property
    def primary_color(self) -> "str":
        return "#1287B1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Cassandra</title>
     <path d="M10.374 10.53a3.102 3.102 0 0 1-.428-.222l.555.143c0
 .02-.01.036-.01.055l-.117.025zm-.283
 1.506-.315.253.852-1.079-1.078.391c.002.017.009.033.009.05a.57.57 0 0
 1-.184.42c.102.217.228.424.375.616a3.2 3.2 0 0 1
 .34-.651zm.717-2.347-.652-.82a.427.427 0 0
 1-.506.162c-.054.073-.083.162-.13.24l1.258.463c.011-.015.019-.031.03-.045zm-1.666.444c-.07.314-.087.637-.05.956a.566.566
 0 0 1
 .451.475l.946-.606c-.067-.022-.126-.06-.191-.088l-1.119-.08.64-.14a3.186
 3.186 0 0 1-.668-.554l-.01.037zM20.1 11.648c-.164.202.833 1.022.833
 1.022s-1.654-1.022-2.234-.72c-.278.144.574.811 1.175
 1.242-.428-.274-.982-.571-1.175-.408-.328.277 1.565 2.549 1.565
 2.549s-2.145-2.322-2.36-2.209c-.214.114.593 1.224.593
 1.224s-1.06-1.16-1.35-.959c-.29.202 1.514 3.218 1.514
 3.218s-1.956-3.091-2.763-2.574c1.268 2.782.795 3.18.795
 3.18s-.162-2.839-1.742-2.764c-.795.038.379 2.12.379
 2.12s-1.08-1.902-1.8-1.864c1.326 2.51.854 3.53.854
 3.53s.219-2.143-1.58-3.336c.682.606-.427 3.336-.427
 3.336s.976-4.023-.719-3.256c-.268.121-.019 2.007-.019
 2.007s-.34-2.158-.851-2.045c-.298.066-1.893 2.99-1.893
 2.99s1.306-3.16.908-3.027c-.29.096-.833 1.4-.833 1.4s.265-1.287
 0-1.363c-.264-.075-1.74 1.363-1.74
 1.363s1.097-1.287.908-1.552c-.287-.402-.623-.42-1.022-.265-.581.226-1.363
 1.287-1.363 1.287s.78-1.074.643-1.476c-.219-.647-2.46 1.249-2.46
 1.249s1.325-1.25
 1.022-1.514c-.303-.265-1.947-.183-2.46-.185-1.515-.004-2.039-.36-2.498-.724
 1.987.997 3.803-.151
 6.094.494l.21.06c-1.3-.558-2.144-1.378-2.226-2.354-.036-.416.074-.827.297-1.222.619-.4
 1.29-.773 2.06-1.095a4 4 0 0 0-.064.698c0 2.44 2.203 4.417 4.92
 4.417s4.92-1.977 4.92-4.417c0-.45-.083-.881-.223-1.29 1.431.404
 2.45.968 3.132
 1.335.022.092.045.184.053.279.024.274-.018.547-.11.814.095-.147.198-.288.28-.445.367-.997
 1.855.227 1.855.227s-1.085-.454-1.06-.24c.026.215 1.628.96
 1.628.96s-1.45-.455-1.362-.114c.088.34 1.817 1.703 1.817
 1.703s-1.956-1.489-2.12-1.287zm-7.268 2.65.042-.008-.06.01zM9.256
 9.753c.12.13.26.234.396.343l.927-.029-1.064-.788c-.093.154-.195.303-.26.474Zm10.62
 3.44c.3.215.54.373.54.373s-.24-.181-.54-.374zM7.507
 8.617c-.14.229-.214.492-.215.76a3.99 3.99 0 0 0 2.358
 3.64c0-.005.002-.01.003-.014a3.19 3.19 0 0
 1-.58-.788c-.648.099-.926-.794-.336-1.08a3.174 3.174 0 0 1 .138-1.388
 3.162 3.162 0 0
 1-.52-1.36c-.296.07-.579.147-.848.23Zm1.488.82c.108-.24.243-.46.402-.661a.435.435
 0 0 1 .568-.557c.077-.059.166-.099.248-.15a16.17 16.17 0 0
 0-1.727.284c.114.388.272.76.509 1.084Zm2.285 3.928c1.4 0 2.633-.723
 3.344-1.816a3.399 3.399 0 0
 0-1.265-.539l-.297-.023.916.9-1.197-.467.704
 1.078-1.074-.832-.012.006.347 1.278-.596-1.134-.098
 1.33-.401-1.326-.472
 1.261.114-1.359c-.006-.002-.01-.006-.015-.008l-.814
 1.154.286-1.067c-.34.322-.605.713-.781
 1.146.095.102.197.198.303.29.322.083.66.128
 1.008.128zm10.145-4.434c.971-.567 1.716-1.955 1.716-1.955s-1.893
 1.955-3.205 1.665c1.186-.934 1.766-2.549 1.766-2.549s-1.506
 2.325-2.448 2.423c1.086-.959 1.54-2.322 1.54-2.322s-1.237 1.817-2.196
 1.944c1.287-1.161 1.338-1.893 1.338-1.893s-1.781 2.302-2.499
 1.943c.858-.934 1.439-2.12 1.439-2.12s-1.489 2.019-1.893
 1.69c-.277-.05.454-.958.454-.958s-.908.807-1.16.606c.454-.278
 1.236-1.64 1.236-1.64S16 7.505 15.621 7.304l.731-1.483s-.73
 1.483-1.715 1.23c.454-.58.63-1.112.63-1.112s-.756
 1.213-1.69.885c-.22-.077.273-.635.273-.635s-.626.61-1.055.534c-.43-.076.025-.858.025-.858s-.757
 1.186-.908
 1.136c-.152-.05.075-.833.075-.833s-.555.908-.858.858c-.302-.05 0-.934
 0-.934s-.328.984-.58.909c-.252-.076-.303-.656-.303-.656s-.068.788-.429.858c-2.725.53-5.728
 1.69-9.489 5.45C3.887 10.738 5.3 7.91 11.962 7.659c5.044-.191 7.399
 2.137 8.177 2.17C22.51 9.93 24 7.633 24 7.633s-1.489 1.716-2.574
 1.3zm-7.74.872-.608.464v.001l.054.003a3.35 3.35 0 0 0
 .554-.468zm1.583-.426c0-.536-.237-.929-.594-1.217a3.178 3.178 0 0
 1-.165.825.393.393 0 0
 1-.328.681c-.154.233-.34.445-.549.63l.661.034-.995.237c-.025.018-.045.041-.07.058a3.194
 3.194 0 0 1 1.536.691c.32-.574.504-1.235.504-1.94zM10.99 7.996a3.5
 3.5 0 0 0-.785.46.427.427 0 0
 1-.013.357l.885.643.023-.016-.36-1.262.627
 1.12c.018-.006.04-.006.058-.011l-.02-1.251.398 1.163.477-1.15.016
 1.268c.004.001.007.005.012.007l.713-1.005-.363 1.218.009.01
 1.04-.69-.759
 1.05.002.005.95-.34c.012-.016.028-.029.041-.045a.395.395 0 0 1
 .394-.632 3.43 3.43 0 0 0 .27-.784 13.99 13.99 0 0
 0-2.798-.168c-.286.011-.55.033-.817.053Z" />
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
