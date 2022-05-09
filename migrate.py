#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse

def main():
	parser = argparse.ArgumentParser(description="Migrācijas prototips")
	parser.add_argument('-i',dest='Xen_input',  help="Xen servera adrese")
	parser.add_argument('-p',dest='password',  help="Xen servera parole")
	parser.add_argument('-vm',dest='selected_VM', help="Xen servera Virtuālās mašīnas nosaukums")
	parser.add_argument('-P',dest='VMWare_Input',  help="VMWare servera adrese")
	parser.add_argument('-O',dest='VM_output_name',  help="Pārtaisītās KVM virtuālās mašīnas formāta nosaukums")
	args = parser.parse_args()
	xen_input = args.Xen_input
	password  = args.password
