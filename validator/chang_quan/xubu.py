import numpy as np
import numpy.typing as npt
from utils import constants
import validator.base_stance as base_stance


def _checkCOG(neck: npt.ArrayLike, backAnkle: npt.ArrayLike) -> bool:
    x_drift = np.array(neck)[0] - np.array(backAnkle)[0]
    z_drift = np.array(neck)[2] - np.array(backAnkle)[2]

    return np.sqrt(x_drift**2 + z_drift**2) < constants.COG_TOLERANCE


def _validateXuBu(neck: npt.ArrayLike,
                frontHip: npt.ArrayLike, backHip: npt.ArrayLike,
                frontKnee: npt.ArrayLike, backKnee: npt.ArrayLike,
                frontAnkle: npt.ArrayLike, backAnkle: npt.ArrayLike) -> bool:
    """
        Internal master logic to validate a Chang Quan Xu Bu
    """
    # Check that the back thigh is level
    backThighLevel: bool = base_stance.isLevel(backHip, backKnee)

    # Center of gravity on the back leg
    centerOnBack: bool = _checkCOG(neck, backAnkle)

    # Front leg is extended
    isExtended: bool = base_stance.isExtended(frontAnkle, frontKnee, frontHip, constants.MIN_EXTENDED_ANGLE)

    return backThighLevel and centerOnBack and isExtended


def validateLeftXuBu(neck: npt.ArrayLike,
                     leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                     leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike,
                     leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike):
    """
        Validate the left-side Chang Quan Xu Bu
    """
    return _validateXuBu(neck,
                         rightHip, leftHip,
                         rightKnee, leftKnee,
                         rightAnkle, leftAnkle)


def validateRightXuBu(neck: npt.ArrayLike,
                     leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                     leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike,
                     leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike):
    """
        Validate the right-side Chang Quan Xu Bu
    """
    return _validateXuBu(neck,
                         leftHip, rightHip,
                         leftKnee, rightKnee,
                         leftAnkle, rightAnkle)