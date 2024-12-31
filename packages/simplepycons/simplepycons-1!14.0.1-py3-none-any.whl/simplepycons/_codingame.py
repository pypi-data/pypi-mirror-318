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


class CodingameIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codingame"

    @property
    def original_file_name(self) -> "str":
        return "codingame.svg"

    @property
    def title(self) -> "str":
        return "CodinGame"

    @property
    def primary_color(self) -> "str":
        return "#F2BB13"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodinGame</title>
     <path d="M1.025
 11.893c-.1.293-.07.561.009.67.078.11.223.26.55.272.327.012.697-.167.697-.167l-.136.78c-.008.008-.4.138-.88.134-.661-.004-1.321-.317-1.261-1.252.006-.081.053-.398.128-.573a1.8
 1.8 0 0 1 1.105-1.073c.67-.236 1.39-.016
 1.39-.016l-.141.817s-.247-.203-.755-.154a1.055 1.055 0 0
 0-.323.106.853.853 0 0 0-.383.456zm3.98.594c-.08.479-.446 1.097-1.397
 1.097-.951 0-1.102-.618-1.016-1.097.217-1.134 1.394-1.077
 1.394-1.077s1.195-.057 1.02
 1.077zm-.887-.277c-.043-.175-.241-.169-.241-.169v.001s-.213-.017-.33.21c-.136.314-.075.514-.07.532.043.175.24.169.24.169v-.001s.214.017.33-.21c.136-.314.075-.514.07-.532zm3.827-1.747l-.534
 3.07h-.868l.043-.245a.84.84 0 0 1-.66.3c-.527
 0-.813-.395-.707-1.003.132-.76.65-1.2 1.138-1.2.234 0
 .411.099.512.275v-.002l.208-1.195zm-1.43
 1.577c-.205-.004-.36.242-.402.48-.04.238-.005.427.244.43.15 0
 .326-.088.394-.43.028-.163.05-.48-.236-.48zm3.554-.556s-.259-.174-.698
 0c-.189.073-.374.308-.374.308l.058-.335h-.867l-.26
 1.493h.87l.1-.573.002-.019c.014-.071.078-.318.305-.318.265 0
 .18.334.18.334l-.198
 1.159h.866l.237-1.363c.09-.525-.22-.686-.22-.686zm-1.367-.338c.22 0
 .398-.156.398-.349 0-.193-.178-.349-.398-.349-.22 0-.398.156-.398.35
 0 .191.178.348.398.348zm3.723.146c.605 0
 .818.158.818.158l.134-.768c-.405-.102-2.343-.479-2.782 1.463-.264
 1.52 1.343 1.438 1.343 1.438s.634 0
 1.176-.244l.189-1.09-.885-.003-.1.6s-.55.147-.753-.265c-.077-.152-.025-.449-.025-.449s.117-.84.885-.84zm3.21
 1.032l-.21 1.209h-.788l.055-.315s-.26.366-.706.366c-.65
 0-.52-.655-.52-.655s.053-.561.752-.679l.646-.071s.079-.241-.303-.241-.763.207-.763.207l.1-.577s.516-.187.995-.163c1.01.005.742.919.742.919zm-.84.258s-.158.033-.3.045c-.225.034-.253.182-.257.203-.038.22.196.19.196.19s.248.009.338-.31zm4.29-1.178c-.512
 0-.766.364-.766.364s-.098-.364-.57-.364c-.471
 0-.756.376-.756.376l.056-.321h-.87l-.361
 2.074h.87l.209-1.201s.07-.293.303-.293c.232 0 .176.297.176.297l-.208
 1.197h.872l.207-1.193s.058-.301.301-.301c.244 0 .174.309.174.309l-.21
 1.184h.878l.241-1.388c0 .001.133-.74-.546-.74zm4.414-.417c0
 .02.01.297-.483.382-.858.11-.96.575-.97.63-.012.055.005.163-.032.35a50.196
 50.196 0 0
 0-.06.394H20.62s.041.293.412.293.63-.116.63-.116l-.087.536s-.26.134-.828.134c-.09
 0-1.115-.002-.926-1.091.091-.524.557-1.095
 1.368-1.095.38-.002.4.133.767.133.31-.008.57-.305.57-.305s.094-.15.17-.32c.06-.082.168-.258.514-.222.29.053.29.277.29.297zm-2.47.946c-.27
 0-.333.357-.333.357h.53s.074-.357-.197-.357zm2.792-1.523a.179.179 0 1
 0 0 .358.179.179 0 0 0 0-.358z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.codingame.com/work/press/press-ki'''

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
