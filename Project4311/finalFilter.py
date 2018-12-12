
#filter object, used to filter out protocol fields
class filter:

    #New session object as defined within the srs and sdd
    def __init__(self, name, expression):
        self.filterName = name
        self.expression = expression

    #returns name of current filter
    def getName(self):
        return self.filterName

    #returns expression of current filter
    def getExpression(self):
        return self.expression

    #change filter name
    def changeName(self,newName):
        self.name = newName

    #change expression of filter
    #might not be needed tbh
    def changeExpression(self, newExpression):
        self.expression = newExpression

    #is filtering out done here?
    #or is this just an object that holds the filters to be used somewhere else







#imports for gtk GUI, unused at the moment
#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk


#goes at the end
#unused during this version
#sessionBuilder = Gtk.Builder()
#sessionBuilder.add_from_file("Session_GUI.glade") #placeholder at the moment
#sessionBuilder.connect_signals(Session())

#window = sessionBuilder.get_object("window1")
#window.show_all()

#Gtk.main()