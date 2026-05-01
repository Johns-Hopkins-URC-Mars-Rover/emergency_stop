import rclpy
import json
from rclpy.node import Node
from std_msgs.msg import String
import base_motor.PublisherSubscriber.publisher as pub


class SignalSubscriber(Node):

    def __init__(self):
        super().__init__('signal_subscriber')
        
        self.subscription = self.create_subscription(
            String,
            'base_signal',
            self.signal_callback,
            10
        )

        self.publisher_ = pub.Publisher(
            "base_publisher",
            "base_motors",
            self.stop_rover,
            0.5
        )

        self.last_signal_time = self.get_clock().now()
        self.timer = self.create_timer(1.0, self.timer_callback)

    def stop_rover(self):
        data = {
            "speed": 0,
            "heading": 0
        }
        return json.dumps(data)

    def signal_callback(self, msg):
        self.last_signal_time = self.get_clock().now()
        self.get_logger().info('Received signal')

    def timer_callback(self):
        now = self.get_clock().now()
        elapsed = now - self.last_signal_time
        seconds = elapsed.nanoseconds / 1e9

        self.get_logger().info(f'Time since last message: {seconds:.2f} seconds')

        if seconds >= 3:
            self.get_logger().warn('No signal received! Stopping rover.')
            self.publisher_.publish()  # trigger stop command


def main(args=None):
    rclpy.init(args=args)
    signal_subscriber = SignalSubscriber()
    rclpy.spin(signal_subscriber)
    signal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()