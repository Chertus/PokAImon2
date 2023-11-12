import pygetwindow as gw
import pyautogui
import cv2
import numpy as np
import time
import keyboard

def find_pyboy_window():
    windows = gw.getWindowsWithTitle('PyBoy')  # Adjust the title to match the PyBoy window
    return windows[0] if windows else None

def capture_window(window):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('pyboy_capture.avi', fourcc, 20.0, (window.width, window.height))

    while True:
        if not gw.getWindowsWithTitle('PyBoy'):  # Check if PyBoy window is still open
            break
        if keyboard.is_pressed('ctrl+shift+c'):  # Check if Ctrl+Shift+C is pressed
            break

        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)  # Write the frame to the video file

        time.sleep(0.05)  # Adjust the frequency of screenshots

    out.release()  # Release the VideoWriter object

def main():
    while True:
        pyboy_window = find_pyboy_window()
        if pyboy_window:
            print("PyBoy window found. Starting capture.")
            capture_window(pyboy_window)
            break
        else:
            print("Waiting for PyBoy window...")
            time.sleep(1)

if __name__ == "__main__":
    main()
