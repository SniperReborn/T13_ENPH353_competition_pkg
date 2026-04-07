#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def move_meter(cmd_pub, score_pub):
    rospy.sleep(1.0)

    score_pub.publish("team13,jleetmomo,0,NA")

    move = Twist()
    move.linear.x = 1

    end_time = rospy.Time.now().to_sec() + 3
    while rospy.Time.now().to_sec() < end_time:
        cmd_pub.publish(move)
        rospy.sleep(0.1)

    stop_move = Twist()
    cmd_pub.publish(stop_move)

    score_pub.publish("team13,jleetmomo,-1,NA")

def listener():
    rospy.init_node("time_trial")
    cmd_pub = rospy.Publisher("/B1/cmd_vel", Twist, queue_size=1)
    score_pub = rospy.Publisher("/score_tracker", String, queue_size=1)
    move_meter(cmd_pub, score_pub)

if __name__ == "__main__":
    listener()
