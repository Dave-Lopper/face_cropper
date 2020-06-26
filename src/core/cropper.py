import os
import sys

import click
from PIL import Image

from .. import THRESHOLD_IMAGE_SIZE
from .detector import detect
from .selector import select


@click.command()
@click.option(
    '--image_path',
    help='Path to the image to be cropped.',
    required=True
)
@click.option(
    '--saving_path',
    help='If provided, cropped image will be saved in the provided location',
    default=None
)
@click.option(
    '--verbose/--non-verbose',
    help='Command should output informatio.',
    default=False
)
def crop(image_path: str, saving_path: str = None, verbose: bool = False):
    """Crops an image to the largest face on it.

    :param image_path: Path to access the image to be cropped
    :type image_path: str
    :param saving_path: Path to save the cropped image, defaults to None
    :type saving_path: str, optional
    :param verbose: [description], defaults to False
    :type verbose: bool, optional

    :return: The cropped image
    :rtype: [PIL.Image.Image]
    """
    try:
        detections = detect(image_path, verbose)
    except RuntimeError:
        sys.exit("File not found : please check on the provided image path.")
    if len(detections) == 0:
        sys.exit("No face has been detected on the provided image.")

    selected_detection = select(detections, verbose)
    if selected_detection is None:
        sys.exit(
            f"The face has to be less than {THRESHOLD_IMAGE_SIZE}px * {THRESHOLD_IMAGE_SIZE}px maximum"
        )

    cropping_coordinates = (
        selected_detection.left(),
        selected_detection.top(),
        selected_detection.right(),
        selected_detection.bottom()
    )

    with Image.open(image_path) as non_cropped_image:
        cropped_image = non_cropped_image.crop(cropping_coordinates)
        filepath = os.path.basename(non_cropped_image.filename)
        filename, extension = os.path.splitext(filepath)
        if saving_path is not None:
            try:
                cropped_image.save(
                    os.path.join(
                        saving_path,
                        f"{filename}_cropped{extension}"
                    )
                )
            except FileNotFoundError:
                sys.exit(
                    "Folder not found : please check on the provided saving path."
                )
        return cropped_image
