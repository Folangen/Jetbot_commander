import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kostya/ros2_ws/ROS2_Jetbot_Motor_Controller/install/ROS2_Jetbot_Motor_Controller'
