#!/usr/bin/env python
## publishes std_msgs/Strings messages
## to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
# from turtlesim.msg import Pose
import math
import numpy as np
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 2056
#import socketconnection class to connect to robot
#requires socketconnection_class.py file in the same folder
from socketconnection_class import ConnectSocket
connecttcp = ConnectSocket()
s = connecttcp.sock
#get ip adress and port from launch file
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")
ip_address = "172.21.5.123"
port = 7171
connecttcp.connect(str(ip_address), port)

def getInfo_WirelessLink():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_WirelessLink', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Wirelesslink"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_WirelessQuality():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_WirelessQuality', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo WirelessQuality"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_Odometer():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Odometer', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Odometer(KM)"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_HourMeter():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_HourMeter', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo HourMeter"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_Temperature():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Temperature', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Temperature(C)"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_LaserScore():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserScore', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserScore"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

def getInfo_LaserLock():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserLock', String, queue_size=10)
    #specify node name
    rospy.init_node('getInfo_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserLock"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            applicationFaultQuery = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(applicationFaultQuery)[1:])
            #publish data
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()
            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")
            rate.sleep()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            getInfo_WirelessLink()
            getInfo_WirelessQuality()
            getInfo_Odometer()
            getInfo_HourMeter()
            getInfo_Temperature()
            getInfo_LaserScore()
            getInfo_LaserLock()

    except rospy.ROSInterruptException:
        pass