import sys

import click

from .. import THRESHOLD_IMAGE_SIZE
from .detector import detect
from .selector import select


@click.command()
@click.option(
    '--image',
    help='Path to the image to be cropped.',
    required=True
)
@click.option(
    '--verbose/--non-verbose',
    help='Command should output the matches.',
    default=False
)
def crop(image: str, verbose: bool):
    detections = detect(image, verbose)
    if len(detections) == 0:
        sys.exit("No face has been detected on the provided image.")

    selected_detection = select(detections, verbose)
    if selected_detection is None:
        sys.exit(
            f"The face has to be less than {THRESHOLD_IMAGE_SIZE}px x {THRESHOLD_IMAGE_SIZE}px maximum"
        )
