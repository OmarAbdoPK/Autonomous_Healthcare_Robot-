#!/usr/bin/env python 
import rospy
from std_msgs.msg import String, Int16

def my_callback(my_num) :
    rospy.loginfo(f"I Got You {my_num}")

def listenersaad():
    rospy.init_node('listenersaad', anonymous=False)
    rospy.Subscriber("num", Int16, my_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listenersaad()
    except rospy.ROSInterruptException:
        pass
