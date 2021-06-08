#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import termios
import sys


def get_byte():
    old_attr = termios.tcgetattr(sys.stdin.fileno())
    new_attr = [item for item in old_attr]
    new_attr[3] &= ~(termios.ICANON|termios.ECHO)
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, new_attr)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, old_attr)
    return key

def control():
    rospy.init_node("joint_positions_node", anonymous=False)
    j1_pub = rospy.Publisher("/reachAlpha/joint_1_controller/command", Float64, queue_size=10)
    j2_pub = rospy.Publisher("/reachAlpha/joint_2_controller/command", Float64, queue_size=10)
    j5_pub = rospy.Publisher("/reachAlpha/joint_3_controller/command", Float64, queue_size=10)
    j6_pub = rospy.Publisher("/reachAlpha/joint_4_controller/command", Float64, queue_size=10)

    pub_dict = {'1':j1_pub, '2':j2_pub, '3':j5_pub, '4':j6_pub}
    pub = j1_pub
    command = 0

    while not rospy.is_shutdown():
        key = get_byte()
        new_pub = pub_dict.get(key, pub)
        command *= (new_pub==pub)
        pub = new_pub
        command = 0.1+((key=='d')-(key=='a'))
        pub.publish(command)

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
