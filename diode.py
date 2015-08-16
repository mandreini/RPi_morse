import time

class Diode(object):
    """This will control the state of the light (on/off)"""

    def __init__(self):
        
        self.time_factor = 0.5  # s
        self.times = {
            "s": 1,
            "l": 3,
            "d": 1,
            "l": 3,
            "w": 7
            }

        self.t_start = time.time()
        self.light_on = False
        
        self.morse_message = None
        self.curr_letter = None
        self.curr_output = None

    @staticmethod
    def _gen_message(morse_message):
        """Creates a generator for the morse_message"""
        word_msg = "w".join(morse_message)
        letter_msg = "d".join(word_msg)

        for l in letter_msg:
            yield l

    def set_message(self, morse_message):
        """Initializes the message (other than None)"""
        self.morse_message = self._gen_message(morse_message)
        first_output = self.morse_message.send(None)
        self.curr_output = self.times[first_output]
        self.curr_output = int(self.curr_output)

    def update(self):
        t = time.time()
        dt = t - self.t_start
        factored_time = dt / self.time_factor

        if dt < self.curr_output: return

        self.t_start = t
        self.light_on = not self.light_on
        next_val = self.morse_message.send(None)
        self.curr_output = self.times[next_val]
        self.curr_output = int(self.curr_output)
        

        

        
