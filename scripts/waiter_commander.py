#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def commander():
    pub = rospy.Publisher('waiter/joint_states', JointState, 
                            queue_size=10)
    rospy.init_node('commander', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    joint_state = JointState()
    joint_state.header = Header()
    joint_state.name = ['base_to_legs', 'legs_to_body']

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        joint_state.position = [0.4, 0.1]

        pub.publish(joint_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass