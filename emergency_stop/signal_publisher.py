import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SignalPublisher(Node):

    def __init__(self):
        super().__init__('signal_publisher')
        self.publisher_ = self.create_publisher(String, 'base_signal', 10)
        self.timer = self.create_timer(1.0, self.send_signal)  # send every second

    def send_signal(self):
        msg = String()
        msg.data = "base station signal"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing signal')


def main(args=None):
    rclpy.init(args=args)
    signal_publisher = SignalPublisher()
    rclpy.spin(signal_publisher)
    signal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()