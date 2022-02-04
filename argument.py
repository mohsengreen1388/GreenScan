import argparse

ListSoftware = {"Nmap": '1', "Ping": '2'}

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--List", help="list scan")
parser.add_argument("-u", "--Url", help="url target")
args = parser.parse_args()
