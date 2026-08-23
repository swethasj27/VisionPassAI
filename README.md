VisionPassAI

AI-powered facial liveness verification system for secure attendance authentication.

VisionPassAI uses real-time facial landmark detection to verify that a person in front of the camera is a live user, rather than a photo or static image.

What It Does?

The system gives the user a sequence of randomized facial challenges. Attendance is verified only after the user successfully completes the required challenges.
Current verification flow

Blink detection
Left head turn
Return to center
Right head turn
Return to center
wider the mouth
Attendance Verified

The sequential flow prevents a user from simply performing random movements and getting verified.

Technologies Used:

Python

OpenCV — real-time camera processing

MediaPipe Face Mesh — facial landmark detection

Computer Vision

Facial Liveness Detection

📁 Project Structure

VisionPassAI/

MAIN.py

BLINKdetect.py

HEADturnleft.py

HEADturnright.py

faceCENTER.py

MOUTHopen.py

README.md

.gitignore

⚙️ How It Works

The webcam captures the user's face in real time.

MediaPipe Face Mesh extracts facial landmarks, which are then used to determine:

whether the user blinked
whether the user turned their head left
whether the user returned to the center
whether the user turned their head right
whether the user opened their mouth

Each challenge is processed only when it is the user's current required step.

For example:
Blink 

↓ 

Left Turn 

↓

Center

↓

Right Turn 

↓ 

Center 

↓ 

Mouth Open

↓ 

Attendance Verified

🛡️ Liveness Detection
The purpose of the challenge-based system is to make the verification process more resistant to simple spoofing attempts such as presenting a static photograph to the camera.

Instead of verifying only whether a face exists, VisionPassAI checks whether the detected face performs the required real-time actions.
The current version demonstrates real-time facial liveness verification using sequential facial challenges.

Future Improvements

 Randomized challenge sequences
 
 Mobile application support
 
 Backend/database integration
 
 Stronger anti-spoofing mechanisms
 
 Attendance record management
 
 Improved user interface
 
 Offline verification with later synchronization
 
 Project

VisionPassAI
AI / Computer Vision project focused on secure facial liveness verification.

