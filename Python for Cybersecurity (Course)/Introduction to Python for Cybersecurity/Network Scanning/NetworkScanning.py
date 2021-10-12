#pip install --pre scapy[basic] (use this command to install scapy)
from scapy.all import *

ports = [25,80,53,443,445,8080,8443]
def SynScan(host):
    ans,unans = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].cport == r[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(sport=5555,dport=54)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans:
        print("DNS Server at %s"%host)

host = input("What is the host ip: ")

SynScan(host)
DNSScan(host)
