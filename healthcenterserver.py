

#!/usr/bin/env python

import socket
import threading
import sys
import sqlite3

udic={}  #global updated time index list

class ThreadServer(object):
    #define class member create serversocket
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #release port address guarantee port address can be reused
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    #listen incomming clients, build connection with multi clients via multithread
    #use the main thread just for listening for new clients. When one connects, the main thread creates a new thread that just listens to the new client and ends when it doesn't talk for 60 seconds.
    def listen(self):
        #connection queue maxnum
        self.sock.listen(2)
        #new client has new accept
        while True:
            conn, addr = self.sock.accept()
            conn.settimeout(60)
            t=threading.Thread(target=self.handle_client, args=(conn, addr))
            t.start()


    def handle_client(self, conn, addr):
        global udic
        try:
            msg=conn.recv(1024)
            list1=msg.split()
            list1 = list(map(str,list1))
            list1 = [l[2:-1] for l in list1]
            #print(list1)
            if not msg:
                raise error('Client disconnected')
            print('---------------------------------------------\nPhase1:The Health Center Server has received request from a patient with username', list1[0], 'and password', list1[1])

            #load user database
            #open file users.txt and store infor in its memoery
            try:
                with open('input/users.txt', 'r') as f:
                    store=f.read()
                #print('User database:\n', store)
            except IOError:
                print ('File is not found')
                conn.close()
                sys.exit(1)

            list2=store.split()

            dicti={}
            dicti[list2[0]]= list2[1]
            dicti[list2[2]]= list2[3]
            #print(dicti)
            #print(list(dicti.keys()))
            if list1[0] in dicti.keys():
                # print("svdsvdsvsdvdsvdsvdsvds")
                # print(dicti[list1[0]])
                # print('//......')
                # print(list1[1])
                if (dicti[list1[0]] == list1[1]):
                    # print("sdvsdvsdvdsvsv")
                    response="Success"
                    conn.send(bytes(response,'utf-8'))
                    print('Phase1: The Health Center Server sends the response:', response, 'to patient with username', list1[0])

                    ask=conn.recv(1024).decode()
                    print('Phase2: The Health Center Server receives a request for available time slots from patients with port number:', conn.getpeername()[1], 'and IP Address:', conn.getpeername()[0]) 

                    time=""
                    d={}
                    #communication only via string, not list
                    try:
                        f=open('input/availabilities.txt', 'r')
                        for l in f:
                            k,v = l.strip().split(' ', 1)
                            d[k]=v
                        #print(d)
                        # print(udic)

                        if len(udic) == 0:
                            udic = d.copy()
                        # print(udic)
                        keys=list(udic.keys())
                        # print(keys)
                        keys.sort()
                        # print(keys)
                        for k in keys:
                            ls = k + " " + udic[k]
                            #print(ls)

                        for k in keys:
                            t = k + " " + " ".join(udic[k].split()[:2]) + '\n'
                            time += t
                        f.close()
                    except IOError:
                        print("File is not accessible")
                        conn.close()
                        sys.exit(1)
                        
                    print(time)
                    #print('cvsvsvsvdsvsvs')
                    conn.send(bytes(time , 'utf-8'))
                    print('Phase2: The Healther Center Server sends available time slots to patients with username',list1[0])
                    
                    while True:
                        choice=conn.recv(1024).decode()
                        choicestr=choice.split(' ')
                        prefer=choicestr[1] + ""
                        
                        #check if prefer is included in indexlist or not, maybe not integer
                        ks=d.keys()
                        if prefer not in ks:
                            print('Receiving invalid time index, let patient re-enter')
                            p='Invalid'
                            conn.send(p.encode('utf-8'))
                        else:
                            break

                    print('Phase2: The Health Center Server receives a request for appoinment',prefer, 'from patient with port number:', conn.getpeername()[1], 'and username', list1[0])

                    if prefer in udic.keys():
                        docInfor = udic[prefer].split()[-1] + " "
                        print(docInfor) 
                        conn.send(bytes(docInfor , 'utf-8'))
                        print('Phase2: The Health Center Server confirms the following appointment', prefer, 'to patient with username', list1[0])
                        del udic[prefer]     #delete chosen choice
                    else:
                        q='notavailable'
                        conn.send(q.encode('utf-8'))
                        print( 'Phase2: The Health Center Server rejects the following appoinment', prefer, 'to patient with username',list1[0])

                else:
                    response="Failure"
                    conn.send(response) 
                    print('Phase1: The Health Center Server sends the response:', response, 'to patient with username', list1[0])
                    conn.close()
                
            else:
                response="Failure"
                conn.send(response)
                print('Phase1: The Health Center Server sends the reponses:', response, 'to patient with username', list1[0])
                conn.close()
        except:
            conn.close()
        
        conn.close()
    #end of handle_client function


if __name__ == "__main__":
    serverPort=21000
    serverHost='127.0.0.1'
    print('Patient Database:\n')
    conn = sqlite3.connect('Vidhi.db')
    cursor = conn.cursor()
    #print("Connected to SQLite")
    select_query = """SELECT * from patients"""
    cursor.execute(select_query)
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    #print("Printing each row")
    print("Id: ",end="\t")
    print("Username: ",end="\t")
    print("Password: ",end="\t")
    print("Insurance: ",end="\t")
    #print("Port: ", end="\t")
    print("\n")
    for r in records:
        print(r[0],end="\t")
        print(r[1],end="\t") 
        print(r[2],end="\t")
        print(r[3],end="\t\t")
        #print(r[4],end="\t")
        print("\n")
    #print("\n")
    print('\nDoctor Database:\n')
    select_query = """SELECT * from doctors"""
    cursor.execute(select_query)
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    #print("Printing each row")
    print("Name: ",end="\t")
    print("Port: ",end="\t")
    print("Insurance: ",end="\t")
    print("Cost: ",end="\t")
    #print("Port: ", end="\t")
    print("\n")
    for r in records:
        print(r[0],end="\t")
        print(r[1],end="\t") 
        print(r[2],end="\t")
        print(r[3],end="\t\t")
        #print(r[4],end="\t")
        print("\n")
    
    cursor.close()
    print ("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Phase1:The Health Center Server has port number: %s and IP address: %s "% (serverPort, serverHost))
    ThreadServer(serverHost, serverPort).listen()






