class TVController:
    def __init__(self, channels):
        self.ch = {x: y for x, y in zip(range(1, len(channels) + 1), channels)}
        self.n = len(channels)
        self.current = self.ch[1]

    def first_channel(self):
        self.current = self.ch[1]
        return self.ch[1]

    def last_channel(self):
        self.current = self.ch[self.n]
        return self.ch[self.n]

    def turn_channel(self, number):
        self.current = self.ch[number]
        for key, value in (self.ch).items():
            if number == key:
                return value

    def next_channel(self):
        for key, value in (self.ch).items():
            if value == self.current:
                if self.ch[key] == self.n:
                    self.current = self.ch[1]
                    return self.ch[1]
                else:
                    self.current = self.ch[key + 1]
                    return self.ch[key + 1]

    def previous_channel(self):
        for key, value in (self.ch).items():
            if value == self.current:
                if self.ch[key] == 1:
                    self.current = self.ch[self.n]
                    return self.ch[self.n]
                else:
                    self.current = self.ch[key - 1]
                    return self.ch[key - 1]

    def current_channel(self):
        return self.current

    def is_exist(self, name):
        for key, value in (self.ch).items():
            if key == name or value == name:
                return "Yes"
            else:
                return "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
