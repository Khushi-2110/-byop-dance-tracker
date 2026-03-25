# Smart Dance Practice Mirror

## About the Project
I developed this tool to solve a practical problem I consistently face during solo dance practice: the inefficient cycle of recording and re-watching videos just to check my form. Without access to a professional studio mirror, it is difficult to verify if limb angles and extensions are accurate in real-time. 

This project acts as a Computer Vision-powered "Smart Mirror" accessed through a standard webcam. Utilizing Google's MediaPipe and OpenCV, it maps the user's skeletal joints and dynamically calculates the interior angles of the elbows and knees. The system provides immediate visual feedback directly on the screen—highlighting full extensions (over 160 degrees) in green, and indicating bent or broken forms in red. 

To take it a step further than just live feedback, the script logs this spatial data throughout the practice session. Once the routine is finished, it generates a performance graph and saves a CSV file, allowing the dancer to review exactly when and where their form began to lose consistency.

**Course Concepts Applied:** Image Processing, Pose Estimation, Coordinate Geometry, and Data Visualization.

---

## Local Setup & Installation

This application is designed to be fully executable via the command-line interface (CLI). 

### 1. Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone [https://github.com/Khushi-2110/-byop-dance-tracker.git](https://github.com/Khushi-2110/-byop-dance-tracker.git)
cd -byop-dance-tracker

2. Configure a Virtual Environment
It is highly recommended to run this project inside a virtual environment to ensure dependency stability and prevent conflicts with global Python packages.

For Windows:

PowerShell
python -m venv venv
.\venv\Scripts\activate
For macOS/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
With your virtual environment active, install the required core libraries (OpenCV, MediaPipe, and Matplotlib):

Bash
pip install -r requirements.txt
Execution & Usage Instructions
(Note: Ensure your webcam is not currently allocated to another application like Zoom or Microsoft Teams before running the script).

To launch the Smart Mirror, execute the following command from the project's root directory:

Bash
python main.py
Positioning: Step back from the camera to ensure your upper body and knees are clearly visible within the frame.

Live Tracking: Begin your routine. The on-screen metrics will track your joint angles in real-time. Green text indicates a successful extension, while red text indicates a bent joint.

Conclude Session: Press the q key on your keyboard to terminate the camera feed.

Post-Session Analytics: Immediately upon closing, a Matplotlib graph will render to display your joint extension history over the duration of the session, and a .csv file containing the raw telemetry will be saved to your directory.