cmake_minimum_required(VERSION 2.8.3)

project(reachAlpha)

find_package(catkin REQUIRED COMPONENTS
  controller_manager
  effort_controllers
  gazebo_ros
  gazebo_ros_control
  joint_state_controller
  joint_state_publisher
  position_controllers
  robot_state_publisher
  rospy
  rqt_gui
  rviz
  urdf
)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
