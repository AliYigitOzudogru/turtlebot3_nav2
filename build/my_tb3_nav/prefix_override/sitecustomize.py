import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ali/Desktop/turtlebot3_nav2/install/my_tb3_nav'
