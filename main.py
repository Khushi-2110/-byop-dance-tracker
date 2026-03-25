import cv2
import numpy as np
import csv
import time
import matplotlib.pyplot as plt

# --- Setup MediaPipe ---
import mediapipe as mp

# Standard way to access solutions
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles # Optional: for better looking lines
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(np.degrees(radians))
    return angle if angle <= 180 else 360 - angle

# --- Setup Video Capture ---
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# --- Setup CSV Logging ---
filename = f"dance_telemetry_{int(time.time())}.csv"
file = open(filename, mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["Frame", "Timestamp", "Joint", "Angle", "Status"])

# --- Setup Data Storage for Final Graph ---
angle_history = {"Left Arm": [], "Right Arm": [], "Left Leg": [], "Right Leg": []}
frame_history = []

print("Starting Dance Tracker. Press 'q' to stop and view your performance graph.")

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Mirror effect
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            h, w, _ = image.shape

            # Define joints to track
            joints = {
                "Left Arm": [
                    [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y],
                    [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y],
                    [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                ],
                "Right Arm": [
                    [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y],
                    [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y],
                    [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                ],
                "Left Leg": [
                    [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],
                    [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y],
                    [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                ],
                "Right Leg": [
                    [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y],
                    [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y],
                    [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                ]
            }

            frame_history.append(frame_count)

            # Calculate and display angles
            for name, points in joints.items():
                angle = calculate_angle(*points)
                color = (0, 255, 0) if angle > 160 else (0, 0, 255)
                status = "Extended" if angle > 160 else "Bent"

                # Use the middle joint (elbow/knee) for text placement
                joint_pos = tuple(np.multiply(points[1], [w, h]).astype(int))
                cv2.putText(image, f"{name}: {int(angle)}°",
                            joint_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA)

                # Log to CSV
                writer.writerow([frame_count, time.time(), name, int(angle), status])

                # Save for the final graph
                angle_history[name].append(angle)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Dance Practice Mirror - Performance Mode', image)

        frame_count += 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# --- Cleanup ---
cap.release()
file.close()
cv2.destroyAllWindows()

# --- Post-Session Analysis: Generate the Graph ---
print("Session saved! Generating final performance graph...")

plt.figure(figsize=(12, 6))
for name, angles in angle_history.items():
    plt.plot(frame_history, angles, label=name, linewidth=2)

plt.title("Dance Routine Joint Extension Analysis", fontsize=16)
plt.xlabel("Frames (Time)", fontsize=12)
plt.ylabel("Joint Angle (Degrees)", fontsize=12)
plt.ylim(0, 180)
plt.axhline(y=160, color='r', linestyle='--', alpha=0.5, label='Extension Target (160°)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
