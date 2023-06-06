#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class SmartphoneNode(Node): # modify name
    def __init__(self):
        super().__init__("smartphone") # modify name
        # subscribe to topic
        self.subscriber = self.create_subscription(String, "robot_news", self.callback_robot_news, 10)
        self.get_logger().info("Smarphone has been started")
    
    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)


    
def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode() # modify name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()