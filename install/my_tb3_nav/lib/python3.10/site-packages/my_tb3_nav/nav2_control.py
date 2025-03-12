import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import time 
import math 


class TurtlebotNav(Node):
    def __init__(self):
        super().__init__("tb3_navigator")
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()
        self.get_logger().info("Nav2 has started")
    
    def go_to_goal(self,x,y):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x=x
        goal_pose.pose.position.y=y
        goal_pose.pose.orientation.w=1.0
        self.get_logger().info(f"Hedefe gidiliyor: X={x}, Y={y}")
        self.navigator.goToPose(goal_pose)

        while not self.navigator.isTaskComplete():
            feedback = self.navigator.getFeedback()
            if feedback:
                self.get_logger().info(f"Total Distance: {feedback.current_waypoint + 1}")
            time.sleep(1)

        result = self.navigator.getResult()
        if result == 4:  # NavigateToPose.Result.SUCCEEDED
            self.get_logger().info("Robot have reached to goal succesfully")
        else:
            self.get_logger().error("Navigation has failed")

def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotNav()
    
    node.go_to_goal(2.0, 2.0)  # Robotun gitmesini istediğin koordinatları yaz

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()