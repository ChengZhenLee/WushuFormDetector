import numpy.typing as npt
import utils.chang_quan as chang_quan
import validator.base_stance as base_stance


def _validateGongBu(frontHip: npt.ArrayLike, backHip: npt.ArrayLike,
                    frontKnee: npt.ArrayLike, backKnee: npt.ArrayLike, 
                    frontAnkle: npt.ArrayLike, backAnkle: npt.ArrayLike) -> bool:
    """
        Internal master logic to validate a Chang Quan Gong Bu
    """
    # Check if the front thigh is level
    frontThighLevel: bool = base_stance.isLevel(frontHip, frontKnee)

    # Check if the front leg forms a right angle
    isSquare = base_stance.isWithinAngleRange(
            frontHip, frontKnee, frontHip,
            chang_quan.MIN_ANGLE, chang_quan.MAX_ANGLE)

    # Check if the back leg is straight
    backLegStraight: bool = base_stance.isStraight([backHip, backKnee, backAnkle])

    return frontThighLevel and isSquare and backLegStraight


def validateLeftGongBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                    leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                    leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike) -> bool:
    """
        Validate the left-side Chang Quan Gong Bu
    """
    return _validateGongBu(leftHip, rightHip,
                           leftKnee, rightKnee,
                           leftAnkle, rightAnkle)


def validateRightGongBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                        leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                        leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike) -> bool:
    """
        Validate the right-side Chang Quan Gong Bu
    """
    return _validateGongBu(rightHip, leftHip,
                           rightKnee, leftKnee,
                           rightAnkle, leftAnkle)