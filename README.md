# lehigh_barc

roslaunch openni2_launch openni2.launch depth_registration:=true

roslaunch rtabmap_ros demo_turtlebot_mapping.launch localization:=true rgbd_odometry:=true

roslaunch rtabmap_ros demo_turtlebot_rviz.launch
