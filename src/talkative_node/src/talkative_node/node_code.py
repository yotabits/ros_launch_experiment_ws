import rospy
import time


def easytalk():
    rospy.init_node("not_used_because_of_launch_file")
    #rospy.logerr(rospy.get_param_names())
    #for param in rospy.get_param_names():
    #    rospy.logerr("param: " + param + "   val:" + rospy.get_param(param))
    interlocutor = rospy.get_param("~private_param")

    while not rospy.is_shutdown():
        rospy.loginfo("hello " + interlocutor)
        time.sleep(2)
