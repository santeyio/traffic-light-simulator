##############################
Traffic Light Simulator Goals
##############################

This is an attempt to simulate a simple traffic light. You can specify how long you want each light show before it changes to the next light, as well as the number of cycles (green to red or red to green light changes) you want before the simulator stops running.

#############################
Install
#############################

Install with pip
#####################

You may want to do this in a virtualenv if you don't want to clutter up your global packages. Certainly not necessary, but if you want to use a virtualenv just: ::

  $ virtuanelv testenv
  $ cd testenv
  $ . bin/activate

Then simply install with pip: ::

  $ pip install traffic-light-simulator
  
Using the source files
#######################

Simply clone this repo. 

#############################
Running the simulator
#############################

If you installed with pip, you have a script available to you to run the simulator. Simply enter into your terminal: ::

  $ traffic-light-simulator

Otherwise, if you've cloned the repo, just run the traffic_light_simulator/user_interface.py with your interpreter: ::

  $ python user_interface.py


#############################
Running the tests
#############################

There are some tests that I wrote while writing the TrafficLight class, located in tests.py. If you want to run it simply run it with your interpreter ::

  $ python tests.py
