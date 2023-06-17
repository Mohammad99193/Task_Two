import socket , threading
q = open("quiz.txt","r")
qe = []
for i in range(20):
 qe.append(q.readline()[0:-3])

Check_Answers = ["'9'", " '6'", " '15'", " '30'", " '150'", " '8'", " '24'", " '1000'", " '60'", " '80'",
 " '1200'", " '90'", " '100'", " '2000'", " '99'", " '88'", " '625'", " '2500'", " '36'", " '180'"]

So = socket.socket()
So.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
So.bind(('127.0.0.1',7777))
So.listen(5)

def handle_Users (i ,UserSocket,UserAdd):
    result = 0
    print(f'+++ Accepted  User_{i} and his Address is : {UserAdd}')
    UserSocket.send(f'{qe}'.encode())
    Ans = ''
    while True:
     Ans=UserSocket.recv(4096).decode()
     if Ans :
        break

    User_Answers = Ans[1:len(Ans)-1].split(',')
    
    for j in range(20) :
     if User_Answers[j] == Check_Answers[j]:
            result +=0.5
    
    UserSocket.send(f'Your Result is : {result} // Thank You'.encode())
    UserSocket.close()
    print(f'Done from User {i} and His result is {result}')


i = 1 
while True :
    print('The Server is Weating for new Users ......')
    us , uadd = So.accept()
    user = threading.Thread(target=handle_Users,args=(i, us, uadd))
    user.start()
    i +=1 









