#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__(node_name="py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        # 2Hz so period is 0.5s
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Hello {str(self.counter_)}")
        


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    #callbacks called from spin function
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()