# Virtual Drawing Board

A real-time, hand-gesture-controlled virtual drawing board powered by **MediaPipe** and **OpenCV**. This application allows you to draw, erase, and select colors using your index finger — no physical stylus or touchscreen required!

## Demo

![Screenshot 2025-05-26 225418](https://github.com/user-attachments/assets/19af8bfa-a563-4f71-a2ca-aedd6c6d405d)



---

## Features

- **Real-Time Hand Tracking**: Utilizes MediaPipe to detect and track hand gestures via your webcam.
- **Gesture-Based Drawing**: Draw using your index finger with smooth tracking and dynamic control.
- **Color Selection**: Easily switch between multiple colors using virtual on-screen buttons.
- **Eraser Mode**: "Erase" drawn content by switching to a special eraser gesture or button.
- **Canvas Reset**: Clear the entire canvas with a dedicated gesture or trash button.
- **Seamless Interface**: Blends live video with your drawing canvas, creating a mixed-reality whiteboard experience.

---

## Tech Stack

- **Python**
- **OpenCV** – for image processing and GUI handling.
- **MediaPipe** – for hand detection and tracking.
- **NumPy** – for efficient canvas array manipulation.

---

## How It Works

1. The webcam feed is captured using OpenCV.
2. MediaPipe processes the frame to detect hand landmarks.
3. If the index finger is raised and tracked:
   - The system checks if the fingertip is over any UI buttons (colors, eraser, clear).
   - Otherwise, it draws on a separate black canvas in the chosen color.
4. The canvas is blended with the live video feed for a smooth overlay effect.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhama-S-Nair/Virtual-Drawing-board.git
   cd Virtual-Drawing-board
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python mediapipe numpy
   ```

3. **Run the project**
   ```bash
   python main.py
   ```

---

## Folder Structure

```
├── main.py             # Main application script
├── README.md           # Project description
├── black.png           # Color button images
├── red.png
├── green.png
├── blue.png
├── eraser.png
├── trash.png
```

---

## Controls

- **Draw**: Use your index finger in the main screen area.
- **Change Color**: Hover your finger over a color button.
- **Eraser**: Select the eraser tool to remove drawn lines.
- **Clear Canvas**: Hover over the trash icon to wipe the entire board.

---

## Applications

- Virtual classrooms
- Gesture-based UI control
- Interactive whiteboards
- Creative tools for touchless interfaces

---

## Credits

- Developed by [Bhama S Nair](https://github.com/Bhama-S-Nair)
- MediaPipe by Google
- OpenCV community

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
