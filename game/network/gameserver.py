import socket, threading
import socketserver
import signal
import sys
import logging

import session
import telnet
import assets

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class TelnetHandler(telnet.NVTBaseClass):
    """
        Class to handle Telnet commands and emulate a telnet NVT for the client.
    """
    pass

class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        logging.info("{} connected.".format(self.client_address))
        # Create a new Session instance to handle this client's game
        gamesession = session.Session(self.client_address)
        #telnethandler = TelnetHandler()

        self.connected = True
        self.cur_thread = threading.current_thread()

        # Handle user login
        login = False
        self.request.sendall(assets.welcome_message)
        self.request.sendall("Authenticate with your username and password.\n Enter 'NEW' as username to register as a new user.\n")
        self.request.sendall("Username: ")
        state = "username"

        username = ""
        password = ""

        while login is False:
            # Get data from user
            data = self.rfile.readline()
            if not data:
                logging.info("{} closed the connection.")
                break
            data = data.strip()

            if state is "username":
                username = data
                state = "password"
                self.request.sendall("Password: ")

            if state is "password":
                password = data
                state = "authenticate"

            if state is "authenticate":
                success = gamesession.authenticate(username, password)
                if success:
                    self.request.sendall("Authentication successful.")
                    login = True
                else:
                    self.request.sendall("Couldn't authenticate. Incorrect username or password.")
                    state = "username"
                    self.request.sendall("\nUsername: ")



        while self.connected:
            # grab data
            self.data= self.rfile.readline()

            # End the thread if the client has closed the connection
            if not self.data:
                logging.info("{} closed the connection.")
                break

            self.data = self.data.strip() # Remove whitespace
            logging.debug("{} sent: {}".format(self.client_address, self.data))

            # Handle telnet commands

            # Pass the player input to the gamesession object to create a response
            response = gamesession.handle_input(self.data)

            # Send the response back to the player
            self.request.sendall(response)

        # Close the server at the end of the session
        self.server_close()

class GameServer:
    """
        Class that handles all network connections to the active socket.
        When a client makes a new connection, the listener spins off a
        new thread to handle that client.
    """
    def __init__(self, host, client_port, control_port = 111, debug = False):
        self.host = host
        self.client_port = client_port
        self.control_port = control_port

        # Setup logging
        loglevel = logging.INFO
        if debug:
            loglevel = logging.DEBUG
        logging.basicConfig(level = loglevel)


        # Setup the socketserver and the server thread
        self.server = ThreadedTCPServer((self.host, self.client_port), RequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

        self.active_sessions = [] #maybe not strictly necessary to keep track

        signal.signal(signal.SIGINT, self._signal_handler) # Handle SIGINT (ctr-c) to shutdown the server

    def run_server(self):
        logging.info("Starting GameServer.")
        self.server_thread.start()
        logging.info("Server running in thread: {}".format(self.server_thread.current_thread()))

    def _signal_handler(self, signal, frame):
        logging.info("Shutting down GameServer.")
        self.server.shutdown()

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 23

    server = GameServer(HOST, PORT, debug = True)
    server.run_server()