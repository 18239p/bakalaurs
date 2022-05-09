#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse
import subprocess
#Pseudocode:
# virt-v2v -ic 'xen+ssh://root@xen.example.com' -ip password Guest_name
def virt_v2v(xen_input,xen_password,selected_VM):
	subprocess.run(['virt-v2v', xen_input, xen_password, selected_VM], shell=True, capture_output=True,text=True)
#

#Pseudocode:
# scp selected_VM.vmdk root@vm.wa.re.address /sshrootdir/ 
def scp (VMWare_Input,VMWare_Password,selected_VM):
	subprocess.run(['scp', VMWare_Input, VMWare_Password, selected_VM], '/',shell=True, capture_output=True,text=True)
#

#Pseudocode:
#qemu-img -f qcow2 -O vmdk selected_VM.qcow2 selected_VM.vmdk
def qemu_img(selected_VM):
	subprocess.run(['qemu-img', '-f qcow2 -O vmdk', selected_VM+'.qcow2', selected_VM+'.vmdk'],shell=True,capture_output=True,text=True)

#ienākošie mainīgie
parser = argparse.ArgumentParser(description="Migrācijas prototips")
parser.add_argument('-i',dest='Xen_input',  help="Xen servera adrese")
parser.add_argument('-p',dest='Xen_password',  help="Xen servera parole")
parser.add_argument('-vm',dest='selected_VM', help="Xen servera Virtuālās mašīnas nosaukums")
parser.add_argument('-P',dest='VMWare_Input',  help="VMWare servera adrese")
parser.add_argument('-vP',dest='VMWare_Password', help="VMWare servera parole")
parser.add_argument('-O',dest='VM_output_name',  help="Pārtaisītās KVM virtuālās mašīnas formāta nosaukums")

#ienākošo mainīgo piešķiršana/galvenā loģika
if __name__ == '__main__':
	args = parser.parse_args()
	xen_input      = args.Xen_input
	xen_password   = args.Xen_password
	selected_VM    = args.selected_VM
	VMWare_Input   = args.VMWare_Input
	VM_output_name = args.VM_output_name

