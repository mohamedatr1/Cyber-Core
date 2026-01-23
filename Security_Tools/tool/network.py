import argparse
from tools.extract_ip import extract_ip
from tools.scan_paths import scan_paths
from tools.status_code import status_code

parser = argparse.ArgumentParser(description="Python Network Tools")
parser.add_argument("command",choices=["ip","paths","status_code"],help = "Command Tools Run") 
args = parser.parse_args()

if args.command == "ip":
    extract_ip()
if args.command == "paths":
    scan_paths()
if args.command == "status_code":
    status_code()
