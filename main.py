from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Map each plant type to its model path and class names
MODEL_INFO = {
    "Potato": {
        "model_path": "./models/potato",
        "classes": ["Early Blight", "Late Blight", "Healthy"]
    },
    "Tomato": {
        "model_path": "./models/tomato",
        "classes": ["Early blight", "Late blight", "Healthy"]
    },
    "Bell Pepper": {
        "model_path": "./models/bell_pepper",
        "classes": ["Bacterial spot", "Healthy"]
    },
    "Apple": {
        "model_path": "./models/apple",
        "classes": ['Apple scab','Black rot','Cedar apple rust','Healthy']
    },
    "Corn": {
        "model_path": "./models/corn",
        "classes": ['Cercospora leaf spot (Gray leaf spot)','Common rust','Northern Leaf Blight','Healthy']
    },
    "Grapes": {
        "model_path": "./models/grape",
        "classes": ['Black rot','Esca (Black_Measles)','Leaf_blight (Isariopsis_Leaf_Spot)','Healthy']
    }
}

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).resize((256, 256)))  # Resize to model's input size
    return image

@app.post("/predict")
async def predict(
    plant: str,  # Expect the plant name from the frontend
    file: UploadFile = File(...)
):
    if plant not in MODEL_INFO:
        return {"error": "Invalid plant type"}

    # Load the model dynamically
    model_path = MODEL_INFO[plant]["model_path"]
    class_names = MODEL_INFO[plant]["classes"]
    model = tf.keras.models.load_model(model_path)

    # Preprocess the image
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # Make predictions
    predictions = model.predict(img_batch)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        "class": predicted_class,
        "confidence": float(confidence),
        'plant':plant
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
