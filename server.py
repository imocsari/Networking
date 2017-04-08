import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Server started!")
    while True:
        newdata = []
        while len(newdata) < 2:
            data, addr = s.recvfrom(1024)
            print("message from client: " + str(data.decode()))
            newdata.append(data)
        R = (newdata[1][::-1].decode() + newdata[0][::-1].decode())
        print("sending: " +str(R))
        s.sendto(R.encode(),addr)
    s.close()
    
    
if __name__ == '__main__':
        Main()
