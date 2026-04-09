import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math, random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        # Cria publisher para o tópico /temperature
        self.publisher_ = self.create_publisher(Float64, '/temperature', 10)
        # Timer para publicar a cada 0.5s (2 Hz)
        self.timer = self.create_timer(0.5, self.publish_temperature)

    def publish_temperature(self):
        # Simulação de sensor: valor oscilando com seno + aleatório
        random_number = random.randint(80, 100)
        temperature = 25.0 + 5.0 * math.sin(random_number / 10.0)
        msg = Float64()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando temperatura: {temperature:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
