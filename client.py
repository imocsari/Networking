import socket

def Main():
    host = '127.0.0.1'
    port = 5001
    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    S = input("->")
    while S != "q":
        leng = len(S)
        halfleng = int(leng/2)
        if (leng % 2 == 0):
            S1 = S[0 : halfleng]
            S2 = S[halfleng : ]
        else:
            S1 = S[0 : (halfleng + 1)]
            S2 = S[(halfleng + 1) : ]
        s.sendto(S1.encode(), server)
        s.sendto(S2.encode(), server)
        data, addr = s.recvfrom(1024)
        if (data.decode() == S[::-1]):
            print('received from server: ' + str(data.decode()))
        else:
            "error"
        S = input("->")
    s.close()

if __name__ == '__main__':
    Main()
