#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome

def talker():
   pub = rospy.Publisher('custom_chatter', SuperAwesome)
   rospy.init_node('custom_talker', anonymous=True)
   r = rospy.Rate(500)
   msg = SuperAwesome()
   msg.superawesome = "Hello World"
   count = 0

   while not rospy.is_shutdown():
      rospy.loginfo(msg)
      pub.publish(msg)
      count = count+1
      rospy.loginfo("%d msgs sent by python_pub" % count) 
      r.sleep()

if __name__ == '__main__':
   try:
      talker()
   except rospy.ROSInterruptException: pass
