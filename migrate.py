#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse

def main():
	parser = argparse.ArgumentParser(description="Migrācijas prototips")
	parser.add_argument('-i', help="XEN servera adrese")
	parser.add_argument('-p', help="Xen servera parole")
