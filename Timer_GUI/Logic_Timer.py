class TimerModel:
    def __init__(self):
        self.seconds_left = 0
        self.is_running = False

    def set_time(self, seconds):
        self.seconds_left = seconds
        self.is_running = True

    def tick(self):
        if self.seconds_left > 0:
            self.seconds_left -= 1
            return True
        self.is_running = False
        return False