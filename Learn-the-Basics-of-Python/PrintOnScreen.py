
class DisplayMsg:
    def __init__(self,pyFile):
        self.pyFile = pyFile
        msg = "--------------| " + pyFile + ".py |-----------------"
        print(msg)

    def see(self,message):
        print(f"PyFile : " + self.pyFile + ".py" + " | Message : " + message)





