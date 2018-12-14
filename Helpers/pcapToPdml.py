#tshark commands
#To capture test data:
#tshark -w filename.pcap -F libpcap
#To convert pcap to PDML
#tshark -r inputFile.pcap -T pdml > outputFile.pdml

#dissectorPath: Path to the dissector executable
#Example: C:\Program Files\Wireshark\tshark.exe
#pcapPath: Path to the pcap file
#Example: C:\Users\currentUser\Desktop\SE2-Team-3-Net-Tool\test.pcap
#workspacePath: Path to the workspace where the pdml document should be stored
#Example: C:\Users\currentUser\Desktop\SE2-Team-3-Net-Tool\
#Mind the "\"!

import subprocess
import xml.etree.ElementTree as ET
def pcapToPdmlConverter(dissectorPath, pcapPath, workspacePath):
    #dissectorPath = "C:\\Program Files\\Wireshark\\tshark.exe"

    #pcapPath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\lightweightTest.pcap"

    #Please be careful that this location points to a folder and ends with "\\"
    #workspacePath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\"
    process = subprocess.Popen([dissectorPath, "-r", pcapPath, "-T", "pdml"], stdout=subprocess.PIPE)
    finalPath = workspacePath+"PDMLDoc.pdml"
    pdml = open(finalPath, "wb")
    pdml.write(process.stdout.read())
    pdml.close()

    pdml = open(finalPath, "r")
    root = ET.fromstring(pdml.read())

    #XML documentation for python
    #https://docs.python.org/2/library/xml.etree.elementtree.html
    return root
