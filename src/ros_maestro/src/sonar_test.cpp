#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sstream>

#include "ros/ros.h"
#include <sensor_msgs/Range.h>


int main( int argc, char **argv){
    ros::init( argc, argv, "publish_sonar");
    ros::NodeHandle nh;
    sensor_msgs::Range rangeMsg;
    ros::Publisher pub = nh.advertise<sensor_msgs::Range>("sonar0",1);
    char rxBuf[80];
    float range;
    int fd;
    fd = open("/dev/ttyUSB1", O_EXCL);
    if (fd < 0){
        std::cerr << "Error opening sonar tty\n";
        return(-1);
    }

    while(ros::ok()){
        // Maxbotix output is R1234, range in mm
        int i = 0;
        while(read(fd, &rxBuf[i], 1)) {
            if (rxBuf[i] == '\r') {
            rxBuf[i] = '\0';
            break;
        }
        i++;
        
    }

    range = strtof(&rxBuf[1], NULL) / 1000; // output in meters
    rangeMsg.range = range;
    rangeMsg.header.stamp = ros::Time::now();
    ROS_INFO_STREAM("Sonar msg: " << std::string(rxBuf) << "range: "<< range);
    pub.publish(rangeMsg);
    }
    return(0);
}
