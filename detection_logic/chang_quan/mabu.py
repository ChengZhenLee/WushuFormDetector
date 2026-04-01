import numpy.typing as npt
import base_math


def validateMaBu(leftHip: npt.ArrayLike, rightHip: npt.ArrayLike,
                leftKnee: npt.ArrayLike, rightKnee: npt.ArrayLike, 
                leftAnkle: npt.ArrayLike, rightAnkle: npt.ArrayLike) -> bool:
    """
        Validate a Chang Quan Ma Bu
    """
    # Check if the thighs are level
    leftThighLevel: bool = base_math.isLevel(leftHip, leftKnee)
    rightThighLevel: bool = base_math.isLevel(rightHip, rightKnee)

    # Check if the hips are level
    hipLevel: bool = base_math.isLevel(leftHip, rightHip)

    # Check if the legs form a square structure
    leftAngle: float = base_math.calculateAngle(leftAnkle, leftKnee, leftHip)
    rightAngle: float = base_math.calculateAngle(rightAnkle, rightKnee, rightHip)
    
    isSquare: bool = base_math.checkAngle(leftAngle, 90) and base_math.checkAngle(rightAngle, 90)

    return leftThighLevel and rightThighLevel and hipLevel and isSquare