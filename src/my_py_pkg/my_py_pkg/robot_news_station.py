#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class RobotNewsStationNode(Node):

    def __init__(self):
        super().__init__(node_name="robot_news_station")
        self.robot_name_ = "R2D3"
        # publish msg on topic robot_news
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started")
    
    def publish_news(self):
        msg = String()
        msg.data = "Hi " + str(self.robot_name_) + " from the robot news station."
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    #callbacks called from spin function
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()