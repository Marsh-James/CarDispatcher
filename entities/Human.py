class human:
    def __init__(
            self,
            start_x: int,
            start_y: int,
            final_x: int,
            final_y: int,
            earliest_start: int,
            latest_finish: int,
    ):
        self.start_x = start_x
        self.start_y = start_y
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.distance = self.get_distance(final_x, final_y)
        self.on_time = False

    # math for earliest pickup points gain
    def get_distance(self, final_x, final_y):
        return abs(final_x - self.start_x) + abs(final_y - self.start_y)
