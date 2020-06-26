import os

import click
import dlib


@click.command()
@click.option('--image',
              help='Path to the image to be cropped.',
              required=True)
@click.option('--verbose/--non-verbose',
              help='Command should output the matches.',
              default=False)
def detect(image: str, verbose: bool = False):
    """Detects faces on a given image using dlib and returns matches.

    :param image: Path to access the image to be searched
    :type image: [string]
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
            f"Detection {index}:\n Left: {detection.left()}\n Top: {detection.top()}\n Right: {detection.right()}\n Bottom: {detection.bottom()}\n Detection height: {height}px\n Detection width: {width}px\n Detection area: {height * width}px"
        )
    return detections
