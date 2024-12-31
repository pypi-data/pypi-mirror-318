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


class StrongswanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "strongswan"

    @property
    def original_file_name(self) -> "str":
        return "strongswan.svg"

    @property
    def title(self) -> "str":
        return "strongSwan"

    @property
    def primary_color(self) -> "str":
        return "#E00033"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>strongSwan</title>
     <path d="M17.803 5.24a3.161 3.161 0 0
 0-1.647.5c-.245.185-.54.52-.518
 1.165.022.32.031.294.112.58.232.433.458.622.826.94.06.047.079.06.133.099.275.258.553.556.79.823.207.256.432.54.604.825.229.392.263.369.546.928.287.645.398
 1.392.226 2.068a4.62 4.62 0 0 1-.88 1.646l.347
 1.137.303-1.115.463.003.298 1.114.34-1.112h.466l-.554
 1.662c.3-.39.528-.74.763-1.197l.409.07c.036-.093.079-.155.145-.183.04-.018.063-.032.19-.032.1-.001.216.016.253.095.013.035.028.064.023.183a3.68
 3.68 0 0 1-.436.104c-.302.059-.427.105-.521.192a.44.44 0 0
 0-.152.355c0
 .11.02.184.07.26.079.122.19.197.344.23.1.022.302.018.393-.008a.86.86
 0 0 0 .27-.138l.07-.053.056.173h.482l-.015-.03a1.143 1.143 0 0
 1-.075-.22c-.012-.054-.014-.132-.015-.548
 0-.401-.003-.497-.014-.552-.022-.112-.04-.16-.102-.216a.46.46 0 0
 0-.257-.14 1.74 1.74 0 0 0-.494-.025c-.216.018-.42.11-.49.22 0 .002 0
 .002-.002.003.734-1.491
 1.002-3.19.274-4.696-.42-.92-1.036-1.522-1.751-2.102.71.009 1.367.094
 2.033.02.167-.012.3-.02.455-.056a.624.624 0 0 1
 .318-.073c.335-.116.376-.214.379-.292-.021-.181-.335-.323-.487-.393l-.96.202c-.057-.04-.835-.292-.83-.595.003-.122.13-.138.16-.433l.001-.263-.058-.298c-.063-.082-.425-.313-.626-.421-.241-.12-.386-.19-.562-.235a3.181
 3.181 0 0 0-1.096-.171zm-6.332.657c-1.667-.01-3.283.509-4.457
 1.83-.55.579-1.06 1.274-1.458 1.923.396.083.697.186
 1.165.32.438.097.78.378
 1.082.488l.09-.048c-1.001-.5-.685-.4-.284-.266.723.654 1.823.52 2.545
 1.162l.243.14c.113-.04-.322-.275-.248-.282l.063.004c-.022-.001-.862-.533-.795-.53-.085-.145-.267-.225-.358-.308.227.073.587.375.732.428l.074-.063c.033-.029.005.135.141.165l.1-.165c.017-.026.087.146.131.157.03.008.004-.061.074-.111-.123-.079-.14-.075-.26-.138-.154-.029-.183-.042-.459-.238.29-.024.326.09.46.15.44.126.9.28
 1.274.562l.033-.04c.017-.02.546.385.51.35l.065-.083c.012-.015.132.172.142.161l.06-.067c.252.226.276.377.528.551.16.075.54.373.79.528.505.45.711.64-.029.077-.166-.093-.617-.525-.528-.161.166.125.671.372.446.387.008.004.039.076.375.265.143.081.447.298.447.298l.014-.025.176.16c-.012-.012-.127-.013-.188-.022-.282-.22-.27-.194-.296-.193-.211.236.208.156.032.3.154.084.302.212.417.327.012.122.13.19.264.317s.285.315.389.41c.846-.389
 1.315-.976
 1.551-1.524.295-.756.245-1.02.086-1.586-.178-.557-.711-1.153-1.183-1.527-.25-.223-.495-.368-.878-.655-.69-.751-.954-1.401-1.019-1.966-.076-.516.06-.998.168-1.315-.7-.07-1.452-.15-2.065-.145a7.912
 7.912 0 0 0-.162-.002zM5.556
 9.65c-.08-.014-.157-.028-.229-.03a.338.338 0 0
 0-.252.089c.13.015.26.03.398.074zm-.083.133l-.08.126c.219.023.314.015.515.04.19.05.542.15.71.207.016.013.088-.033.05-.054-.39-.174-.815-.208-1.195-.319zm-.08.126h-.169l.14.045zm-.028.045l-.031.065c.216.031.986.29
 1.045.297.043.005.063-.048.025-.065-.134-.052-.317-.096-.508-.154a5.804
 5.804 0 0
 0-.531-.143zm-.031.065c-.21-.043-.326-.098-.578-.169-.258-.106-1.13-.252-.557.03.042.098-.506-.041-.341-.095-.06.002-.98-.273-.721-.092-.392-.14-.308-.129-.365.069-.2-.123-.331-.165-.466-.166-.08
 0-.163.015-.262.037-.348-.063-.124-.019-.166.143.114.124.781.278.922.31.322.069
 1.115.315
 1.085.254-.282-.164.146.009.267.068.144.088.58.079.55.225a.353.353 0
 0 1
 .21.077c.123-.215.245-.432.422-.69zm-.528-.254c.067.07.14.053.232.078.066-.006.292-.018.336-.013-.017-.004-.23-.063-.568-.065zm-.408.075c.095.002.427.224.194.138-.243-.065-.326-.128-.21-.135a.034.034
 0 0 1
 .016-.003zm-2.675.011c-.034-.003-.056.08.119.104.054.008-.078-.093-.12-.104zm.22.07c-.03.021.03.068.363.128.274.05-.301-.129-.362-.128zm2.878.03c.04
 0
 .237.123.165.115-.236-.028-.255-.116-.165-.115zm-2.507.19c.229.144.31.17.052.134.147.097.48.15.348.306.055.027.201-.006.224.047.023.053.016.063-.101.13-.08.05-.49-.063-.683-.09-.22-.057-.376-.06-.594-.09-.468-.046-.003.087-.672.046-.545-.032-.193.11-.244.122-.1.137-.284-.069-.313-.044-.044.057-.01.187-.287.006L0
 10.862c.397-.01.522.146.597-.035.17.013.3.096.354.133.054.037-.134.11-.016.095.101-.112.172.067.24.057.044
 0
 .12-.082.17-.088.021.006.079.098.13.093.043-.004.129-.07.149-.057.389.066.488.097.556.176.252-.012.55.164.963.209.981.336-.904-.193-1.462-.16-.188.017-.872-.13-.538.058.288.127.482.255.624.159.048-.026.894.356.338.019.12.017.227-.01.326.045.303.163.47.058.565.134.277.156.474.111.698.135.126.022.411.06.476.104.114.023.067.014.212.038l.102-.267c-.671-.075-.693-.112-1.543-.368l.014-.056c.209.068.343.1.52.127l.012-.094c.09.022.47.105.489.091-.215-.094-.2-.044-.163-.114.11-.033.557.165.613.139.156-.005.123.003.162.007.154-.415.171-.38.276-.654a2.276
 2.276 0 0
 1-.245-.109c-.089.042.196.142-.306-.008-.147-.1-.125-.145-.153-.002-.054-.037-.089-.005-.339-.193-.351-.122-1.261-.338-1.507-.336zm2.274
 1.301l-.104.268c.212.02.167.005.303-.01.135-.014.471.118.621.191.088.057.095.074.363.167.147.025.574.242.876.316.036-.01.363.114.526.15.102.04.193.093.28.157.147.061.207.087.38.11.164.071-.018.024.201.117.24.123.358.242.442.267.104-.053.34-.12.38-.13-.172-.04-.438-.242-.817-.388-.623-.15-1.137-.55-1.71-.804l-.419-.113c-.038.003-.043.021-.044.05.394.123.534.162.677.235.182.16.322.185.351.221-.325-.097-.295-.085-.59-.174-.237-.078-.274-.133-.58-.227-.158-.049-.356-.166-.536-.233a2.167
 2.167 0 0 0-.6-.17zm-.206.535C3.678 13.9 3.315 14.845 1.76
 15.86c-.364.229-.778.4-1.21.427v2.467c1.51.002 3.019.001
 4.528.006-.276-2.279 1.124-4.583
 3.202-5.505-.38-.288-.39-.202-.451-.172-.248-.181-1.15-.677-1.16-.688-.1-.011-.36-.125-.398-.075-.025.055.13.072.187.084.225.041
 1.242.664
 1.32.792-.448.025-.81-.41-1.181-.505l.008-.118c-.236-.12-.415-.122-.481-.166-.08.146-1.016-.346-1.17-.341-.23.033-.213-.036-.572-.089zm.938-1.331c-.017
 0-.007.01.056.041.053.019.515.205.256.143-.168.117.425.013.244.116-.398-.111.547.306.308.07-.093-.147-.131-.088-.193-.12-.183-.093-.297-.127-.414-.178-.03-.009-.216-.07-.257-.072zm.257.072m-4.575-.052c.13
 0
 .266.01.313.014.366-.045.425.12.107.088-.03-.002-.108-.073-.233.049-.074-.009-.126-.086-.212-.104.071.1.293.142-.131.088-.258-.114-.06-.137.156-.135zm.741.033c.05-.002.111.017.128.077-.257-.015-.21-.074-.128-.077zm8.753.28l-.003.001c-.122.08.05.232.385.348-.099-.138-.042-.143-.195-.193.067.172-.15-.155-.187-.156zm-5.734.12c-.23.14.486.301.387.255-.042-.173.399.174.217-.043-.26-.058-.11-.103-.203-.096-.158.066-.295-.098-.401-.115zm-2.067.017c.005
 0
 .01.002.016.005.023.014.052.05.093.072.01.037-.029.04-.069.029-.04-.01-.081-.033-.078-.045.011-.047.023-.062.038-.062zm.845.09c.016
 0
 .048.025.095.102-.097-.004-.126-.1-.095-.101zm7.412.046c-.084.073.188.295.27.145-.136-.126.054.123-.27-.145zm-3.99.003c-.277.065-.275.007.053.197.3.138-.003.095-.126.012.004.03.25.217.22.19.118.083.454.215.32.042.12-.15-.193-.162-.194-.184a.867.867
 0 0
 1-.28-.183c-.185.014.119-.06.007-.074zm-.007.074h.004c-.004-.002-.005-.002-.004
 0zm.28.183c.028.007.048.003.055-.017-.04.007-.055.013-.055.017zm.28
 2.852v.485h-.192v.242h.192l.008
 1.018c.008.224.129.388.334.447.17.028.32.013.478-.028l-.004-.264a.733.733
 0 0
 1-.245.058c-.17-.01-.23-.035-.275-.203l-.005-1.03.53.002v-.242h-.527v-.485zm4.614.436a.7.7
 0 0 0-.459.179l-.056.045v-.175h-.293v1.689h.293v-1.259l.064-.047a.9.9
 0 0 1 .258-.136.571.571 0 0 1 .236
 0c.06.017.11.058.138.113.047.092.05.125.054.754l.004.575h.292l-.003-.625c-.003-.606-.004-.628-.022-.7-.05-.205-.167-.34-.344-.393a.725.725
 0 0 0-.162-.02zm11.251.002a.751.751 0 0 0-.306.068.896.896 0 0
 0-.228.168l-.034.039v-.237h-.444v1.715h.477l-.003-.893c-.01-.438.226-.504.398-.511.195.006.274.14.28.332-.002.358.001.715.004
 1.072H24l-.003-.65c-.003-.591-.005-.656-.018-.71a.462.462 0 0
 0-.286-.337.778.778 0 0 0-.313-.056zm-13.111 0a.901.901 0 0
 0-.198.02c-.3.082-.498.337-.54.699-.016.131-.006.355.02.468.04.173.1.284.214.399a.524.524
 0 0 0 .147.114.794.794 0 0 0
 .234.077c.08.013.265.004.345-.015a.678.678 0 0 0
 .44-.35c.076-.15.097-.247.103-.475a1.144 1.144 0 0
 0-.048-.432.694.694 0 0 0-.717-.505zm3.394.001a.67.67 0 0
 0-.477.196.688.688 0 0
 0-.176.266c-.073.18-.093.425-.053.662.05.3.21.497.444.56a.845.845 0 0
 0 .446-.02c.091-.04.154-.093.225-.148l-.002.135a1.05 1.05 0 0
 1-.018.182c-.027.11-.072.184-.163.23a.537.537 0 0
 1-.297.055c-.196-.004-.364-.073-.488-.116l-.004.307c.1.024.21.047.295.057.185.023.381.012.514-.03.256-.06.425-.299.448-.67v-1.62h-.266l-.014.07-.077-.042c-.156-.074-.264-.073-.337-.074zm-7.03.003a.79.79
 0 0 0-.213.025c-.193.057-.337.192-.38.357a.647.647 0 0 0-.013.137c0
 .15.038.247.13.333.09.085.186.118.471.177.202.042.28.078.313.177.02.175.002.215-.107.283a.726.726
 0 0
 1-.242.042c-.15.014-.372-.071-.554-.218H6.02v.32c.11.056.23.098.355.128.1.026.382.015.452-.008.149-.048.3-.15.358-.261a.453.453
 0 0 0 .06-.254c-.001-.257-.122-.39-.418-.459l-.216-.05a.583.583 0 0
 1-.23-.095c-.045-.041-.069-.136-.052-.206.015-.06.05-.098.108-.133.177-.108.498-.048.722.13h.023v-.308a1.34
 1.34 0 0 0-.337-.105 2.395 2.395 0 0 0-.21-.012zm2.676.042a.678.678 0
 0 0-.395.175l-.093.08.001-.253H8.54l.004
 1.686.285.002-.004-1.199a.915.915 0 0 1
 .251-.162c.148-.053.195-.04.363-.023v-.305h-.13zm.965.204c.051 0
 .103.007.154.022.14.044.237.162.283.343.025.1.032.37.013.482-.038.219-.14.361-.296.413a.447.447
 0 0
 1-.43-.08c-.113-.106-.163-.247-.171-.486-.01-.277.04-.463.155-.578a.421.421
 0 0 1 .292-.116zm3.42.008h.042a.802.802 0 0 1
 .336.098v.918l-.05.035a.803.803 0 0 1-.24.11.619.619 0 0 1-.28
 0c-.118-.038-.19-.122-.232-.276a1.28 1.28 0 0
 1-.03-.335c.016-.214.066-.34.174-.442a.374.374 0 0 1
 .28-.108zm3.96.105c-1.014.897-1.887 1.096-2.407 1.228.247.696.34
 1.51.289 2.245 1.596-.265 3.04-.904
 4.076-2.083l-.43-.001-.31-1.098-.299
 1.098-.46.001zm3.78.58c.007.002.007.028.004.129-.005.156-.019.204-.078.27a.455.455
 0 0
 1-.2.114c-.111.028-.212.005-.283-.065-.112-.112-.073-.274.079-.33.045-.017.08-.026.329-.083a3.467
 3.467 0 0 0 .149-.035z" />
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
