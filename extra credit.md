{% include navigation.html %}

## Extra Credit 


## Triton Activity Notes

Airframe Subteam - designs and builds aircraft
- UGV and new vehicle
- Use MATLAB and python
- They try to minimize power to maximize range
- Design analysis helps to see problems
- They use 3D printing, laser printing and hotwiring
- Use fiberglass layup→ it is light
- UGV is the vehicle that drops during competition

Embedded Subteam - do payload and cut wires
- They have ground control station
- Handle the tuning of the plane
- Put the plane in the right mode to accept messages correctly
- USB connections
- Ensure everything has power
- Work on the Ground Control Station which has antenna tracker which takes in plane location to make antenna point directly at plane

Software Subteam - write code
- Ground control station has software aspect
- Path Planning handles autonomous waypoint generation
- Computer vision handles target detection and classification
- Split in back end and front end
- Back end is written in Go and handles plane telemetries, communication with computer vision and is the brain
- React code helps people interact and test
- Docker containerizer of software
- Team is redoing path planning
- New path planning algo uses rot* ; creates tree that makes sure optimal path is chosen
- Yellow dots are obstacles
- Computer vision : competition objective is to identify targets on the ground
- Deep Learning models trained for computer vision goals
- Computer vision server managers all parts of pipeline


Business Subteam - recaps
- Presentations
- Sponsorships from places like Nortrop Grumann

Reflection
- I could relate to the deep learning and neural networks that the team referenced. During the summer, I worked on a neural network that mapped how a fly decides what smell to avoid or approach. In a similar way, this team uses deep learning to create a machine learning algo that distinguishes colors