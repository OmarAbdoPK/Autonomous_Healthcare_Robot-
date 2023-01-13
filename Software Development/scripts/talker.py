import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher ("Chatting", String, queue_size=20)
    rospy.init_node("talker", anonymous=False)
    range = rospy.Rate(5)
    while not rospy.is_shutdown():
        hi_str = "hello_MOhammad_Saad %s" % rospy.get_time()
        rospy.loginfo(hi_str)
        pub.publish(hi_str)
        range.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



