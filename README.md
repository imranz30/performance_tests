# performance_tests
Publishers and Subscribers for ROS

This repository contains the publishers and subscribers for ROS done in c and python.

C FILES
  - c_pub (pubisher in c)
       <rosrun performance_tests c_pub>
  - c_sub (subscriber in c)
       <rosrun performance_tests c_sub>

PYTHON FILES
  - python_pub (publisher in python)
       <rosrun performance_tests python_pub.py>
  - python_sub (subscriber in python)
       <rosrun performance_tests python_sub.py>
  
These four nodes are run in the following combination:
  1. c_pub with c_sub and python_sub
  2. python_pub with c_sub and python_sub

For the 1st combination the loop rate of publishing the custom message was changed from 10 to 500. It is clear to see that
as the loop rate increases or the frequency of publishing messages increases c_sub is more close to the real life or the 
desired number of messages received as compared to the messages sent. The python_sub is slow to receiving messages and falls
behind the desired number of received messages as compared to the messages sent. The difference becomes obvious from loop rate
value of 200 onwards.

For the 2nd combination the loop rate of publishing the custom message was again changed from 10-500 but it is not really clear 
which is winning in this case. What is for sure is that c_sub is faster than python_sub. This is more evident and a clarity 
for the 1st combination of nodes. 

So I assume the loop rate of more then 200 results in clear observation of the fact that c based publishers and subcribers
are faster then python based ones.
