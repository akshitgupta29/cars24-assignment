from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from models import PredictionResponse

model = tf.keras.models.load_model(r'model.keras')

app = FastAPI()



@app.post("/predict")
async def predict (file: UploadFile):
    try:
        # reading the files using fastapi
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('L')

        # resizing the image and normalizing the image
        image = image.resize((28,28))
        image_array = np.array (image).reshape (1,28,28,1)/255.0

        # prediction of the models
        prediction = model.predict(image_array)
        print (np.argmax(prediction))
        
        #return the prediction
        return {"prediction": int (np.argmax(prediction)) }
    except Exception as e:
        raise HTTPException (status_code=500, detail = str(e))

@app.get ("/")
async def health():
    return {"status" : "ok"}




