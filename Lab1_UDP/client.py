import socket

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_address = ('172.16.9.1', 9090) # 客户端监听自己的端口
udp_client_socket.bind(client_address)

print("客户端已经启动，等待接收数据包")

# 统计
received_packets = []
expected_packets = 100
retryTimes = 0

while len(received_packets) < expected_packets:
    try:
        data, server = udp_client_socket.recvfrom(1024) 
    except:
        retryTimes += 1
        print(f"Error, Retry {retryTimes} times.")
        continue
    retryTimes = 0
    packet = data.decode()
    print(f'接收到：{packet}')
    received_packets.append(packet)

# 统计结果
received_packets = len(received_packets)
lost_count = expected_packets - received_packets

print(f"接受到{received_packets}个包, 丢失{lost_count}个包")

# 向服务器发送统计结果确认
udp_client_socket.sendto("Done".encode(), server)

# 关闭socket
udp_client_socket.close()