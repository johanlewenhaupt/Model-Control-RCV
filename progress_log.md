# Progress Log

This markdown file serves as a log that records the progress of our project.

<a name="project_plan"></a>
### Project Plan

| Sprint No. | Tasks planned to finish |
|:----------:|:-----------------------|
| 1 |<ul><li>Identify Input/Output variables to the MPC controller in dSpace. </li><li>Identify Input variables to the ROS simulator. </li><li>Determine the variables needed from the above tasks, as well as the units of these variables. </li><li> Implement a simple PI-controller in ROS, and go check if (1) it could control the vehicle to go straight with constant velocity; (2) it could control the vehicle speed up or slow down quickly. | 
| 2 | <ul><li>Compute new dynamics from the collected real data. The ROS simulator used a toyota car, but now uses the RCV. This implies we need to change some dynamic variables, such as the mass, max wheel angle, etc. </li><li> Verify the dynamics, to make sure that they are correct by comparing them with those parameters in dSpace. |
| 3 | <ul><li>Upgrade the PI-controller in ROS to an MPC-controller, and verify it using the same experimental settings of the literature [*Lateral Model Predictive Control for Over-Actuated Autonomous Vehicle*](http://ieeexplore.ieee.org/document/7995737/?reload=true). </li><li> Connect output from dSpace to input in ROS. |
| 4 | <ul><li>Connect the output of the MPC controller in ROS to the low-level controller in dSpace. The new MPC system in ROS should now be fully implemented, as it has input from high-level controller in dSpace, and gives output to low-level controller in dSpace. </li><li>Verify the new system by running a simulation from dSpace. |
| 5 | <ul><li>Create a movie that includes a project description as well as a demonstration of the end results. </li><li>Prepare a project presentation for the class. |

---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 |
|:------:|:------:|--------|--------|--------|--------|--------|
|    x   |        |        |        |        |        |        |

### 2017-11-02

- **done:**
  - group meeting in the morning;
  - finished ros installation (kinetic) along with rviz and gazebo 8.1;
  - went through ros tutorial 1.1.1-1.1.3.
- **unsolved:**
  - issue about ros installation on mac;
  - issue about "cannot connect to display" when launching rviz on windows 10 -> go with ubuntu via virtualbox (TODO).
- **next move:** 
  - read literature [*Lateral Model Predictive Control for Over-Actuated Autonomous Vehicle*](http://ieeexplore.ieee.org/document/7995737/?reload=true).

### 2017-11-03

- **done:**
  - group meeting in ITRL;
  - performed test run of simulator [*car_demo*](https://github.com/ecward/car_demo) on the shared laptop. achieved ~0.7 real time factor;
  - tried setting up TortoiseGit for Bitbucket and finish before sub-step 5 of step 5 according to the [instruction](https://gist.github.com/svanas/87330eeb17313ea50d5cf9c265ab693f#step-3-add-your-public-key-to-bitbucket).
- **unsolved:**
  - when starting simulation, we need to untick a lot of properties in rviz to increase real time factor. probably need to check some ways to keep some of the fancy properties while maintaining a high real time factor;
  - ~~some file paths indicated in the [instruction](https://gist.github.com/svanas/87330eeb17313ea50d5cf9c265ab693f#step-3-add-your-public-key-to-bitbucket) are non-existent or maybe deprecated, e.g. ```C:\Users\<your user name>\AppData\Local\GitHub\PORTAB~1\cmd``` in sub-step 5 of step 5~~ (solved in the record of [2017-11-06](#solved_issue_1)).
- **next move:** 
  - read literature [*Lateral Model Predictive Control for Over-Actuated Autonomous Vehicle*](http://ieeexplore.ieee.org/document/7995737/?reload=true) and those RCV part of literature [*Development of Platform-Independent System for Cooperative Automated Driving Evaluated in GCDC 2016*](http://ieeexplore.ieee.org/document/7891914/);
  - play around with ros tutorial beginner level and the [*turtlesim tutorials*](http://wiki.ros.org/turtlesim/Tutorials) if possible;
  - try finding the model part of the simulator in repo [*car_demo*](https://github.com/ecward/car_demo).
  
---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | 
|:------:|:------:|--------|--------|--------|--------|--------|
|    x   |    x   |        |        |        |        |        | 

### 2017-11-06

- **done:**
<a name="solved_issue_1"></a>
  - finished setting up git and bitbucket. The previous [instruction](https://gist.github.com/svanas/87330eeb17313ea50d5cf9c265ab693f#step-3-add-your-public-key-to-bitbucket) turns out to be too redundant to help, and we switch to this [writeup](http://guganeshan.com/blog/setting-up-git-and-tortoisegit-with-bitbucket-step-by-step.html) for quick setup;
  - cloned the simulink files to the local.
- **next move:** 
  - replace the parameters in the simulink diagram with RCV parameters.
  
### 2017-11-07

- **done:**
  - workshop about project management and scrum;
  - git-cloned the new branch [*new_car_model*](https://github.com/ecward/car_demo/tree/new_car_model) (this branch already replaces the Toyota model with RCV) into local repo and tested its running (roslaunch car_demo [rcv_sim.launch](https://github.com/ecward/car_demo/blob/new_car_model/car_demo/launch/rcv_sim.launch)). You can find the command line for git-cloning a specific branch [here](https://stackoverflow.com/questions/4811434/clone-only-one-branch).
- **unsolved:**
  - ~~It seems that rviz is automatically turned off when running the new branch. So perhaps we need to check this and modify it to have the rviz window popped up if those fancy properties, say camera views, are desired~~ (solved in the record of [2017-11-09](#solved_issue_2)).
- **next move:** 
  - double-check the issue above. It could just be a program crashing problem;
  - literature reading.
  
### 2017-11-09

- **done:**
  - We made a (preliminary) plan of our project, including 5 sprints of one week each. The sprint project plan can be found [here](#project_plan).
  - We started trying to find the inputs and outputs. The following graph illustrates the variabes. 
  ![MPC Inputs/Outputs](https://github.com/txzhao/Model-Control-RCV/blob/master/pic/MPCInputOutput.jpg)
  <a name="solved_issue_2"></a>
  - Looked into the rviz-not-popping-up issue. The reason for it comes as: in the launch file [*rcv_sim.launch*](https://github.com/ecward/car_demo/blob/new_car_model/car_demo/launch/rcv_sim.launch), line 34-36 are commented out. That's why the rviz window is not started.
- **next move:** 
  - Understand the input/output variables, such as what are their units.
  - Verify plan.
  
---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 |
|:------:|:------:|:------:|--------|--------|--------|--------|
|    x   |   x    |   x    |        |        |        |        |
  
### 2017-11-14

- **done:**

  - In ROS, we Implemented an alternative to the joystick. We are now able to give an bundle of inputs (throttle, break, shiftgear, steer) to the car straight from the terminal.
  - The following are the output variables of the MPC:

| Variable | Explanation |
|----------|-------------|
| MtrTorqueReqAfterLogic | Values between -75 - 75 [Nm], which equals a force F=T/r forward, where T is the torque and r the wheel radius. This torque is applied to all four wheels, as the RCV uses four-wheel driving. | 
| BrkTorqueReqAfterLogic | A torque value between 0 - 75 [Nm], with the expection of being set to 100 when the velocity is below 0.1 [m]. In the same manner as previously, this equals a force F = T/r, with T and r same as previously. |
| engageMechBrake | A value that is set to one when BrkTorqueReqAfterLogic is nonzero, otherwise this variable is zero. |
| curvatureReq | Curvature value, K, that correspond to a circle with the radius R=1/K. This radius will through Ackerman optimal steering give the wheel angles. |
| crabReq | Angle between the longitudinal line and the car direction. This angle combined with the curvature radius will through Ackerman optimal steering give the wheel angles. |

- **next move:** 
  - Implement PI controller in ROS and try it with a predefined path.

### 2017-11-15

- **done:**
  - done with the meeting with Eric;
  - changed some parts of the steering joints of back wheels; 
  - enabled joystick node connection with gazebo.
- **next move:** 
  - solve the issue of the spinning back wheels.

### 2017-11-16

- **done:**
  - solved the issue of the spinning back wheels and sorted out the crabbing move;
  - tested Akermann steering on Matlab.
- **next move:** 
  - transplant Akermann steering code to the simulator.
  
### 2017-11-17

- **done:**
  - Meeting and demonstration of our work this week. 
  - Solved Ackerman optimal steering in ROS. We can now simulate our car with correct 4-wheel steering based on a curvature and crabbing angle.
  - Decided to work to divide upon: 1 person will rescale the skeleton of the car, 2 persons will redfine the interface and implement PI, the last person will read on MPC.
- **next move:** 
  - Implement PI-controller that controlls a desired velocity and steering.

---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | 
|:------:|:------:|:------:|:------:|--------|--------|--------|
|    x   |    x   |    x   |    x   |        |        |        | 

### 2017-11-21

- **done:**
  - Managed to show the states in terminal as ROS runs, good for debugging.
  - Had a meeting with Gonzalo (PHD who previously worked on the RCV). Told us to remember to update time delay to 0.1 when MPC in ROS
- **next move:** 
  - Implement PI-controller that controlls a desired velocity and steering.

### 2017-11-23

- **done:**
  - Implemented PI-controller to control the desired velocity as well as steering, based on a one time command.
  - Updated the mass of the vehicle as well as the separate wheels. Moreover, we changed the max angle of the wheels to be the correct 25 degrees.
- **next move:** 
  - Implement the MPC controller.
  
### 2017-11-24

- **done:**
  - Fixed the problem of steering control that the car can only steer with the same curvature. Reason being that we used a wrong variable name ste instead of steer in move.py. Code uploaded: https://github.com/txzhao/car_demo

---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | 
|:------:|:------:|:------:|:------:|:------:|--------|--------|
|    x   |    x   |    x   |    x   |   x    |        |        | 

### 2017-11-28

- **done:**
  - Trying new approaches to implement the MPC controller in ROS. Coding by ourselves seem to be too much a task, as problems pop up literally everywhere. Now trying to convert the code via Matlab Coder.
  - Changed the interface of simulator to take torques, curvature and crabbing angle as input (same as MPC).

### 2017-11-29

- **done:**
  - Had a meeting with Yuchao, Erik and Lars where it was concluded that the task of replicating the full MPC code is too great. We instead decided to put more emphasis on understanding the MPC algorithm, and replica only the control algorithm. This task is easier as we do not now have to understand all the specific cases in Gonzalo's MPC controller.
  - Partially finished pure pursuit control (for following a path) and PI control (for velocity control).
- **unsolved:**
  - pure pursuit control failed at the turning point. also sometimes get stuck at a specific point t when the car surpassed its previous point t-1 with a distance only larger than the threshold we define.

### 2017-12-01

- **done:**
  - finished pure pursuit control to follow a predefined path. Turned out that we misunderstood the method in our previous implementation.
  
---

| Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | 
|:------:|:------:|:------:|:------:|:------:|:------:|--------|
|    x   |    x   |    x   |    x   |   x    |    x   |        | 

### 2017-12-04

- **done:**
  - add [real-time xy plot](https://github.com/txzhao/car_demo/blob/master/car_demo/src/liveplot.py) of path by using matplotlib.pyplot.
  - another round of code cleanup for pure pursuit; fix torque control in the mode selection part.
- **unsolved:**
  - ~~check the dimension of vehicle by comparing it with the width of road.~~
  - pure pursuit has a large control error and we thought maybe we can try an adaptive lookahead during pure pursuit.
  
### 2017-12-05

- **done:**
  - checked the width of road (~14m), which corresponds to the width of a 4-lane highway.
  - add yaw infomation in the live plot to visualize the heading direction of the car in real time.

### 2017-12-07

- **done:**
  - change the way of receiving velocity feedback from topic /rosout_agg to /base_link_ground_truth.
  - tried and managed to build C++ package from generated code. now it formed a loop connection instead of a one-way connection between MPC node and gazebo.
