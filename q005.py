class stringer(object):
  def __init__(self):
    self.s = ""
  def getString(self):
    self.s = input()
  def printString(self):
    print(self.s)

S = stringer()
S.getString()
S.printString()