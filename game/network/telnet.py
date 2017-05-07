
commands = {
                "SE": bytes(240),                   # End of subnegotiation parameters.
                "NOP": bytes(241),                  # No operation.
                "Data Mark": bytes(242),            # The data stream portion of a Synch. This should always be accompanied by a TCP Urgent notification.
                "Break": bytes(243),                # NVT character BRK.
                "Interrupt Process": bytes(244),    # The function IP.
                "Abort output": bytes(245),         # The function AO.
                "Are You There": bytes(246),        # The function AYT.
                "Erase character": bytes(247),      # The function EC.
                "Erase Line": bytes(248),           # The function EL.
                "Go ahead": bytes(249),             # The GA signal.
                "SB": bytes(250),                   # 
                "WILL": bytes(251),
                "WON'T": bytes(252),
                "DO": bytes(253),
                "DON'T": bytes(254),
                "IAC": bytes(255)   # Interpret as Command - Must prepend any of the above commands for the command to be valid

}


class NVTBaseClass:
    """
        Base class for a Network Virtual Terminal. Emulates the standard Telnet NVT interface.
    """

    def IP(self):
        """
            Interrupt Process.
        """
        pass

    def AO(self):
        """
            Abort Output.
        """
        pass

    def AYT(self):
        """
            Are You There.
        """
        pass

    def EC(self):
        """
            Erase Character
        """
        pass

    def EL(self):
        """
            Erase Line
        """
        pass

    def Synch(self):
        """
            Synch
        """
        pass



