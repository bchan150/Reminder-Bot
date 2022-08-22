import os

class Events:
    def __init__(self):
        file = open("events.txt", "r")
        Lines = file.readlines()
        self.events = []
        for line in Lines:
            self.events.append(line)
        file.close()

    def eventList(self):
        return self.events

    def check(self):
        if os.stat("events.txt").st_size != 0:
            return True

    def eventWrite(self):
        file = open("events.txt", "w")
        for event in self.events:
            file.write(event)
        
        file.close()

    def eventAdd(self, input):
        self.events.append(input + "\n")
        self.eventWrite()

    def eventDelete(self, input):
        self.events.pop(input)
        self.eventWrite()
