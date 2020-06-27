
[![PyPI version](https://badge.fury.io/py/face-cropper.svg)](https://badge.fury.io/py/face-cropper)
# Face cropper

Welcome to the face cropper module !  
This module will :   
- Automatically detect faces on a provided picture
- Return the biggest one
- Save it in a location of your choosing !

### Requirements
- Python > 3.7  
- pip > 20.1.1

### Quickstart   
##### Use as a package ?
- `pip install face-cropper==1.0`    
##### Use as a CLI ?     
- Clone the repo   
- `pip install -r requirements.txt`   
- `python main.py --image_path=path\to\my\image --saving_path=where\to\save\cropped\image`   
   
     
### CLI documentation   
Just run the main.py module   
##### Required arguments :   
- image_path : The path of the image to be cropped   
- saving_path : The path where the cropped image should be saved   
##### Optionnal arguments :   
- verbose : Wether or not the command should output informations about the face
  detections   

### Module documentation
Simply import the ***crop*** function, and pass it the path of the image to be
cropped as  ***image_path*** !   
It is also possible to pass it another parameter, ***saving_path***, which if
provided will make *face_croper* save the image in the provided location !   
##### Example    
```python
import os

from face_cropper import crop

cropped_image = crop(
    image_path=os.path.join(os.getcwd(), "my_image.jpg")
)
```   
```python
import os

from face_cropper import crop

cropped_image = crop(
    image_path=os.path.join(os.getcwd(), "my_image.jpg"),
    saving_path=os.getcwd()
)
```   
