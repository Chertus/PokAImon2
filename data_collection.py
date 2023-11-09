# data_collection.py
import pygetwindow as gw
import cv2
import numpy as np
import datetime
import os
from data_manager import save_session_data, save_log, save_json

# Function to capture screenshots
def capture_screenshots(window_title):
    window = gw.getWindowsWithTitle(window_title)[0]
    if window:
        window.activate()
        screenshot = gw.screenshot(region=(window.left, window.top, window.width, window.height))
        return np.array(screenshot)
    else:
        return None

# Function to record video
def record_video(window_title, session_id):
    video_path = os.path.join("sessions", f"video_{session_id}.avi")
    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), 8, (window.width, window.height))

    while True:
        img = capture_screenshots(window_title)
        if img is not None:
            out.write(img)
        else:
            break

    out.release()

# Example usage
session_id = "01aee661"
window_title = "pyboy1"  # Example window title
screenshot = capture_screenshots(window_title)
if screenshot is not None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join("sessions", f"screenshot_{session_id}_{timestamp}.png")
    cv2.imwrite(screenshot_path, screenshot)

    # Saving session data
    save_session_data(session_id, f"Screenshot captured: {screenshot_path}")
    save_log(f"Screenshot captured at {timestamp}")

# Start video recording (this should be run in a separate thread or process)
# record_video(window_title, session_id)
