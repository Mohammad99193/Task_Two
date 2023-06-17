import socket
Answers = []
result = ''
Cs = socket.socket()
Cs.connect(('127.0.0.1',7777) )
msg =  Cs.recv(1024).decode() 
qe = msg[1:len(msg)-1].split(',')
for i in range(20) :
    if i ==19 :
        Answers.append(input(f'{qe[i]}'))
        done =  input('Are you Finish ? Y/N ')
        if done == 'Y':
         Cs.sendto(f'{Answers}'.encode(), ('127.0.0.1',7777))
         while True:
            result = Cs.recv(1024).decode()
            if result :
                print(result)
                Cs.close()
                break
         break        
        else :
         print('You have to try later...!')
         Cs.close()
         break
    Answers.append(input(f'{qe[i]}'))

print('Done....!')


