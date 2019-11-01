#!/usr/bin/env python
from connectwifi import connecttowifi

# from socketconnection import socketconnect
# from socketconnection import data, s

from socketconnection_class import ConnectSocket, connecttcp

s = connecttcp.sock
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024

# connecttcp.connect("172.21.5.33", 7171)
# connecttcp.sendpassword()

def analogInputList():
    global s
    global data
    pub = rospy.Publisher('arcl_analogInputList', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    global rcv
    global i
    i = 1
    flag = 0
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while (flag == 0):
        if "End of commands" in rcv:
            flag == 1
            while not rospy.is_shutdown():
                command = "analogInputList"
                command = command.encode('ascii')
                s.send(command+b"\r\n")
                print "Running Command: ",command
                time.sleep(1)
                data = s.recv(BUFFER_SIZE)
                rcv = data.decode("utf-8")
            
                pubout = str(data.splitlines())
                pub.publish(pubout)
                time.sleep(1)
                rospy.loginfo(rcv)
                time.sleep(2)
                exit(0)

        else:
            flag == 0
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

                
if __name__ == '__main__':
    try:
        analogInputList()
    except rospy.ROSInterruptException:
        pass







