import tensorflow as tf
from tensorflow.keras.applications import ResNet50, InceptionV3, VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input as preprocess_inception
from tensorflow.keras.applications.resnet50 import preprocess_input as preprocess_resnet
import numpy as np
import matplotlib.pyplot as plt

# Load models
resnet_model = ResNet50(weights='imagenet')
googlenet_model = InceptionV3(weights='imagenet')  # GoogLeNet in Keras is InceptionV3
vgg16_model = VGG16(weights='imagenet')

# Function to load and preprocess an image
def load_and_preprocess_image(img_path, model_type):
    img = image.load_img(img_path, target_size=(224, 224))  # All models expect 224x224 input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    if model_type == 'resnet':
        img_array = preprocess_resnet(img_array)
    elif model_type == 'googlenet':
        img_array = preprocess_inception(img_array)
    elif model_type == 'vgg16':
        img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
    
    return img_array

# Function to predict the class of the image
def predict_class(model, img_array):
    predictions = model.predict(img_array)
    predicted_class = tf.keras.applications.inception_v3.decode_predictions(predictions, top=1)[0][0][1]
    return predicted_class

# Example image path (use an actual image path for your environment)
img_path = 'image.jpg'  # Replace with an actual image path

# Preprocess image for each model
img_resnet = load_and_preprocess_image(img_path, model_type='resnet')
img_googlenet = load_and_preprocess_image(img_path, model_type='googlenet')
img_vgg16 = load_and_preprocess_image(img_path, model_type='vgg16')

# Predictions for each model
pred_resnet = predict_class(resnet_model, img_resnet)
pred_googlenet = predict_class(googlenet_model, img_googlenet)
pred_vgg16 = predict_class(vgg16_model, img_vgg16)

# Display results
print(f"Predicted Class for ResNet50: {pred_resnet}")
print(f"Predicted Class for GoogLeNet (InceptionV3): {pred_googlenet}")
print(f"Predicted Class for VGG16: {pred_vgg16}")

# Plot the image
img = image.load_img(img_path, target_size=(224, 224))
plt.imshow(img)
plt.axis('off')
plt.show()

# Print model summaries
print("\nResNet50 Model Summary:")
resnet_model.summary()

print("\nGoogLeNet (InceptionV3) Model Summary:")
googlenet_model.summary()

print("\nVGG16 Model Summary:")
vgg16_model.summary()
