class TemperatureMonitor(Node):
    def __init__(self):
        super().__init__('temperature_monitor')
        # Subscriber para /temperature
        self.subscription = self.create_subscription(
            Float64,
            '/temperature',
            self.listener_callback,
            10)
        # Publisher para /average_temperature
        self.publisher_ = self.create_publisher(Float64, '/average_temperature', 10)
        
        # Buffer circular com as últimas 5 temperaturas
        self.data_queue = []

    def listener_callback(self, msg):
        # Adiciona o valor recebido ao buffer
        self.data_queue.append(msg.data)
        # Mantém só os últimos 5 valores (buffer circular)
        if len(self.data_queue) > 5:
            self.data_queue.pop(0)
        # Calcula a média
        avg = sum(self.data_queue) / len(self.data_queue)
        avg_msg = Float64()
        avg_msg.data = avg
        self.publisher_.publish(avg_msg)
        self.get_logger().info(f'Recebido: {msg.data:.2f} °C | Média: {avg:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
