import rospy
import time


def cameras_can_talk(my_name, my_resolution):

    while not rospy.is_shutdown():
        rospy.loginfo("Camera name: " + my_name + " |||||||||||| resolution: " + my_resolution)
        time.sleep(2)
