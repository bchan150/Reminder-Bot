import time

class Refresh:
  def __init__(self):
    file = open("lastRun.txt", "r")
    self.fday = int(file.readline())
    self.current = time.localtime(time.time())
    file.close()

  # Checks to see if current day is different from the file day.
  # Returns true if different.
  def CheckDaily(self):
    if self.fday != self.current.tm_mday:
      return True
    return False

  # Writes to lastRun.txt to keep track of information.
  def WriteDay(self):
    file = open("lastRun.txt", "w")
    file.write(str(self.current.tm_mday))
    file.close()

  def CheckAll(self):
    self.WriteDay()
    return self.CheckDaily()
