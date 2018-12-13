
#Do i take in the pdml or do I just send it to stage 2
class Session:

    #New session object as defined within the srs and sdd
    def __init__(self, name, description):
        self.SessionName = name
        self.description = description
        self.filterList = list()
        self.messageTypeList  = list()

    #Binds the given PDML to the session object
    #placeholder until we figure out how this works lol
    def addPDML(self,pdmlObject):
        self.sessionPDML = pdmlObject

    #add a messageType object to the session
    def addMessageType(self,messageType):
        self.messageTypeList.append(messageType)

    #add a filter object to the session
    def addFilter(self, filter):
        self.filterList.append(filter)






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
