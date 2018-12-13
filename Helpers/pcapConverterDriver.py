#For testing purposes
from pcapToPdml import pcapToPdmlConverter
def testPcapConversion():
    #If the tshark executable is not in your PATH environment variable, please specify the complete path to it
    #dissectorPath = "tshark"
    #Double "\" are used because \ escapes a character, double \ makes sure no character is escaped and the string's integrity is preserved
    dissectorPath = "C:\\Program Files\\Wireshark\\tshark.exe"

    pcapPath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\lightweightTest.pcap"

    #Please be careful that this location points to a folder and ends with "\\"
    workspacePath = "C:\\Users\\alien\\Desktop\\SE2-Team-3-Net-Tool\\"

    pcapToPdmlConverter(dissectorPath, pcapPath, workspacePath)
testPcapConversion()
