import datetime #for timestampts and date

class PDML:

    #creates a new session object that does not yet contain any data enclosed within it
    #need something for packets?
    def __init__(self):
        self.name = ""
        self.description = ""
        self.timestampt = datetime.datetime.now()
        self.analystsName = ""
        self.date  = datetime.datetime.now().date()
        self.stage = ""

    def editName(self,newName):
        self.name = newName

    def editDecription(selfself,newDesc):
        self.decription = newDesc

    def editAnalyst(self,newAnalysts):
        self.analystsName = newAnalysts

    def editStage(self,newStage):
        self.stage = newStage
