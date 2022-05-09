#!/usr/bin/env python3

#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse
import subprocess
#Pseudocode:
# virt-v2v -ic 'xen+ssh://root@xen.example.com' -ip password Guest_name
def virt_v2v(Xen_input,Xen_password,selected_VM):
	virt_result=subprocess.run(['virt-v2v', Xen_input, Xen_password, selected_VM], shell=True, capture_output=True,text=True)
	return virt_result.stdout
#

#Pseudocode:
# scp selected_VM.vmdk root@vm.wa.re.address /sshrootdir/ 
def scp (VMWare_Input,VMWare_Password,selected_VM):
	scp_result=subprocess.run(['scp', VMWare_Input, VMWare_Password, selected_VM], '/',shell=True, capture_output=True,text=True)
	return scp_result.stdout
#

#Pseudocode:
# qemu-img -f qcow2 -O vmdk selected_VM.qcow2 selected_VM.vmdk
def qemu_img(selected_VM):
	Qemu_result=subprocess.run(['qemu-img', '-f qcow2 -O vmdk', selected_VM+'.qcow2', selected_VM+'.vmdk'],shell=True,capture_output=True,text=True)
	return Qemu_result.stdout
#ienākošie mainīgie
parser = argparse.ArgumentParser(description="Migrācijas prototips")
parser.add_argument('-i',dest='Xen_input',  help="Xen servera adrese", required=True)
parser.add_argument('-p',dest='Xen_password',  help="Xen servera parole", required=True)
parser.add_argument('-vm',dest='selected_VM', help="Xen servera Virtuālās mašīnas nosaukums", required=True)
parser.add_argument('-P',dest='VMWare_Input',  help="VMWare servera adrese", required=True)
parser.add_argument('-vP',dest='VMWare_Password', help="VMWare servera parole", required=True)
parser.add_argument('-O',dest='VM_output_name',  help="Pārtaisītās KVM virtuālās mašīnas formāta nosaukums", required=True)

#ienākošo mainīgo piešķiršana/main logic
def main():
	args = parser.parse_args()
	Xen_input      = args.Xen_input
	Xen_password   = args.Xen_password
	selected_VM    = args.selected_VM
	VMWare_Input   = args.VMWare_Input
	VM_output_name = args.VM_output_name
if __name__ == '__main__':
	main()
	#1.
	#virt-v2v
	virt_v2v(Xen_input,Xen_password,selected_VM)
	print(virt_v2v)
	qemu_img()
	print(qemu_img)
	#2.
	#qemu_img
	#3.
	#scp
