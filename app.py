import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import os

# Streamlit page setup
st.set_page_config(layout="wide")
st.title("Virtual Drawing Board")

# Load button images from 'buttons/' folder
button_folder = "buttons"
button_images = {}
button_coords = {}
button_height = 100
x_start = 0

for filename in sorted(os.listdir(button_folder)):
    if filename.endswith(".png"):
        path = os.path.join(button_folder, filename)
        img = cv2.imread(path)
        img = cv2.resize(img, (100, button_height))
        name = filename.split(".")[0]
        button_images[name] = img
        button_coords[name] = (x_start, x_start + 100)
        x_start += 100

# Initial states
draw_color = (0, 0, 255)  # Default red
eraser_mode = False
selected_button = None

# Set up video capture
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Drawing canvas
canvas = None
drawn_mask = None
prev_x, prev_y = 0, 0

# Streamlit image placeholder
frame_placeholder = st.empty()

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)
        drawn_mask = np.zeros(frame.shape[:2], dtype=np.uint8)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        lm_list = hand_landmarks.landmark
        h, w, _ = frame.shape
        index_x = int(lm_list[8].x * w)
        index_y = int(lm_list[8].y * h)

        # Button detection
        if index_y < button_height:
            for name, (x1, x2) in button_coords.items():
                if x1 < index_x < x2:
                    selected_button = name
                    if name == "eraser":
                        eraser_mode = True
                    else:
                        eraser_mode = False
                        draw_color = {
                            "red": (0, 0, 255),
                            "blue": (255, 0, 0),
                            "green": (0, 255, 0),
                            "pen": (255, 255, 255)
                        }.get(name, (0, 0, 255))
                    break

        else:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = index_x, index_y

            if eraser_mode:
                cv2.circle(canvas, (index_x, index_y), 20, (0, 0, 0), -1)
                cv2.circle(drawn_mask, (index_x, index_y), 20, 0, -1)
            else:
                cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), draw_color, 5)
                cv2.line(drawn_mask, (prev_x, prev_y), (index_x, index_y), 255, 5)

            prev_x, prev_y = index_x, index_y
    else:
        prev_x, prev_y = 0, 0

    # Combine canvas with frame
    frame_output = frame.copy()
    frame_output[drawn_mask > 0] = canvas[drawn_mask > 0]

    # Draw button images
    for name, (x1, x2) in button_coords.items():
        button_img = button_images[name]
        frame_output[0:button_height, x1:x2] = cv2.addWeighted(
            frame_output[0:button_height, x1:x2], 0.3, button_img, 0.7, 0
        )
        if selected_button == name:
            cv2.rectangle(frame_output, (x1, 0), (x2, button_height), (255, 255, 255), 3)

    # Show image on Streamlit
    frame_placeholder.image(frame_output, channels="BGR")

    # Break condition (Streamlit can't use cv2.waitKey, so skip it here)