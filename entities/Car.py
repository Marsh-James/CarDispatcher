class car:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.turn_available = 0
        self.in_use = False

    # calculate turn available
    # set when car is in use
    def set_available(self):
        self.in_use = True

    def set_unavailable(self):
        self.in_use = False
