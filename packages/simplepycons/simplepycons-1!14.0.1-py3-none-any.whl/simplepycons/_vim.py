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


class VimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vim"

    @property
    def original_file_name(self) -> "str":
        return "vim.svg"

    @property
    def title(self) -> "str":
        return "Vim"

    @property
    def primary_color(self) -> "str":
        return "#019733"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vim</title>
     <path d="M24 11.986h-.027l-4.318-4.318
 4.303-4.414V1.461l-.649-.648h-8.198l-.66.605v1.045L12.015.027V0L12
 .014 11.986 0v.027l-1.29
 1.291-.538-.539H2.035l-.638.692v1.885l.616.616h.72v5.31L.027
 11.987H0L.014 12 0 12.014h.027l2.706
 2.706v6.467l.907.523h2.322l1.857-1.904 4.166
 4.166V24l.015-.014.014.014v-.028l2.51-2.509h.485c.111 0
 .211-.07.25-.179l.146-.426c.028-.084.012-.172-.037-.239l1.462-1.462-.612
 1.962c-.043.141.036.289.177.332.025.008.052.012.078.012h1.824c.106-.001.201-.064.243-.163l.165-.394c.025-.065.024-.138-.004-.203-.027-.065-.08-.116-.146-.142-.029-.012-.062-.019-.097-.02h-.075l.84-2.644h1.232l-1.016
 3.221c-.043.141.036.289.176.332.025.008.052.012.079.012h2.002c.11 0
 .207-.066.248-.17l.164-.428c.051-.138-.021-.29-.158-.341-.029-.011-.06-.017-.091-.017h-.145l1.131-3.673c.027-.082.012-.173-.039-.24l-.375-.504-.003-.005c-.051-.064-.127-.102-.209-.102h-1.436c-.071
 0-.141.03-.19.081l-.4.439h-.624l-.042-.046 4.445-4.445H24L23.986
 12l.014-.014zM9.838 21.139l1.579-4.509h-.501l.297-.304h1.659l-1.563
 4.555h.623l-.079.258H9.838zm3.695-7.516l.15.151-.269.922-.225.226h-.969l-.181-.181.311-.871.288-.247h.895zM5.59
 20.829H3.877l-.262-.15V3.091H2.379l-.1-.1V1.815l.143-.154h7.371l.213.214v1.108l-.142.173H8.785v8.688l8.807-8.688h-2.086l-.175-.188V1.805l.121-.111h7.49l.132.133v1.07L12.979
 13.25h-.373c-.015-.001-.028
 0-.042.001l-.02.003c-.045.01-.086.03-.119.06l-.343.295-.004.003c-.033.031-.059.069-.073.111l-.296.83-6.119
 6.276zm14.768-3.952l.474-.519h1.334l.309.415-1.265
 4.107h.493l-.08.209H19.84l1.124-3.564h-2.015l-1.077
 3.391h.424l-.073.174h-1.605l1.107-3.548h-2.096l-1.062
 3.339h.436l-.072.209H13.27l1.514-4.46H14.198l.091-.271h1.65l.519.537h.906l.491-.554h1.061l.489.535h.953z"
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
        return '''https://commons.wikimedia.org/wiki/File:Vimlo'''

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
