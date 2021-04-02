

class Timer:
    def __init__(self, window, typeview):
        self.typeview = typeview
        self.window = window
        self.time = 5

    def restart(self):
        self.time = 5
        
    def run(self):
        if self.time > 0:
            self.time -= 1
            self.window.after(1000, self.run)
        else:
            self.typeview.delete_all()

    def get_time(self):
        return self.time
