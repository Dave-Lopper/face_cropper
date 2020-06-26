import dlib


def detect(image: str, verbose: bool = False):
    """Detects faces on a given image using dlib and returns matches.

    :param image: Path to access the image to be searched
    :type image: [string]
    :param verbose: Wether or not command should output informations
    :type image: [bool], default to False

    :return: The detected faces
    :rtype: [list of dlib.rectangle]
    """
    detector = dlib.get_frontal_face_detector()
    img = dlib.load_rgb_image(image)
    dets = detector(img, 1)
    verbose and print(f"Number of faces detected: {len(dets)}")
    detections = []
    for index, detection in enumerate(dets):
        height = detection.bottom() - detection.top()
        width = detection.right() - detection.left()
        detections.append(detection)
        verbose and print(
            f"""Detection {index}:
  Coordinates:
    Left: {detection.left()}
    Right: {detection.right()}
    Top: {detection.top()}
    Bottom: {detection.bottom()}
  Dimensions:
    Detection height: {height}px
    Detection width: {width}px
    Detection area: {height * width}px"""
        )
    return detections
