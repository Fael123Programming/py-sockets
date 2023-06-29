import urllib.request as r

def run_client():
    request = r.urlopen('http://127.0.0.1:9000')
    for line in request:
        print(line.decode().strip())


if __name__ == '__main__':
    run_client()
    