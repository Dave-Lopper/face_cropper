import click

from ..core.cropper import crop


@click.command(name="crop")
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
def crop_command(
        image_path: str,
        saving_path: str = None,
        verbose: bool = False):
    """Calls crop function from CLI.

    :param image_path: Path to access the image to be cropped
    :type image_path: str
    :param saving_path: Path to save the cropped image, defaults to None
    :type saving_path: str, optional
    :param verbose: [description], defaults to False
    :type verbose: bool, optional
    """
    crop(image_path, saving_path, verbose)
