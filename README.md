Virtual Drawing Board
A real-time, hand-gesture-controlled virtual drawing board powered by MediaPipe and OpenCV. This application allows you to draw, erase, and select colors using your index finger — no physical stylus or touchscreen required!

Demo
Insert a short GIF or video link demonstrating the project in action.

Features
Real-Time Hand Tracking: Utilizes MediaPipe to detect and track hand gestures via your webcam.

Gesture-Based Drawing: Draw using your index finger with smooth tracking and dynamic control.

Color Selection: Easily switch between multiple colors using virtual on-screen buttons.

Eraser Mode: "Erase" drawn content by switching to a special eraser gesture or button.

Canvas Reset: Clear the entire canvas with a dedicated gesture or trash button.

Seamless Interface: Blends live video with your drawing canvas, creating a mixed-reality whiteboard experience.

Tech Stack
Python

OpenCV – for image processing and GUI handling.

MediaPipe – for hand detection and tracking.

NumPy – for efficient canvas array manipulation.

How It Works
The webcam feed is captured using OpenCV.

MediaPipe processes the frame to detect hand landmarks.

If the index finger is raised and tracked:

The system checks if the fingertip is over any UI buttons (colors, eraser, clear).

Otherwise, it draws on a separate black canvas in the chosen color.

The canvas is blended with the live video feed for a smooth overlay effect.

Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/Bhama-S-Nair/Virtual-Drawing-board.git
cd Virtual-Drawing-board
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe numpy
Run the project

bash
Copy
Edit
python main.py
Folder Structure
text
Copy
Edit
├── main.py             # Main application script
├── README.md           # Project description
├── black.png           # Color button images
├── red.png
├── green.png
├── blue.png
├── eraser.png
├── trash.png
Controls
Draw: Use your index finger in the main screen area.

Change Color: Hover your finger over a color button.

Eraser: Select the eraser tool to remove drawn lines.

Clear Canvas: Hover over the trash icon to wipe the entire board.

Applications
Virtual classrooms

Gesture-based UI control

Interactive whiteboards

Creative tools for touchless interfaces

Credits
Developed by Bhama S Nair

MediaPipe by Google

OpenCV community

License
This project is licensed under the MIT License – see the LICENSE file for details.

