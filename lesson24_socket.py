import socket
import threading

HOST = "127.0.0.1"
PORT = 5060

server_ready = threading.Event()


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print("სერვერი ელოდება კლიენტს...")
        server_ready.set()

        connection, address = server.accept()
        with connection:
            data = connection.recv(1024)
            text = data.decode()
            print("მივიღეთ:", text)
            connection.sendall(text.upper().encode())

    print("სერვერი დასრულდა")


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall("hello socket".encode())
        answer = client.recv(1024).decode()
    return answer


server_thread = threading.Thread(target=run_server)
server_thread.start()

server_ready.wait()  # კლიენტი მანამდე ელოდება, სანამ სერვერი მზად არ იქნება
answer = run_client()

server_thread.join()
print("პასუხი:", answer)
