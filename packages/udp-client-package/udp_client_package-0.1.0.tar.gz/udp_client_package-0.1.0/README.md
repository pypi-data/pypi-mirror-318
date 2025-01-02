# UDP Client

一个基于PySide6的简单UDP客户端实现。

## 安装
pip install dist/udp_client_package-0.1.0-py3-none-any.whl


## 使用示例

from udp_client import UdpClient


### 创建UDP客户端
udp = UdpClient(local_ip="192.168.0.100", local_port=5000)

### 连接到目标
udp.connect_to("192.168.0.7", 5300)

### 发送消息
udp.send_message("Hello, UDP!")

### 获取本地地址和端口
print(f"本地地址: {udp.local_address}:{udp.local_port}")

### 关闭连接
udp.close()
