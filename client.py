import socket

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # client.connect(('data.pr4e.org', 80))
        # request = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
        client.connect(('localhost', 9000))
        request = 'GET HTTP/1.0\r\n\r\n'.encode()
        client.send(request)
        while True:
            data = client.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')
    

if __name__ == '__main__':
    run_client()
    