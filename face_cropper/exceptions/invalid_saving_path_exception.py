from face_cropper.core import THRESHOLD_IMAGE_SIZE


class InvalidSavingPathException(Exception):
    """Raised when the provided saving path is invalid."""

    def __init__(self):
        self.message = "Folder not found : please check on the provided saving path."
