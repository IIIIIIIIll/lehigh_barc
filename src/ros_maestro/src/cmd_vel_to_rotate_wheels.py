#!/usr/bin/env python
import roslib
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

#need to do experiments on how the wheels relate to the 
def translatorCB(msg):
    key = '0'
    wheel_channel = '0'
    motor_channel = '5'
    wheel_radius = 0.05 #need to actually measure it in meters
    wheelSep = 0.13 * 2.54  #also in meters
    transVelocity = msg.linear.x    #actual speed in m.s
    rotVelocity = msg.angular.z     #radian
    rotate_angle = rotVelocity*180/3.1415 / 45 #should be somewhere between 0 and 30 and need to figure out how a kinematic model work
    if transVelocity > 0.5:
        transVelocity = 0.5
    if rotate_angle > 1:
        rotate_angle = 1
    rkey = 1500+int(transVelocity*800)  
    skey = 1500+int(rotate_angle*800)
    ssend =str(skey) 
    rsend =str(rkey)

    pub1.publish(key+wheel_channel+rsend)
    pub1.publish(key+motor_channel+ssend)    


if __name__ == "__main__":
    rospy.init_node('translator', anonymous=True) #make node 
    pub1 = rospy.Publisher('maestro_command', String, queue_size=5)
    rospy.Subscriber('/cmd_vel',Twist,translatorCB)
    rospy.spin()