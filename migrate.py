#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse

def main():
	parser = argparse.ArgumentParser(description="Migrācijas prototips")
	parser.add_argument('-i', help="Xen servera adrese")
	parser.add_argument('-p', help="Xen servera parole")
	parser.add_argument('-vm', help="Xen servera Virtuālās mašīnas nosaukums")
	parser.add_argument('-P',help="VMWare servera adrese")
	parser.add_argument('-O', help="Pārtaisītās KVM virtuālās mašīnas formāta nosaukums")
