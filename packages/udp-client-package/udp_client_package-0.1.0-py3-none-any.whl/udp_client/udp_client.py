# This Python file uses the following encoding: utf-8
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from typing import Optional

class UdpClient:
    """UDP通信客户端类
    
    用于处理UDP数据报的发送和接收
    """
    
    def __init__(self, local_ip: str = "0.0.0.0", local_port: int = 0):
        """初始化UDP客户端
        
        Args:
            local_ip: 本地绑定IP地址，默认为0.0.0.0（所有网络接口）
            local_port: 本地绑定端口，默认为0（系统自动分配）
        """
        self.udp_socket = QUdpSocket()
        self._target_address: Optional[QHostAddress] = None
        self._target_port: Optional[int] = None
        
        if not self.udp_socket.bind(QHostAddress(local_ip), local_port):
            raise RuntimeError(f"无法绑定到 {local_ip}:{local_port}")

    def connect_to(self, target_ip: str, target_port: int) -> None:
        """设置目标地址和端口
        
        Args:
            target_ip: 目标IP地址
            target_port: 目标端口
        """
        self._target_address = QHostAddress(target_ip)
        self._target_port = target_port
        self.udp_socket.readyRead.connect(self._handle_incoming_data)

    def _handle_incoming_data(self) -> None:
        """处理接收到的数据"""
        while self.udp_socket.hasPendingDatagrams():
            datagram = self.udp_socket.receiveDatagram()
            if datagram.isValid():
                data = datagram.data().decode()
                sender = datagram.senderAddress()
                port = datagram.senderPort()
                print(f"收到来自 {sender.toString()}:{port} 的数据: {data}")

    def send_message(self, message: str) -> bool:
        """发送消息到目标地址
        
        Args:
            message: 要发送的消息
            
        Returns:
            bool: 发送是否成功
        """
        if not self._target_address or not self._target_port:
            raise RuntimeError("未设置目标地址和端口")
            
        bytes_written = self.udp_socket.writeDatagram(
            message, 
            self._target_address, 
            self._target_port
        )
        return bytes_written > 0

    def close(self) -> None:
        """关闭UDP socket"""
        self.udp_socket.close()

    @property
    def target_address(self) -> Optional[QHostAddress]:
        """获取目标地址"""
        return self._target_address

    @property
    def target_port(self) -> Optional[int]:
        """获取目标端口"""
        return self._target_port

    @property
    def local_address(self) -> str:
        """获取本地地址"""
        return self.udp_socket.localAddress().toString()

    @property
    def local_port(self) -> int:
        """获取本地端口"""
        return self.udp_socket.localPort()

# # 测试代码
# # 创建UDP客户端
# udp = UdpClient(192.168.0.100,5000)

# # 连接到目标
# udp.connect_to("192.168.0.7", 5300)

# # 发送消息
# udp.send_message("Hello, UDP!")

# # 获取本地地址和端口
# print(f"本地地址: {udp.local_address}:{udp.local_port}")

# # 关闭连接
# udp.close()