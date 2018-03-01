class human:
    def __init__(self, on_time):
        self.pos_x = 0
        self.pos_y = 0
        self.earliest_start = 0
        self.latest_finish = 0
        self.distance = 0
        self.points_obtained = 0
        self.on_time = on_time

    # math for earliest pickup points gain
    def get_distance(self, final_x, final_y):
        self.distance = abs(final_x - self.pos_x) + abs(final_y - self.pos_y)
