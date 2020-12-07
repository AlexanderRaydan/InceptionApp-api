import tensorflow as tf
import keras 
import numpy as np
import matplotlib.pyplot as plt
import urllib
import urllib.request as request

from keras.applications.inception_v3 import InceptionV3 , decode_predictions
from keras import backend as K
from PIL import Image
from keras.preprocessing import image as keras_image


from api.models import InceptionImageModel


def interception(image:InceptionImageModel):

    iv3 = InceptionV3()
    URL = 'http://localhost:8000/images/' + str(image.image)
    IMAGE_PATH = './media/temp/temp.png'


    with urllib.request.urlopen(URL) as url:
        with open(IMAGE_PATH, 'wb') as f:
            f.write(url.read())

    img = Image.open(IMAGE_PATH)
    img = img.resize([299, 299])
    x = keras_image.img_to_array(img)

    #cambio de rando
    x /=255
    x -= 0.5
    x *=2

    #redimencion
    x = x.reshape(1 , x.shape[0] ,  x.shape[1] ,  x.shape[2])
    x.shape

    y = iv3.predict(x)

    predict = decode_predictions(y)[0][0]
    name = predict[1]
    percentage = predict[2]

    return name , percentage

