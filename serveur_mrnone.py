import sys, socket, select, os, time

Title = "-----------Messagerie de None-----------";

str(raw_input("Pour entrer tapez : 1\n-->"))
you = str(raw_input("Entre ton pseudo : "))

def chat_client():

    hostname = socket.gethostname()
    host = socket.gethostbyname('codeat.ddns.net')
    port = 9009
    print 'Thank you'
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print host
    try :
        print '---------------connexion au server---------------'
        s.connect((host, port))
    except :
        print "Le serveur n'est pas online, Veuillez contacter le createur pour qu'il active son serveur."
        sys.exit()
    
    print 'Vou etes connecter au serveur, vous pouvez enoyer des messages !'
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Title)
    sys.stdout.write(you+"=> "); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Error in Windows- Solution: select on sockets on one thread and blocking local I/O on a second thread,
        # Working on this!
        # May have to use Async frameworks like Twisted
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        sock.shutdown(socket.SHUT_WR)
         
        for sock in read_sockets:            
            if sock == s:

                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :

                    sys.stdout.write(data)
                    sys.stdout.write(you+"=> "); sys.stdout.flush() 
                        
            
            else :

                msg = you+":"+sys.stdin.readline()
                s.send(msg)
                sys.stdout.write(you+"-> "); sys.stdout.flush() 
                 

if __name__ == "__main__":

    sys.exit(chat_client())
