import socket, threading

class InterfaceServer:
    """
        Class that handles all network connections to the active socket.
        When a client makes a new connection, the listener spins off a
        new thread to handle that client.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

        self.active_sessions = [] #maybe not strictly necessary to keep track
        self.listen()

    def listen(self):
        self.sock.listen(5)
        while True:
            # Handle new connections
            client, address = self.sock.accept()
            client.settimeout(60) # client will timeout after 60 seconds... need to change
            self.new_session(client, address)

            # Clean up closed connections
            for i, session in enumerate(self.active_sessions):
                if session.is_alive() is not True:
                    self.active_sessions = del self.active_sessions[i]


    def new_session(self, client, address):
        """
            Creates a new session and appends it to the list of
        """
        session = SessionDaemon(client, address)
        session.start()
        self.active_sessions.append(session)

        return True


        

class SessionDaemon(threading.Thread):
    """
        Each individual active session has its own threaded daemon that
        handles network interfacing for the duration of that session.
    """
 
    def __init__(self, client, address, bufsize = 1024):
        threading.Thread.__init__(self, daemon = True)
        self.client = client
        self.address = address
        self.bufsize = bufsize

        self.lock = threading.Lock()
        self.welcome_message = "Hello"

        self.player = None
    
    def help_menu(self):
        """
            Print out the help menu.
        """
        data = \
        " \
        "

    def handle_command(self, command, arguments = None):
        """
            Handles a valid command by the user.
        """

    def handle_login(self):
        """
            Handles user login and new player creation
        """
        # Display welcome message
        self.client.send(self.welcome_message)

        self.client.send("USER AUTHENTICATION\nEnter username. For new users, enter \"NEW\".")
        try:
            data = 
    def run(self):
 
        
 
        # Handle user login

        while True:
            # wait for user to send data
            data = self.client.recv(self.bufsize)
            
            # handle menu alterantives and set proper return message
            if data[0] == '1':
                play_sound()
                data = 'The place looks the same as before\n'
                # execute some function
            elif data[0] == '2':
                open_window()
                data = 'I feel a chilly wind\n'
                # execute some other function
            elif data[0] == '3':
                break;
            else:
                data = welcome_message
 
            # send the designated message back to the client
            self.socket.send(data);
 
        # close connection
        self.socket.close()