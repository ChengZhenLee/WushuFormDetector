import numpy.typing as npt
import base_math


def _validateGongBu(frontHip: npt.ArrayLike, backHip: npt.ArrayLike,
                    frontKnee: npt.ArrayLike, backKnee: npt.ArrayLike, 
                    frontAnkle: npt.ArrayLike, backAnkle: npt.ArrayLike) -> bool:
    """
        Internal master logic to validate a Chang Quan Gong Bu
    """
    # Check if the front thigh is level
    frontThighLevel: bool = base_math.isLevel(frontHip, frontKnee)

    # Check if the front leg forms a right angle
    frontAngle: float = base_math.calculateAngle(frontAnkle, frontKnee, frontHip)
    isSquare: bool = base_math.checkAngle(frontAngle, 90)

    # Check if the back leg is straight
    backLegStraight: bool = base_math.isStraight([backHip, backKnee, backAnkle])

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