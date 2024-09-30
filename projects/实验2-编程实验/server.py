# Server ip: 172.26.104.148
# Client ip: 172.26.70.178

import socket
import time

# 服务器的 IP 地址和端口号
server_ip = "172.26.104.148"  # 接收来自所有 IP 的数据
server_port = 12345  # 使用的端口

# 客户端的 IP 地址和端口号
client_ip = "172.26.70.178"  # 替换为客户端的 IP 地址
client_port = 54321  # 客户端的端口

# 创建一个 UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口号
server_socket.bind((server_ip, server_port))

print(f"UDP 服务器正在向 {client_ip}:{client_port} 发送消息...")

# 设置发送的消息
message = "这是来自可豪Cohol服务器的消息"

# 不断发送消息
while True:
    server_socket.sendto(message.encode(), (client_ip, client_port))
    print(f"发送消息: {message} 到 {client_ip}:{client_port}")
    time.sleep(0.1)  # 每隔 100 毫秒发送一次