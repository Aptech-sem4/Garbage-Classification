from flask import Blueprint, render_template, jsonify
import os, numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from flask import current_app
from app import MODEL_PATH

mymodel = load_model(MODEL_PATH)

# Function to preprocess a single image for prediction
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to make predictions on a single image
def predict_single_image(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = mymodel.predict(preprocessed_img)
    predicted_class = np.argmax(prediction)
    return predicted_class

    
def process_image(filename):
    # Lấy đường dẫn tuyệt đối của file hiện tại
    print('vao neeeeeeeeeeee')
    folder_name = '/static/uploads'
    root_path = current_app.root_path
    
    absolute_path = root_path + folder_name
    file_path = os.path.join(absolute_path, filename)

    predicted_class = predict_single_image(file_path)

    # img = image.load_img(file_path, target_size=(224, 224))
    # img_array = image.img_to_array(img)
    # img_array = np.expand_dims(img_array, axis=0)
    # img_array /= 255

    # predictions = mymodel.predict(img_array)

    # y_pred = np.argmax(predictions, axis=1)
    # target_names = classes
    # Decode prediction
    # decoded_predictions = EfficientNetB0.decode_predictions(predictions)
    
    # Process decoded predictions to get the top result
    # top_prediction = decoded_predictions[0][0]  # Lấy kết quả dự đoán hàng đầu
    print(predicted_class)
    return predicted_class
    # pass
