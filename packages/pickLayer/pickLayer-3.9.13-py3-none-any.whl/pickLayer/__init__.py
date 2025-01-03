# noqa: N999
#  Copyright (C) 2014-2019 Enrico Ferreguti (enricofer@gmail.com)
#  Copyright (C) 2021-2023 National Land Survey of Finland
#  (https://www.maanmittauslaitos.fi/en).
#
#
#  This file is part of PickLayer.
#
#  PickLayer is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PickLayer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PickLayer. If not, see <https://www.gnu.org/licenses/>.


def classFactory(iface):  # noqa: ANN201, ANN001, N802
    """Load pickLayer class from file picklayer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from pickLayer.plugin import Plugin

    return Plugin()
