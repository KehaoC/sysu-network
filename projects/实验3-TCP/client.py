import socket
import threading

SERVER_IP = '172.16.9.1'
SERVER_PORT = 12345

ADDR = (SERVER_IP, SERVER_PORT)

def receive_message(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f'\n收到消息: {msg}')
        except:
            print("与服务器断开连接")
            client_socket.close()
            break

# 启动客户端并连接到服务器
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    # 用户登录，发送用户名到服务器
    username = input("输入用户名")
    client_socket.send(username.encode('utf-8'))

    # 开启新线程，专门用于接收消息
    threading.Thread(target=receive_message, args=(client_socket,)).start()

    while True:
        target_user = input("请输入你要私聊的对象:")
        message = input("请输入消息:")
        full_message = f"{target_user}:{message}"
        client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    start_client()