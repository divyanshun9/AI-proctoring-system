# Proctoring-AI

Project to create an automated proctoring system where the user can be monitored automatically through the webcam and microphone. The project is divided into two parts: vision and audio-based functionalities.


## Vision

It has six vision based functionalities right now:
1. Track eyeballs and report if candidate is looking left, right or up.
2. Find if the candidate opens his mouth by recording the distance between lips at starting.
3. Instance segmentation to count number of people and report if no one or more than one person detected.
4. Find and report any instances of mobile phones.
5. Head pose estimation to find where the person is looking.
6. Face spoofing detection

### Face detection
Earlier, Dlib's frontal face HOG detector was used to find faces. However, it did not give very good results. <br>
different face detection models are compared and OpenCV's DNN module provides best result.

It is implemented in `face_detector.py` and is used for tracking eyes, mouth opening detection, head pose estimation, and face spoofing.


### Facial Landmarks
Earlier, Dlib's facial landmarks model was used but it did not give good results when a face was at an angle. Now, new Tensorflow-based model is used

It is implemented in `face_landmarks.py` and is used for tracking eyes, mouth opening detection, and head pose estimation.


### Eye tracking
`eye_tracker.py` is to track eyes.

### Mouth Opening Detection
`mouth_opening_detector.py` is used to check if the candidate opens his/her mouth during the exam after recording it initially.



### Person counting and mobile phone detection
`person_and_phone.py` is for counting persons and detecting mobile phones. YOLOv3 is used in Tensorflow 2 .
### Head pose estimation
`head_pose_estimation.py` is used for finding where the head is facing. 

### Face spoofing
`face_spoofing.py` is used to find whether the face is real or a photograph or image.

### FPS obtained
Functionality | On Intel i5
--- | ---
Eye Tracking | 7.1
Mouth Detection | 7.2
Person and Phone Detection | 1.3
Head Pose Estimation | 8.5
Face Spoofing | 6.9

If you testing on a different processor a GPU consider making a pull request to add the FPS obtained on that processor.




