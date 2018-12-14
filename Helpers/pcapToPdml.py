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
import os.path
def pcapToPdmlConverter(dissectorPath, pcapPath, workspacePath):
    #dissectorPath = "C:\\Program Files\\Wireshark\\tshark.exe"
    #pcapPath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\lightweightTest.pcap"
    #Please be careful that this location points to a folder and ends with "\\"
    #workspacePath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\"
    pdmlPath = workspacePath+"PDMLDoc.pdml"
    if os.path.isfile(pdmlPath):
        return pdmlPath

    process = subprocess.Popen([dissectorPath, "-r", pcapPath, "-T", "pdml"], stdout=subprocess.PIPE)
    pdml = open(pdmlPath, "wb")
    pdml.write(process.stdout.read())
    pdml.close()

    return pdmlPath

def nodeSequenceFromPDML(dissectorPath, pcapPath, workspacePath):
    pdmlPath = pcapToPdmlConverter(dissectorPath, pcapPath, workspacePath)
    pdml = open(pdmlPath, "r")
    root = ET.fromstring(pdml.read())

    nodeList = []

    for proto in root.iter('proto'):
        tempNode = {
            "name": proto.attrib['name']
        }
        nodeList.append(tempNode)
    return nodeList

def fullInformationFromPDML(dissectorPath, pcapPath, workspacePath):
    pdmlPath = pcapToPdmlConverter(dissectorPath, pcapPath, workspacePath)
    pdml = open(pdmlPath, "r")
    root = ET.fromstring(pdml.read())

    nodeDictionary = {}

    for proto in root.iter('proto'):
        currentNode = {}
        for key in proto.attrib:
            currentNode[key] = proto.attrib[key]
        nodeDictionary[proto.attrib['name']] = currentNode
    return nodeDictionary
