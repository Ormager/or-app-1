import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("Canny Edge Detection App")
    st.write("Upload an image to apply the Canny filter.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert to numpy array
        image_np = np.array(image)

        # Convert to grayscale
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

        st.write("Adjust Canny Edge Detection parameters:")

        # Slider for threshold values
        threshold1 = st.slider("Threshold 1", 0, 255, 100)
        threshold2 = st.slider("Threshold 2", 0, 255, 200)

        # Apply Canny Edge Detection
        edges = cv2.Canny(gray_image, threshold1, threshold2)

        # Display the result
        st.image(edges, caption="Canny Edge Detection", use_column_width=True, channels="GRAY")

if __name__ == "__main__":
    main()
