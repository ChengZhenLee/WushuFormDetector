import numpy as np
import numpy.typing as npt


def calculateMagnitude(vector: npt.ArrayLike) -> float:
    """
        Calculate the magnitude of a vector
    """
    return float(np.linalg.norm(vector))


def calculateAngle(point1: npt.ArrayLike, hinge: npt.ArrayLike, point2: npt.ArrayLike) -> float:
    """
        Calculate the angle between the 2 vectors around the hinge.
        Returns the angle in degrees
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

    # Convert the angle to degrees
    angleDeg: float = np.degrees(angle)

    return angleDeg