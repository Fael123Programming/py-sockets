from socket import *

def run_server():
    with socket(AF_INET, SOCK_STREAM) as server:
        print('Access \'http://localhost:9000\'')
        try:
            server.bind(('localhost', 9000))
            server.listen(5)
            while True:
                client, address = server.accept()
                request = client.recv(5000).decode()
                split = request.split('\n')
                if len(split) > 0:
                    print(split[0])
                data = 'HTTP/1.1 200 OK\r\n'
                data += 'Content-Type: text/html; charset=utf-8\r\n\r\n'
                data += '<html><body><h1>Hello from server!</h1></body></html>'
                client.sendall(data.encode())
                client.shutdown(SHUT_WR)
        except KeyboardInterrupt:
            print('\nShutting down...\n')
        except Exception as exc:
            print('Error: \n')
            print(exc)
        
        
if __name__ == '__main__':
    run_server()
        