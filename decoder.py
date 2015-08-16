class Decoder(object):

    def __init__(self):
        self.msg_decoder = self._make_decoder()

    def _make_decoder(self):
        """
        Creates (and returns) a dictionary with the letter/number as key and
        morse code as value. Set for a-z and 0-9
        """
        
        decoder = {
            "a": "sl",
            "b": "lsss",
            "c": "lsls",
            "d": "lss",
            "e": "s",
            "f": "ssls",
            "g": "lls",
            "h": "ssss",
            "i": "ss",
            "j": "slll",
            "k": "lsl",
            "l": "slss",
            "m": "ll",
            "n": "ls",
            "o": "lll",
            "p": "slls",
            "q": "llsl",
            "r": "sls",
            "s": "sss",
            "t": "l",
            "u": "ssl",
            "v": "sssl",
            "w": "sll",
            "x": "lssl",
            "y": "lsll",
            "z": "llss",
            
            "1": "sllll",
            "2": "sslll",
            "3": "sssll",
            "4": "ssssl",
            "5": "sssss",
            "6": "lssss",
            "7": "llsss",
            "8": "lllss",
            "9": "lllls",
            "0": "lllll",
            }

        return decoder

    def decode_message(self, message):
        """
        Returns a list of the message in morse code. Case insensitive.
        Only supports a-z and 0-9
        """

        # Error handling
        if not isinstance(message, str):
            raise Exception("Message '", message, "' is not a string and cannot be converted to morse code.")

        message = message.lower()        
        decoder = self.msg_decoder
        allowed_chars = decoder.keys()
                            
        for char in message:
            if allowed_chars.__contains__(char) == -1 and char != " ":
                raise Exception("Invalid character %s in message" % char)

        # Decoding
        morse_msg = []
        for letter in message:
            if letter == " ":
                morse_msg.append("w")  # change this
            else:
                new_morse_letter = decoder[letter]
                morse_msg.append(new_morse_letter)

        return morse_msg
            
