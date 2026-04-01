import numpy.typing as npt
import utils.constants as constants
import validator.base_stance as base_stance


def _validatePuBu(compressedHip: npt.ArrayLike, stretchedHip: npt.ArrayLike,
                  compressedKnee: npt.ArrayLike, stretchedKnee: npt.ArrayLike,
                  compressedAnkle: npt.ArrayLike, stretchedAnkle: npt.ArrayLike):
    """
        Internal master logic to validate a Chang Quan Pu Bu
    """
    # Check if the compressed leg is compressed
    compressed: bool = base_stance.isCompressed(compressedAnkle, compressedKnee, compressedHip,
                                                constants.COMPRESSION_FACTOR)

    # Check if the stretched leg is straight
    legStraight: bool = base_stance.isStraight([stretchedHip, stretchedKnee, stretchedAnkle])

    # Check if the stretched leg is level
    legLevel: bool = base_stance.isLevel(stretchedHip, stretchedAnkle)

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