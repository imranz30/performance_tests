#include "ros/ros.h"
#include "performance_tests/SuperAwesome.h"

int count = 0;
void chatterCallback(performance_tests::SuperAwesome msg)
{
   ROS_INFO("%s is greeting", msg.superawesome.c_str());
   ROS_INFO("%d msgs received by c_sub", count);
   ++count;
}

int main(int argc, char **argv)
{
   ros::init(argc, argv, "listener");
   ros::NodeHandle n;
   
   ros::Subscriber sub = n.subscribe("custom_chatter", 1000, chatterCallback);
   
   ros::spin();
 
   return 0;
}
