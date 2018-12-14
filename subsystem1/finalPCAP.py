import subprocess
import xml.etree.ElementTree as ET

#need to write down exactly what the session needs to do !!!
class PCAP:

    #creates a new session object that does not yet contain any data enclosed within it
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath

    def editName(self,newName):
        self.name = name

    #called via arlPCAP.convertToPDML(dissectorLocation, WorkspaceLocation)
    #pcapPath specified when PCAP object created
    #workspace location used for storing file
    def convertToPdml(self, dissectorPath, workspacePath):
        dissectorPath = "C:\\Program Files\\Wireshark\\tshark.exe"

        pcapPath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\lightweightTest.pcap"

        #below should be the one used once debugging is finished
        #pcapPath = self.filepath

        # Please be careful that this location points to a folder and ends with "\\"
        workspacePath = 'C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\'
        process = subprocess.Popen([dissectorPath, "-r", pcapPath, "-T", "pdml"], stdout=subprocess.PIPE)
        finalPath = workspacePath + "PDMLDoc.pdml"
        pdml = open(finalPath, "wb")
        pdml.write(process.stdout.read())
        pdml.close()

        pdml = open(finalPath, "r")
        root = ET.fromstring(pdml.read())

        # XML documentation for python
        # https://docs.python.org/2/library/xml.etree.elementtree.html
        return root


