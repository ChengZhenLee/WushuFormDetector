import numpy as np
import numpy.typing as npt
import utils.constants as constants
import utils.base_math as base_math


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


def isWithinAngleRange(start: npt.ArrayLike, hinge: npt.ArrayLike, end: npt.ArrayLike, 
                       minAngle: float, maxAngle: float) -> bool:
    """
        Check if the angle at the hinge is the target angle
    """
    # Get the angle around the hinge
    angle = base_math.calculateAngle(start, hinge, end)

    return minAngle <= angle <= maxAngle


def isExtended(start: npt.ArrayLike, hinge: npt.ArrayLike, end: npt.ArrayLike, 
               minAngle: float=constants.MIN_EXTENDED_ANGLE) -> bool:
    """
    """
    # Get angle around the hinge
    angle = base_math.calculateAngle(start, hinge, end)

    return angle > minAngle


def isCompressed(start: npt.ArrayLike, hinge: npt.ArrayLike, end: npt.ArrayLike,
                 factor: float = constants.COMPRESSION_FACTOR) -> bool:
    """
    Generic check: Is the distance between 'start' and 'end' 
    significantly shorter than the segment 'start-to-hinge'?
    """
    # Magnitude of the first segment
    segment_length = base_math.calculateMagnitude(np.array(start) - np.array(hinge))
    
    # Direct distance between the two extremities
    fold_distance = base_math.calculateMagnitude(np.array(start) - np.array(end))

    return fold_distance < segment_length * factor