import numpy as np
import numpy.typing as npt


def calculateAngle(point1: npt.ArrayLike, hinge: npt.ArrayLike, point2: npt.ArrayLike) -> float:
    """
        Calculate the angle between the 2 vectors around the hinge.
    """
    # Convert inputs to numpy arrays
    p1: npt.ArrayLike = np.array(point1)
    h: npt.ArrayLike = np.array(hinge)
    p2: npt.ArrayLike = np.array(point2)

    # Vectors
    h_p1: npt.ArrayLike = p1 - h
    h_p2: npt.ArrayLike = p2 - h

    # Calculate the norms
    norm_h_p1: float = float(np.linalg.norm(h_p1))
    norm_h_p2: float = float(np.linalg.norm(h_p2))

    # Calculate the cosine
    cosine_angle: float = np.dot(h_p1, h_p2) / (norm_h_p1 * norm_h_p2)

    # Get the angle in radians
    angle: float = np.arccos(np.clip(cosine_angle, -1.0, 1.0))

    return angle


def checkLevel(point1: npt.ArrayLike, point2: npt.ArrayLike, tolerance: float=0.05) -> bool:
    """
        Check if two points are on the same y-level
    """
    # Converts inputs to numpy arrays
    p1: npt.ArrayLike = np.array(point1)
    p2: npt.ArrayLike = np.array(point2)

    # Get the absoluate difference of the y-coordinates
    diff: float = abs(p1[1] - p2[1])

    return abs(diff) < tolerance