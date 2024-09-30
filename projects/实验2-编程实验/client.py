import socket

# 服务器的 IP 地址和端口号（替换为服务器的实际 IP）
server_ip = "172.26.104.148"  # 你的 Mac 服务器 IP 地址
server_port = 12345  # 和服务器端保持一致的端口号

# 创建一个 UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 要发送的消息
message = "Hello, Server!"

# 发送消息给服务器
client_socket.sendto(message.encode(), (server_ip, server_port))
print(f"向服务器发送消息: {message}")

# 接收来自服务器的响应
response, server_addr = client_socket.recvfrom(1024)
print(f"收到来自服务器 {server_addr} 的响应: {response.decode()}")

# 关闭客户端 socket
client_socket.close()