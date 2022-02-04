from abc import ABCMeta, abstractmethod
import os
from argument import args

ListScan = {"PortScan": '1', "PortScanNoPing": '2', "ScanMachinNetwork": '3'}

def checkOperator(numberOperation: str):
	if numberOperation == ListScan.get('PortScan'):
            ScanNmap(PortScan, args.Url)
	elif numberOperation == ListScan.get('PortScanNoPing'):
            ScanNmap(PortScanNoPing, args.Url)
	elif numberOperation == ListScan.get('ScanMachinNetwork'):
            ScanNmap(ScanMachinNetwork, args.Url)
	else:
            print(color.CRED + 'Error please for help -h' + color.CEND)
            
class NmapInterfaceBase(ABCMeta):

    @abstractmethod
    def operator(self):
        pass


class PortScan(NmapInterfaceBase):

    def operator(self, url):
        os.system("nmap " + url)


class PortScanNoPing(NmapInterfaceBase):

    def operator(self, url):
        os.system("nmap -Pn " + url)


class ScanMachinNetwork(NmapInterfaceBase):

    def operator(self, url):
        os.system("nmap -sn " + url + '/24')


class ScanNmap:
    nmap = None

    def __init__(self, NmapInterfaceBase, url):
        self.nmap = NmapInterfaceBase
        self.nmap.operator(self, url)
