"""
The Blender interpolate module

"""

import typing
import collections.abc
import typing_extensions

def poly_3d_calc(veclist, pt):
    """Calculate barycentric weights for a point on a polygon.

    :param veclist: Sequence of 3D positions.
    :param pt: 2D or 3D position.   :type pt: Sequence[float]   :return: list of per-vector weights.
    """
