#!/usr/bin/env python 
import rospy
from std_msgs.msg import Int16, String

def sender ():
    pub = rospy.Publisher ('num', Int16, queue_size=10)
    rospy.init_node("sender", anonymous=True)
    rate = rospy.Rate(1)
    x=10
    while not rospy.is_shutdown():
        my_num = x
        rospy.loginfo(my_num)
        pub.publish(my_num)
        rate.sleep()
        x=x+1

if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass

