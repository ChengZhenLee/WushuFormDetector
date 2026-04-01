import numpy as np
import numpy.typing as npt
from constants import constants


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


def checkAngle(angle: float, targetAngle: float, tolerance: float=constants.DEGREE_TOLERANCE) -> bool:
    """
        Check if an angle is a right angle
    """
    return abs(angle - targetAngle) < tolerance


def isLevel(point1: npt.ArrayLike, point2: npt.ArrayLike, tolerance: float=constants.DEGREE_TOLERANCE) -> bool:
    """
        Check if two points are on the same y-level
    """
    # Converts inputs to numpy arrays
    p1: npt.ArrayLike = np.array(point1)
    p2: npt.ArrayLike = np.array(point2)

    # Get the absolute difference of the y-coordinates
    diff: float = abs(p1[1] - p2[1])

    return abs(diff) < tolerance


def isVertical(point1: npt.ArrayLike, point2: npt.ArrayLike, tolerance: float=constants.DEGREE_TOLERANCE) -> bool:
    """
        Check if two points are on the same x-level
    """
    # Converts input to numpy arrays
    p1: npt.ArrayLike = np.array(point1)
    p2: npt.ArrayLike = np.array(point2)

    # Get the absolute difference of the x-coordinates
    diff: float = abs(p1[0] - p2[0])

    return abs(diff) < tolerance


def isStraight(points: list[npt.ArrayLike], tolerance: float=constants.COG_TOLERANCE) -> bool:
    """
        Check for straightness by how much intermediate points drift from the line
        formed by the first and last points
    """
    # Convert the start and end into an numpy array
    start: npt.ArrayLike = np.array(points[0])
    end: npt.ArrayLike = np.array(points[1])

    # Vector of the ideal line
    lineVector: npt.ArrayLike = start - end
    lineMagnitude: float = float(np.linalg.norm(lineVector))

    # The points are the same
    if lineMagnitude == 0: return True

    errors: list[float] = []
    # Check all intermediate points
    for point in points[1:-1]:
        # Cross product is the area of parallelogram
        # Distnace (height) = area / base (magnitude of start to end vector)
        p: npt.ArrayLike = np.array(point)
        distance: float = float(np.abs(np.cross(lineVector, p)) / lineMagnitude)
        errors.append(distance)
        
    return max(errors) < tolerance