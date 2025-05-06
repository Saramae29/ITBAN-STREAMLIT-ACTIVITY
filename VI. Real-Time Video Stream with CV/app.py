import streamlit as st
import cv2
import time

st.title("🎥 Real-Time Webcam Stream using OpenCV")
st.write("This app captures and displays real-time video from your webcam using OpenCV and Streamlit.")

# Start video capture
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Create a placeholder for the video frames
frame_window = st.image([])

# Start streaming
st.info("Press `Stop` above to end the stream.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to capture video.")
        break

    # Convert BGR to RGB for Streamlit display
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Show the frame
    frame_window.image(frame)

    # Small delay to reduce CPU usage
    time.sleep(0.03)

# Release the capture when done
cap.release()
