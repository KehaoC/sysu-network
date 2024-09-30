import socket
import threading


# 服务器IP和端口
SERVER_IP = "172.16.9.1"
SERVER_PORT = 12345
ADDR = (SERVER_IP, SERVER_PORT)

# 存储客户链接
clients = {}

# 处理客户端连接
def handle_client(sender_name, client_socket, addr):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"[{addr}] {msg}")
                handle_message(sender_name, msg, client_socket)
        except:
            # 客户端开链接
            print(f"[{addr}] 断开连接")
            client_socket.close()
            break

# 消息处理函数，在接受到消息后，转发给目标客户
def handle_message(sender_name, msg, sender_socket):
    # 消息格式 username: message
    target_user, message = msg.split(':', 1)
    if target_user in clients:
        target_socket = clients[target_user]
        target_socket.send(f"\n{sender_name}: {message}\n".encode('utf-8'))
    else:
        sender_socket.send("目标用户不存在".encode('utf-8'))

def objects_to_string(clients):
    clientList = []
    for key in clients.keys():
        clientList.append(key)
    return str(clientList)

# 启动服务器
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    print(f"[启动] 服务器启动，等待连接")

    while True:
        client_socket, client_addr = server_socket.accept()
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"[连接] 客户端连接自 {client_addr}")

        clientsList = objects_to_string(clients)
        online_clients = "在线列表：\n" + clientsList
        client_socket.send(online_clients.encode('utf-8'))

        threading.Thread(target=handle_client, args=(username, client_socket, client_addr)).start()

if __name__ == "__main__":
    start_server()
