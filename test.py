import rclpy
from signal_publisher import SignalPublisher
from signal_subscriber import SignalSubscriber

rclpy.init()
pub = SignalPublisher()
sub = SignalSubscriber()

pub.send_signal()
rclpy.spin_once(pub, timeout_sec=0.1)
rclpy.spin(sub)
