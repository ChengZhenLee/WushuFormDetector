import numpy as np
import numpy.typing as npt
from constants import constants
import base_math


def _validatePuBu(compressedHip: npt.ArrayLike, stretchedHip: npt.ArrayLike,
                  compressedKnee: npt.ArrayLike, stretchedKnee: npt.ArrayLike,
                  compressedAnkle: npt.ArrayLike, stretchedAnkle: npt.ArrayLike):
    """
        Internal master logic to validate a Chang Quan Pu Bu
    """
    # Check if the compressed leg is compressed
    thighLength: float = base_math.calculateMagnitude(np.array(compressedHip) - np.array(compressedKnee))
    hipAnkleLength: float = base_math.calculateMagnitude(np.array(compressedHip) - np.array(compressedAnkle))

    compressed: bool = hipAnkleLength < (thighLength * constants.COMPRESSION_FACTOR)

    # Check if the stretched leg is straight
    legStraight: bool = base_math.isStraight([stretchedHip, stretchedKnee, stretchedAnkle])

    # Check if the stretched leg is level
    legLevel: bool = base_math.isLevel(stretchedHip, stretchedAnkle)

    return compressed and legStraight and legLevel


def validateLeftPuBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                    leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                    leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike):
    """
        Validate the left-side Chang Quan Pu Bu
    """
    return _validatePuBu(rightHip, leftHip,
                         rightKnee, leftKnee,
                         rightAnkle, leftAnkle)


def validateRightPuBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                    leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                    leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike):
    """
        Validate the right-side Chang Quan Pu Bu
    """
    return _validatePuBu(leftHip, rightHip,
                         leftKnee, rightKnee,
                         leftAnkle, rightAnkle)