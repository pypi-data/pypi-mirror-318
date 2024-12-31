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


class PuppeteerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "puppeteer"

    @property
    def original_file_name(self) -> "str":
        return "puppeteer.svg"

    @property
    def title(self) -> "str":
        return "Puppeteer"

    @property
    def primary_color(self) -> "str":
        return "#40B5A4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Puppeteer</title>
     <path d="M17.89 17.86h.397v.174h.028a.466.466 0 0 1
 .619-.155l-.11.373a.364.364 0 0 0-.184-.043.288.288 0 0
 0-.243.11.471.471 0 0 0-.082.29v.635h-.424zm-.26 1.048a.766.766 0 0
 1-.27.28.741.741 0 0 1-.398.101.822.822 0 0 1-.3-.054.752.752 0 0
 1-.237-.155.704.704 0 0 1-.214-.529c0-.1.018-.194.056-.282a.719.719 0
 0 1 .156-.235.725.725 0 0 1 .529-.22.75.75 0 0 1 .302.056.642.642 0 0
 1 .353.384.846.846 0 0 1
 .037.402h-1.02c.02.09.063.156.127.198a.387.387 0 0 0 .214.062.345.345
 0 0 0 .32-.18zm-.376-.54a.227.227 0 0 0-.03-.074.21.21 0 0
 0-.058-.07.264.264 0 0 0-.093-.054.325.325 0 0
 0-.43.198zm-1.242.54a.766.766 0 0 1-.27.28.741.741 0 0
 1-.397.101.822.822 0 0 1-.3-.054.752.752 0 0 1-.237-.155.704.704 0 0
 1-.215-.529c0-.1.019-.194.057-.282a.719.719 0 0 1 .155-.235.725.725 0
 0 1 .529-.22c.115 0 .215.018.302.056a.642.642 0 0 1 .353.384.846.846
 0 0 1 .037.402h-1.02c.02.09.063.156.127.198a.387.387 0 0 0
 .215.062.345.345 0 0 0 .32-.18zm-.376-.54a.227.227 0 0
 0-.028-.074.21.21 0 0 0-.06-.07.264.264 0 0 0-.093-.054.325.325 0 0
 0-.43.198zm-1.918-.144l-.243-.004.004-.388.25.012-.007-.41.412.004-.016.39.367.02-.012.355-.365.008.013.47c-.012.092.022.145.027.194.08.1.137.068.137.068.02-.008.162-.027.177-.038l.04.388c-.138.082-.377.036-.377.036-.253-.037-.383-.217-.384-.293-.025-.068-.018-.21-.029-.29zm-.412.717c-.037.126-.172.218-.283.285a.772.772
 0 0 1-.406.11.944.944 0 0
 1-.32-.077c-.09-.038-.165-.113-.233-.18-.068-.065-.093-.142-.131-.23a.822.822
 0 0
 1-.045-.31c-.015-.194.126-.378.212-.505.28-.238.49-.22.49-.22.387-.075.696.288.718.437.03.086.022.18.022.28-.005.054
 0 .05-.031.125h-1.037c.02.09.063.192.104.24.048.06.128.06.207.06.079
 0 .163.002.214-.032.053-.034.172-.072.203-.125zm-.37-.558a.41.41 0 0
 0-.04-.097c-.014-.026-.05-.046-.076-.066-.024-.023-.071-.037-.109-.05a.31.31
 0 0 0-.121-.023.274.274 0 0
 0-.168.053c-.057.037-.097.12-.123.19zm-2.34-.372h.028a.388.388 0 0 1
 .147-.138.498.498 0 0 1 .254-.06.623.623 0 0 1 .467.207.696.696 0 0 1
 .147.232c.036.09.053.19.053.3a.8.8 0 0 1-.053.3.729.729 0 0
 1-.147.234.647.647 0 0 1-.467.203.518.518 0 0 1-.254-.056.409.409 0 0
 1-.147-.142h-.028l.028.198v.565H10.2V17.86h.396zm.336.198a.34.34 0 0
 0-.31.201.37.37 0 0 0-.026.141c0 .053.008.101.025.145a.362.362 0 0 0
 .074.107c.032.028.068.05.107.068a.378.378 0 0 0 .257 0 .348.348 0 0 0
 .108-.068.304.304 0 0 0 .073-.107.358.358 0 0 0 .028-.145.338.338 0 0
 0-.336-.342zm-2.026-.198h.03a.388.388 0 0 1 .146-.138.498.498 0 0 1
 .254-.06.623.623 0 0 1 .466.207.696.696 0 0 1
 .147.232c.036.09.054.19.054.3a.8.8 0 0 1-.054.3.729.729 0 0
 1-.147.234.647.647 0 0 1-.466.203.518.518 0 0 1-.254-.056.409.409 0 0
 1-.147-.142h-.029l.03.198v.565H8.51V17.86h.395zm.337.198a.34.34 0 0
 0-.31.201.37.37 0 0 0-.027.141c0 .053.01.101.026.145a.362.362 0 0 0
 .073.107c.032.028.068.05.108.068a.378.378 0 0 0 .257 0 .348.348 0 0 0
 .107-.068.303.303 0 0 0 .074-.107.358.358 0 0 0 .028-.145.338.338 0 0
 0-.21-.316.32.32 0 0 0-.126-.026zm-1.433.86h-.028a.47.47 0 0
 1-.424.22c-.174 0-.303-.055-.387-.167a.703.703 0 0
 1-.128-.438v-.825h.424v.777c0
 .076.018.138.054.187.036.047.091.07.167.07a.245.245 0 0 0
 .217-.11.497.497 0 0 0
 .077-.288v-.636h.424v1.385H7.81zm-2.594.175V17.22h.724a.82.82 0 0 1
 .285.048.677.677 0 0 1 .23.136.589.589 0 0 1 .15.206.67.67 0 0 1
 .053.27.657.657 0 0 1-.054.267.617.617 0 0 1-.379.342.818.818 0 0
 1-.285.048h-.283v.707zm.738-1.125c.092 0 .16-.023.206-.068a.234.234 0
 0 0 .068-.172.234.234 0 0
 0-.068-.173c-.045-.045-.114-.068-.206-.068h-.297v.48zM18.04
 2.758l-.594.05.236 2.932.626.363zm-12.016.01L5.728
 6.01l.624-.3.266-2.89zm-.49 5.183l-.044.557-1.247
 3.137c-.216.224-.308.514-.307.825L3.93 22.84c0 .669.49 1.16 1.158
 1.16H18.82c.67 0 1.25-.444
 1.25-1.11V12.485c0-.306-.1-.56-.286-.774L18.44
 7.748l-.006-.068-.575.257.267 3.33H5.846l.237-2.615.226-.588L6.143
 8l.002-.03zm13.112
 2.34l.323.987c-.088-.014-.158-.006-.245-.01zm-13.316.232l-.084.744c-.058-.005-.12.005-.172.007zm-.18
 1.134l13.67.008c.47 0
 .853.344.853.815v.796H4.313v-.796c0-.47.364-.823.837-.823zm.135.553a.27.27
 0 0 0-.272.27c0 .36.542.36.542 0a.27.27 0 0 0-.27-.27zm.92 0c-.36
 0-.36.54 0 .54s.362-.54.002-.54zm.896 0c-.39-.034-.39.572 0
 .538.33-.028.33-.51 0-.538zm-2.788 1.424h15.36v9.153c0
 .595-.38.846-.853.845l-13.668-.004a.828.828 0 0 1-.84-.841zm1.883
 4.42c.07-.117.07-.11.068-.186-.008-.073-.004-.076-.053-.135-.054-.054-.123-.138-.2-.134h-.387l-.02.55h.407c.122-.002.16-.084.185-.094zm-.185-.83a.58.58
 0 0 1 .442.171c.11.117.164.273.164.465a.65.65 0 0
 1-.16.462c-.117.12-.263.21-.43.203l-.4.008-.004.774-.412-.013-.005-2.088zm1.793
 1.26l-.012-.624.366-.004.004 1.435-.36.004v-.122a.582.582 0 0
 1-.432.15.557.557 0 0
 1-.413-.156c-.103-.11-.13-.31-.123-.46l-.004-.847h.372l-.008.77a.328.328
 0 0 0 .075.23.25.25 0 0 0 .198.09c.225 0
 .336-.156.336-.468zm1.805.077a.36.36 0 0
 0-.11-.272c-.07-.073-.115-.118-.218-.115-.1
 0-.186.018-.266.094a.388.388 0 0 0-.116.293c0
 .12.038.217.117.29.07.073.168.114.27.114.102.003.166-.053.238-.126.087-.094.06-.21.085-.278zm-.262-.76c.176
 0 .333.11.466.245a.71.71 0 0 1 .197.515.7.7 0 0
 1-.197.512c-.093.16-.31.255-.486.254-.16.005-.36-.066-.428-.197l.004.76-.4.006-.02-2.04.416-.02v.157c.126-.103.285-.2.448-.193zm2.002.764c-.014-.16-.044-.203-.117-.283-.072-.074-.117-.087-.22-.085-.1
 0-.178-.005-.257.07a.388.388 0 0 0-.116.294c0
 .12.038.217.116.29.07.073.168.114.27.114.102.003.154-.065.226-.137.073-.08.086-.175.098-.263zm-.318-.75c.177
 0 .389.096.522.23a.712.712 0 0 1 .198.516.7.7 0 0
 1-.198.512c-.105.15-.344.255-.522.254a.475.475 0 0
 1-.392-.197v.75l-.405.01-.023-2.034h.428v.137c.126-.103.23-.183.392-.177zm1.268.576l.637-.008c-.017-.074-.063-.12-.124-.166a.357.357
 0 0
 0-.406.003c-.085.068-.054.056-.107.17zm.313-.575c.179-.003.425.078.552.203.133.13.157.308.166.512l-.031.125h-1.03c.02.095.044.186.104.244.059.056.153.07.234.07a.5.5
 0 0 0 .383-.17l.316.141c-.046.14-.187.223-.304.296a.757.757 0 0
 1-.408.094c-.184.003-.378-.116-.507-.247a.718.718 0 0
 1-.2-.523c0-.21.094-.382.23-.518.13-.132.31-.232.495-.227zm1.673
 1.127c.08-.003.11.002.178-.038l.04.388c-.107.063-.135.038-.26.042a.633.633
 0 0
 1-.416-.155c-.094-.09-.097-.26-.097-.443l-.012-.513-.243-.004.004-.388.25.012-.007-.41.412.004-.016.39.367.02-.012.355-.365.008.003.507c.002.155.042.225.175.225zm.75-.54h.654a.32.32
 0 0 0-.12-.186.357.357 0 0 0-.407.003.3.3 0 0
 0-.127.184zm.338-.587c.185 0
 .368.092.5.22.133.13.173.295.183.5v.12h-1.03a.4.4 0 0 0 .12.228.31.31
 0 0 0 .218.086c.155 0
 .297-.06.367-.18l.3.15c-.05.13-.12.19-.238.262a.958.958 0 0
 1-.452.125.712.712 0 0 1-.502-.224.77.77 0 0
 1-.208-.542c0-.21.106-.382.24-.518.132-.132.316-.232.5-.227zm1.27.587h.654a.32.32
 0 0 0-.12-.186.357.357 0 0 0-.407.003.3.3 0 0
 0-.127.184zm.337-.587a.74.74 0 0 1
 .5.22c.134.13.174.295.184.5v.12h-1.03a.4.4 0 0 0 .12.228.31.31 0 0 0
 .217.086c.154 0
 .297-.06.368-.18l.3.15c-.05.13-.12.19-.238.262a.957.957 0 0
 1-.454.125.713.713 0 0 1-.5-.224.77.77 0 0
 1-.208-.542c0-.21.106-.382.24-.518.13-.132.315-.232.5-.227zm1.938.04l-.067.364-.18-.023c-.322
 0-.36.207-.36.595v.49l-.393.005.008-1.43h.365l-.004.22c.145-.17.215-.286.63-.22zM17.535
 7.91l.02-.366 1.317-.687.007.396zM5.04
 6.84l1.35.68-.008.393-1.314-.65zm7.21-1.748l4.839
 2.448v.392l-4.851-2.46zM6.874 7.51l4.894-2.42-.007.374-4.893
 2.444zm3.467-3.974L5.418 1.099 6.64.494l5.352
 2.744L17.335.466l1.257.65-4.926 2.478c-.196.098-.13.388.067.486l4.838
 2.42-1.22.622-5.353-2.697L6.62 7.129l-1.273-.634 4.998-2.483a.266.266
 0 0 0-.004-.477zM5.059 1.888l.007-.377 4.607 2.276-.348.2zm9.648
 2.077l-.41-.184 4.596-2.303-.028.412zm.422.306l4.124-2.07a.124.124 0
 0 0 .07-.11v-.98c0-.046-.008-.136-.05-.157l-1.94-.94a.124.124 0 0
 0-.113 0l-5.167 2.623a.123.123 0 0 1-.11 0L6.679.015a.124.124 0 0
 0-.11 0L4.616.938c-.04.02-.02.11-.02.157v.995c0
 .047.026.09.07.11l4.14 2.047L4.69 6.239c-.04.02-.108.062-.11.108l.017
 1.034a.123.123 0 0 0
 .068.113l1.933.986c.034.018.122.03.157.014l5.186-2.602a.124.124 0 0 1
 .11 0l5.12 2.603a.124.124 0 0 0 .11
 0l1.972-.954c.042-.02.103-.05.104-.096l-.007-1.033c0-.047-.047-.15-.09-.17z"
 />
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
