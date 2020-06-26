from .. import THRESHOLD_IMAGE_SIZE


def select(detections: list, verbose: bool = False):
    """Selects biggest face detection.

    Check on detections size,
    Keeps the compliant ones (under the threshold),
    Returns None if no detection is compliant.
    Returns the biggest. (With the biggest area)

    :param detections: List of detected faces on the provided image
    :type detections: [list of dlib.rectangle]
    :param verbose: Wether or not command should output informations
    :type verbose: [bool], default to False

    :return: The biggest face detected
    :rtype: [dlib.rectangle], None if no image under our threshold size
    """
    filtered_detections = list(
        filter(
            lambda x:
                x.bottom() -
                x.top() <= THRESHOLD_IMAGE_SIZE and
                x.right() -
                x.left() <= THRESHOLD_IMAGE_SIZE,
            detections
        )
    )
    if len(filtered_detections) == 0:
        return None
    sorted_detections = list(
        sorted(
            filtered_detections,
            key=lambda x: (x.bottom() - x.top()) * (x.right() - x.left()),
            reverse=True
        )
    )
    if verbose:
        print()
        print(
            f"""The biggest face on the provided image:
  Dimensions:
    Height: {sorted_detections[0].bottom() - sorted_detections[0].top()}px
    Width: {sorted_detections[0].right() - sorted_detections[0].left()}px
  Coordinates:
    Top: {sorted_detections[0].top()}
    Bottom: {sorted_detections[0].bottom()}
    Left: {sorted_detections[0].left()}
    Right: {sorted_detections[0].right()}"""
        )
    return sorted_detections[0]
