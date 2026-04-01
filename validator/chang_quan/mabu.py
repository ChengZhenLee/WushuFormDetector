import numpy.typing as npt
import utils.chang_quan as chang_quan
import validator.base_stance as base_stance


def validateMaBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike) -> bool:
    """
        Validate a Chang Quan Ma Bu
    """
    # Check if the thighs are level
    leftThighLevel: bool = base_stance.isLevel(leftHip, leftKnee)
    rightThighLevel: bool = base_stance.isLevel(rightHip, rightKnee)

    # Check if the hips are level
    hipLevel: bool = base_stance.isLevel(leftHip, rightHip)

    # Check if the legs form a square structure
    leftIsSquare: float = base_stance.isWithinAngleRange(
        leftAnkle, leftKnee, leftHip, 
        chang_quan.MIN_ANGLE, chang_quan.MAX_ANGLE)
    
    rightIsSquare: float = base_stance.isWithinAngleRange(
        rightAnkle, rightKnee, rightHip, 
        chang_quan.MIN_ANGLE, chang_quan.MAX_ANGLE)
    
    return leftThighLevel and rightThighLevel and hipLevel and leftIsSquare and rightIsSquare