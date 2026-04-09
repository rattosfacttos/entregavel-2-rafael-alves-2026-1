import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class TemperatureAvgMonitor(Node):
    def __init__(self):
        super().__init__('temperature_avg_monitor')
        # Subscriber para /average_temperature
        self.subscription = self.create_subscription(
            Float64,
            '/average_temperature',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Média recebida: {msg.data:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureAvgMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
