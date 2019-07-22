"""
Author: Peeyush Kushwaha
Usage instructions:
    1. Install SimpleWebsocketServer using the command `sudo pip install git+https://github.com/dpallot/simple-websocket-server.git`
    2. run server via python -i server.py and in the commandline and try to send a message using sendToClient function or in your own file do `from server import sendToClient`
    3. Run the client directory on localhost somehow. I'm using npm's reload package
"""

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import json
import eventing
import time
import datetime

clients = []

def noop():
    print("noop called")

handler = noop

def setHandler(h): 
    global handler
    handler = h

# to be filled by the importing module

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        global clients

        clients.append(self)
        print(self.address, 'connected')
        handler()

    def handleClose(self):
        global clients

        clients.remove(self)
        print(self.address, 'closed')

def websock_server():
    global server

    server = SimpleWebSocketServer('', 8765, SimpleEcho)
    server.serveforever()


def sendToClient(msg):
    for c in clients:
        c.sendMessage(msg)

def sendJSON(o):
    sendToClient(json.dumps(o))

def scheduled(): # runs in own thread
    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        job = eventing.jobs.get()

        if (job[0] < now + datetime.timedelta(seconds = 1)):
            sendJSON(job[1])
        else:
            eventing.jobs.put(job)

serverThread = threading.Thread(target = websock_server)
serverThread.daemon = True
serverThread.start()

scheduledThread = threading.Thread(target = scheduled)
scheduledThread.daemon = True
scheduledThread.start()
