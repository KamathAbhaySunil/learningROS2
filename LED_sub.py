#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LEDSubNode(Node):
    def __init__(self):
        super().__init__("LED_subscriber")
        self.subscription = self.create_subscription(
            Bool,
            'led_control',
            self.listener_callback,
            10
        )
        self.subscription
    
    def listener_callback(self, msg):
        if msg.data:
            self.get_logger().info('LED turned ON')
        else:
            self.get_logger().info('LED turned OFF')

def main(args=None):
    rclpy.init(args=args)
    LED_subscriber = LEDSubNode()
    rclpy.spin(LED_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
