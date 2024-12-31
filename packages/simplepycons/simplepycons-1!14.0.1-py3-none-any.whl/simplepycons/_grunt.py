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


class GruntIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "grunt"

    @property
    def original_file_name(self) -> "str":
        return "grunt.svg"

    @property
    def title(self) -> "str":
        return "Grunt"

    @property
    def primary_color(self) -> "str":
        return "#FAA918"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Grunt</title>
     <path d="M13.04 0c-1.381.488-1.731 1.231-1.835
 1.906-.355-.254-.316-1.079-.336-1.29-.353.041-1.366 1.025-1.32
 2.265a7.96 7.96 0 00-.276.08c-.296-.402-1.167-1.472-2.314-1.842A3.647
 3.647 0 005.832.936c-1.36
 0-2.163.81-2.17.818l-.383.445.576.114c.01.002.966.201
 1.362.826.065.104.083.31.101.527.012.13-.016.257-.043.379-.02.09-.038.181-.043.273-.358.014-.665.084-.914.211a1.255
 1.255 0 00-.662.797c-.233.854.525 1.805.551 1.836.089.158.126
 1.303-.078
 1.762-.028.063-.103.126-.201.205-.03.024-.065.049-.102.076-.288.217-.722.548-.722
 1.305 0 1.036 1.05 1.597 1.894
 2.049.139.074.271.144.39.212l-.003.004c.126.073.57.534.57 1.223 0
 .323-.028 1.859-.172 2.924-.541-.464-1.04-1.211-1.152-2.049 0 0-1.372
 1.057-.969 3.32.246 1.385 1.087 2.16 2.203 2.565.405.89 1.365 2.143
 3.155 2.326.677.554 1.613.913 2.978.914V24h.008c1.367-.001 2.305-.36
 2.982-.916 1.786-.185 2.744-1.437 3.149-2.326 1.116-.406 1.957-1.18
 2.203-2.565.402-2.263-.969-3.32-.969-3.32-.112.838-.61 1.585-1.152
 2.049-.144-1.065-.174-2.601-.174-2.924
 0-.689.446-1.15.572-1.223l-.004-.004c.12-.068.253-.138.39-.212.845-.452
 1.893-1.013 1.893-2.05
 0-.756-.434-1.087-.722-1.304l-.102-.076c-.097-.079-.173-.142-.2-.205-.205-.46-.168-1.604-.079-1.762.026-.03.784-.982.55-1.836a1.255
 1.255 0 00-.661-.797c-.248-.127-.554-.197-.91-.21a1.655 1.655 0
 00-.043-.276 1.289 1.289 0
 01-.043-.379c.018-.218.036-.423.101-.527.396-.625 1.35-.825
 1.36-.826l.576-.114-.381-.445c-.007-.008-.812-.818-2.172-.818-.371
 0-.75.06-1.129.183-1.148.37-2.018 1.443-2.312 1.844a8.06 8.06 0
 00-.45-.127c-.196-.74.42-1.803.42-1.803s-.635-.14-1.578.715C13 1.442
 12.743.784 13.04 0zm5.118 1.637c.516 0 .936.14
 1.158.234-.144.065-.3.15-.455.252a2.51 2.51 0 00-.43-.037 2.33 2.33 0
 00-1.347.418c-.578.406-.846.793-.969 1.049a5.47 5.47 0
 00-.552-.28c.285-.418.926-1.236
 1.767-1.507.265-.086.543-.13.828-.13zm-12.314.002c.285 0
 .564.043.828.129.839.27 1.481 1.086 1.767
 1.505-.074.034-.15.068-.222.104a5.505 5.505 0
 00-.33.176c-.124-.256-.392-.641-.969-1.047a2.32 2.32 0
 00-1.346-.418c-.172 0-.32.017-.433.037a3.15 3.15 0 00-.453-.25 3.034
 3.034 0
 011.158-.236zm-.157.982c.349.014.655.123.913.328.386.308.572.844.634
 1.057a2.965 2.965 0 00-.49.521 6.575 6.575 0 00-.543-.125C6.048 4.194
 6.025 3.91 6 3.61c-.024-.29-.05-.588-.205-.834a1.932 1.932 0
 00-.107-.154zm12.625.002a1.91 1.91 0
 00-.105.15c-.155.246-.18.544-.205.834-.025.3-.05.587-.203.795-.197.037-.38.08-.541.125a2.952
 2.952 0
 00-.488-.52c.065-.221.256-.754.634-1.056.257-.204.562-.314.909-.328zm-6.31.727c1.307
 0 2.477.25 3.482.74.667.325.916.57 1.01.705-1.596.709-2.483
 2.164-2.492 2.18l-.162.273.262-.182.02-.015c.407-.321 1.827-1.395
 3.003-1.768.329-.104.966-.28 1.541-.28.293 0
 .53.045.707.136.166.085.27.206.314.369.117.425-.289 1.057-.439
 1.246a.518.518 0 00-.06.1 6.35 6.35 0 01-.016-.672c-.188.41-.305
 1.477-.238 2.017.168 1.373.736 2.078.736
 2.078-.037-.073-.082-.362-.125-.699.034.03.068.057.101.084l.024.02c.214.172.416.333.416.853
 0 .665-.72 1.056-1.416
 1.432-.134.072-.267.143-.395.217-.406.234-.845.784-.894
 1.603-.041.687.043 2.338.162 3.555-.584.226-1.253.3-1.861.318a5.246
 5.246 0 01-.258-.617h.002c-.032-.092-.919-2.394-1.239-2.918.257
 1.835.823 3.459 1.102 4.201a4.04 4.04 0
 00-.549-.035l-2.736-.002h-.006l-2.736.002c-.206
 0-.387.013-.55.035.28-.742.846-2.366 1.102-4.201-.319.524-1.205
 2.826-1.236 2.918a5.244 5.244 0
 01-.258.617c-.608-.017-1.277-.092-1.861-.318.12-1.217.201-2.868.16-3.555-.049-.819-.486-1.37-.892-1.603-.127-.074-.261-.145-.395-.217-.696-.376-1.416-.767-1.416-1.432
 0-.52.202-.681.416-.853l.023-.02.102-.084c-.043.335-.089.623-.125.697.006-.007.569-.71.736-2.076.067-.54-.052-1.607-.24-2.017.008.227
 0 .454-.016.67a.516.516 0
 00-.058-.098c-.15-.189-.556-.821-.44-1.246a.575.575 0
 01.315-.37c.176-.09.414-.134.707-.134.575 0 1.214.175 1.543.28C8.055
 5.655 9.474 6.73 9.88
 7.05l.02.015.26.182-.163-.273c-.01-.016-.895-1.471-2.49-2.18.094-.135.342-.38
 1.01-.705 1.005-.49 2.177-.74 3.484-.74zm-1.281 4.613s.68.827
 1.277.834v.002h.006c.597-.007 1.277-.834
 1.277-.834v-.002c-.466.282-.884.38-1.281.389a2.495 2.495 0
 01-1.28-.39zm-4.434.066c-.23.006-.47.036-.717.096.204.045.416.11.633.191l-.004.002c-.192.085-.3.323-.326.555-.054.47.244.898.244.898.03-.35.104-.6.19-.777.02.483.147
 1.104.597 1.602.323.357 1.667 1.094
 2.57.285.048.115.1.25.141.398.137.481-.125 1.184-.125
 1.184s.705-.8.65-1.525c.507-.023 1.005-.394.99-.915 0
 0-.883.488-1.663-.41-.4-.458-1.567-1.622-3.18-1.584zm11.428
 0c-1.613-.038-2.781 1.126-3.18
 1.584-.78.898-1.664.41-1.664.41-.014.52.482.892.988.915-.054.724.653
 1.525.653
 1.525s-.262-.703-.125-1.184c.042-.147.091-.282.138-.396.903.807
 2.248.07 2.57-.287.452-.5.579-1.12.598-1.604.086.178.16.428.19.78 0 0
 .3-.43.246-.899-.027-.232-.134-.47-.326-.555-.002 0-.004
 0-.006-.002.217-.082.431-.146.635-.191a3.367 3.367 0
 00-.717-.096zm-10.512.76c.915.514 1.754 1.204 2.104
 1.736-.263.155-1.008.496-1.778-.076-.487-.362-.465-1.235-.326-1.66zm9.596
 0c.14.425.161 1.298-.326 1.66-.77.572-1.517.23-1.78.076.35-.532
 1.191-1.222 2.106-1.736zM4.455 16.197c.512 1.614 2.212 2.075 3.486
 2.131a7.15 7.15 0 01-.34.485l-.052.052c-.339.366-.404.87-.194
 1.494-1.057-.016-2.163-.468-2.724-1.392-.569-.936-.41-2.535-.176-2.77zm15.092
 0c.233.235.393 1.834-.176 2.77-.561.923-1.664 1.373-2.72
 1.39.21-.624.144-1.125-.194-1.49l-.002-.002c-.018-.02-.04-.04-.06-.06a7.1
 7.1 0 01-.334-.477c1.274-.055 2.975-.517 3.486-2.13zM12
 18.895l2.045.001h.74c.709 0 1.019.184 1.154.338.198.226.21.589.04
 1.08v.002c-.31.886-1.14 3.03-3.979
 3.034-2.839-.004-3.67-2.148-3.979-3.034-.17-.491-.157-.856.041-1.082.136-.154.446-.338
 1.155-.338h.74L12 18.895zm-1.805.72l-.896.002h-.182c-.256
 0-.384.074-.445.135-.089.09-.102.213-.041.37.163.415.533.756.642.85a.86.86
 0 00.551.196l.002.002c.207 0
 .39-.076.516-.211.352-.376.561-.782.611-.906.029-.071.062-.207-.04-.313-.081-.082-.221-.125-.417-.125h-.3zm3.31
 0c-.194
 0-.335.043-.415.125-.104.106-.07.242-.041.313.05.124.259.53.611.906v.002c.126.135.31.209.518.209a.861.861
 0
 00.55-.197c.11-.094.48-.434.643-.85.061-.156.048-.281-.04-.371-.061-.06-.188-.135-.444-.135h-.184l-.896-.002h-.301zm-6.728
 1.387c.282.052.575.088.873.111.163.379.347.748.577 1.088a3.186 3.186
 0 01-1.45-1.199zm10.446 0a3.19 3.19 0 01-1.442
 1.195c.228-.34.413-.707.574-1.084a8.26 8.26 0 00.868-.111Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/gruntjs/grunt-docs/blob/ma'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/gruntjs/gruntjs.com/blob/7
0f43898d9ce8e6cc862ad72bf8a7aee5ca199a9/src/media/grunt-logo-no-wordma'''

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
