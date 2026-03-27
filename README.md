# Smart Dance Practice Mirror (BYOP Capstone)

## About the Project
I developed this tool to solve a practical problem I consistently face during solo dance practice: the inefficient cycle of recording and re-watching videos just to check my form. Without access to a professional studio mirror, it is difficult to verify if limb angles and extensions are accurate in real-time. 

This project acts as a Computer Vision-powered "Smart Mirror" accessed through a standard webcam. Utilizing Google's MediaPipe and OpenCV, it maps the user's skeletal joints and dynamically calculates the interior angles of the elbows and knees. The system provides immediate visual feedback directly on the screen—highlighting full extensions (over 160 degrees) in **green**, and indicating bent or broken forms in **red**. 

To take it a step further than just live feedback, the script logs this spatial data throughout the practice session. Once the routine is finished, it generates a performance graph and saves a CSV file, allowing the dancer to review exactly when and where their form began to lose consistency.

**Course Concepts Applied:** Image Processing, Pose Estimation, Coordinate Geometry, and Data Visualization.

**Project Structure**

main.py: The primary application script containing the CV pipeline.

requirements.txt: Configuration file for environment dependencies.

README.md: Documentation and setup guide.

.gitignore: Prevents virtual environment and cache files from being tracked.

dance_telemetry_*.csv: Output data files from practice sessions.

---

## Local Setup & Installation

This application is fully executable via the command-line interface (CLI). 

### 1. Clone the Repository
Open your terminal and clone the project:

``` bash
git clone [https://github.com/Khushi-2110/-byop-dance-tracker.git](https://github.com/Khushi-2110/-byop-dance-tracker.git)
cd -byop-dance-tracker
```

### 2: Configure a Virtual Environment

It is highly recommended to use a virtual environment to ensure dependency stability.

For Windows (PowerShell):
If scripts are disabled on your system, run the first command as Administrator:

``` bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Create environment 
``` bash
python -m venv venv
```
``` bash
.\venv\Scripts\activate
```


For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3: Install Dependencies

This project requires specific library versions (notably numpy<2.0.0) to maintain compatibility with the MediaPipe framework.
``` bash
pip install -r requirements.txt
```
Execution & Usage Instructions

### 4: Launch the Application

Ensure your webcam is not being used by other applications (Zoom, Teams, etc.), then run:

``` bash
python main.py
```

### 5: Practice and Feedback

Positioning: Stand 5-7 feet away from the camera so your full body is visible.

Live Feedback: Perform your routine. The screen will display live angle calculations. Green text signifies a full extension (>160°).

Stop Session: Press the 'q' key on your keyboard to close the camera feed.
  
### 6: Review Analytics

Graph: A Matplotlib window will pop up automatically showing your extension consistency over time.

Telemetry: A new .csv file with a unique timestamp will be saved to your folder containing the raw coordinate data.

### 7: Troubleshooting

Numpy/MediaPipe Error: If you see a numpy._core error, ensure you are using the virtual environment and have installed the versions specified in requirements.txt.

Scripts Disabled: If the activate command fails on Windows, refer to Step 2 for the Set-ExecutionPolicy fix.

Webcam Access: Ensure no other application is currently using the camera.
