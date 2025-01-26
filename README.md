# Plant Disease Classifier

## Overview
The **Plant Disease Classifier** is an AI-powered tool that helps farmers and gardeners diagnose diseases in plants by analyzing images. This project uses machine learning models to classify plant health, making it easier to detect diseases early and take corrective measures. The tool supports different plant types, including **Potato**, **Tomato**, and **Bell Pepper**, and provides confidence levels for the disease classification.

## Features
- **Drag and Drop Image Upload**: Users can drag and drop images of plant leaves for analysis.
- **Plant Type Selection**: Users can select the plant type (Potato, Tomato, Bell Pepper) before uploading an image.
- **Real-time Predictions**: The app makes predictions about plant health using pre-trained models for each plant type.
- **Confidence Score**: The result includes a confidence percentage for the predicted disease classification.

## Screenshots

<div style="display: flex; justify-content: center;  width: 100%;">
    <img src="https://github.com/user-attachments/assets/e61c3626-548c-4ee1-bbb4-9c1650daa49b" width="60%" />
</div>

<div style="display: flex; justify-content: space-between; width: 100%; padding: 0 10%;">
    <img src="https://github.com/user-attachments/assets/caa068cb-a534-4bae-9729-3f238df84ae9" width="45%" />
    <img src="https://github.com/user-attachments/assets/393ea454-abf2-4182-8f31-eda3f5087984" width="45%" />
</div>


## Technologies Used
- **Frontend**:
  - HTML, CSS, and JavaScript for building the user interface.
  - Fetch API for communicating with the backend.
  - FileReader for image preview functionality.
  
- **Backend**:
  - **FastAPI** for creating the backend API.
  - **TensorFlow/Keras** for loading pre-trained machine learning models.
  - **PIL** (Python Imaging Library) for image preprocessing.

- **Model**:
  - Pre-trained models for Potato, Tomato, and Bell Pepper diseases.
  - Each model predicts diseases such as Early Blight, Late Blight, and Healthy status for potatoes, and Bacterial Spot for Bell Peppers.

## Installation

### Prerequisites
- Python 3.8.20
- TensorFlow
- FastAPI
- Uvicorn
- PIL (Pillow)

### Setup

1. Clone this repository to your local machine
2. Install the required dependencies
3. Run the FastAPI server: uvicorn main:app --reload
4. Open the app(index.html) in your browser: Navigate to http://localhost:8000 to start using the tool.
