#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LEDPubNode(Node):
    def __init__(self):
        super().__init__("LED_publisher")
        self.publisher_ = self.create_publisher(Bool, 'led_control', 10)
        self.timer = self.create_timer(0.5, self.run_input_loop)
        

    def publish_led_state(self, state):
        msg = Bool()
        msg.data = state
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"'% ('ON' if state else 'OFF'))

    def run_input_loop(self):
        self.get_logger().info('LED Publisher Running. Type "n" + Enter to turn ON, "f" + Enter to turn OFF')
        while rclpy.ok():
            user_input = input("Enter command (n/f): ")
            if user_input == 'n':
                self.publish_led_state(True)
            elif user_input == 'f':
                self.publish_led_state(False)
            else:
                rclpy.shutdown()
                break

def main(args=None):
    rclpy.init(args=args)
    LED_publisher = LEDPubNode()
    rclpy.spin(LED_publisher)
    rclpy.shutdown()
if __name__ == '__main__':
    main() 