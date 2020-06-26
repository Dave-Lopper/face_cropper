import os

import click


@click.command()
@click.option('--image',
              help='Path to the image to be cropped.',
              required=True)
def crop(image):
    """"""
    print(image)
