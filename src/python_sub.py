#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome

count = 0

def callback(data):
   rospy.loginfo("%s is greeting" % data.superawesome)
   global count
   count = count+1
   rospy.loginfo("%d msgs received by python_sub" % count)  
    

def listener():
   rospy.init_node('custom_listener', anonymous=True)
   rospy.Subscriber("custom_chatter", SuperAwesome, callback)
   rospy.spin()

if __name__ == '__main__':
   listener()
   
