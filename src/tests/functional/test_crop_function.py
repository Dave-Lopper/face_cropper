import os
from pathlib import Path
from PIL import Image
import pytest

from src import DLIB_FACE_DETECTING_MIN_SCORE
from src.core.cropper import crop
from src.exceptions import NoFaceException, InvalidSavingPathException


def test_crop_function_crops_adequatly():
    cropped = crop(
        os.path.join(
            Path(__file__).parent.absolute(),
            "../samples/child.jpeg"
        )
    )
    expected = Image.open(os.path.join(
        Path(__file__).parent.absolute(),
        "../samples/child_cropped.jpeg")
    )
    assert cropped.size == expected.size


def test_crop_function_saves_adequatly():
    crop(
        image_path=os.path.join(
            Path(__file__).parent.absolute(),
            "../samples/mark_zuckerberg.jpeg"
        ),
        saving_path=os.path.join(
            Path(__file__).parent.absolute(),
            "../samples"
        )
    )
    assert os.path.isfile(
        os.path.join(
            Path(__file__).parent.absolute(),
            "../samples/mark_zuckerberg_cropped.jpeg"
        )
    )


def test_crop_function_crops_noface_raises_noface_exception():
    with pytest.raises(NoFaceException) as exception:
        crop(
            os.path.join(
                Path(__file__).parent.absolute(),
                "../samples/no_face.jpeg"
            )
        )
        assert exception.message == f"No face has been detected on the provided image.\nIf you are sure there is one, try adjusting the precision score from dlib\nCurrent minimum score: {DLIB_FACE_DETECTING_MIN_SCORE}"


def test_crop_function_crops_with_unexisting_file_raises_filenotfounderror():
    with pytest.raises(FileNotFoundError) as exception:
        crop(
            os.path.join(
                Path(__file__).parent.absolute(),
                "../samples/unexisting_image.jpeg"
            )
        )
        assert exception.message == "File not found : please check on the provided image path."


def test_crop_function_crops_with_unexisting_saving_path_raises_invalid_savingpath_exception():
    with pytest.raises(InvalidSavingPathException) as exception:
        crop(
            image_path=os.path.join(
                Path(__file__).parent.absolute(),
                "../samples/child.jpeg"
            ),
            saving_path=os.path.join(
                Path(__file__).parent.absolute(),
                "../unexisting_folder"
            )
        )
        assert exception.message == "Folder not found : please check on the provided saving path."
