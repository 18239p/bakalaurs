#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse

#Pseudocode:
#def virt-v2v(Xen_input, password,selected_VM)
#subprocess.run('[virt-v2v, Xen_input, password, selected_VM]', shell=True, capture_output=True,text=True)
#

#Pseudocode
#def ssh
#subprocess.run('[scp, VMWare_Input, VMWare_Password, selected_VM, vmware root dir',shell=True, capture_output=True,text=True)

#pseudocode
#qemu-img -f qcow2 -O vmdk selected_VM.qcow2 selected_VM.vmdk
#subprocess.run('[qemu-img,  selected_VM.qcow2, -O selected_VM(.vmdk)]',shell=True,capture_output=True,text=True)

def main():
	parser = argparse.ArgumentParser(description="Migrācijas prototips")
	parser.add_argument('-i',dest='Xen_input',  help="Xen servera adrese")
	parser.add_argument('-p',dest='password',  help="Xen servera parole")
	parser.add_argument('-vm',dest='selected_VM', help="Xen servera Virtuālās mašīnas nosaukums")
	parser.add_argument('-P',dest='VMWare_Input',  help="VMWare servera adrese")
	parser.add_argument('-vP',dest='VMWare_Password', help="VMWare servera parole")
	parser.add_argument('-O',dest='VM_output_name',  help="Pārtaisītās KVM virtuālās mašīnas formāta nosaukums")
	args = parser.parse_args()
	xen_input      = args.Xen_input
	password       = args.password
	selected_VM    = args.selected_VM
	VMWare_Input   = args.VMWare_Input
	VM_output_name = args.VM_output_name

