#!/usr/bin/env python3


#virt-tools
#Debian -> sid
#pseudocode : /usr/bin
#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
import argparse
import subprocess
import os.path
import os
#uzliekam VM
#virt-install --name=TestaVM --memory 1024 --vcpu 1 --disk Test_Pamateksemplara_VM.qcow2 --import --os-variant ubuntu20.04
#
# shutdown os
# https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-managing_guest_virtual_machines_with_virsh-shutting_down_rebooting_and_force_shutdown_of_a_guest_virtual_machine
 # virsh <connection> shutdown guest1 
#get color output
# ANSI Colors
cBLK  = "\033[1;30m"
cRED  = "\033[38;5;197m"
cGRN  = "\033[1;32m"
cYEL  = "\033[1;33m"
cBLUE = "\033[1;34m"
cMGNT = "\033[1;35m"
cCYAN = "\033[1;36m"
cWHT  = "\033[1;37m"
cPNK  = "\033[38;5;219m"
cPURP = "\033[38;5;141m"
e     = "\033[0m"
#pseudocode : /usr/bin/scp&&qemu-img&&virt-v2v
def filecheck():
	print(cYEL+"checking required files:"+e)
	filepath='/usr/bin/'									#pārbauda Linux direktorijā /usr/bin sekojošās programmas
	if (os.path.exists(filepath+'virt-v2v')):				#virt-v2v
		print(cGRN+"			virt-v2v found"+e)
		if(os.path.exists(filepath+'qemu-img')):			#qemu-img
			print(cGRN+"			qemu-img found"+e)
			if(os.path.exists(filepath+'scp')):				#scp
				print(cGRN+"			scp found!"+e)
			else:
				print(cRED+"			scp not found!?"+e)
				quit()
		else:
			print(cRED+"			qemu-img not found!"+e)
			quit()											#ja neatrod dotās programmas
		
	else:
		print(cRED+"			virt-v2v not found!"+e)
		print("Try installing "+cPNK+"libguestfs-tools"+e+" or "+cPNK+"virt-v2v"+e+"!")
		quit()												#python programma beidz darbību
#

#Pseudocode:
# virt-v2v -ic 'xen+ssh://root@xen.example.com' -ip password Guest_name
def virt_v2v(Xen_input,Xen_Password,selected_VM):
	virt_result=subprocess.run(['virt-v2v',
	Xen_input,												# ievade priekš XEN lietotāja
	Xen_Password,											# ievade priekš XEN paroles
	selected_VM], shell=True, capture_output=True,text=True)
	return virt_result.stdout								# rezultātu izvade
#

#Pseudocode:
# scp Testa_Pamateksemplara_VM.vmdk v[vmware username]@[vmware ip]:[vmware location] /C:/Users/V/Documents/
#scp file.txt remote_username@10.10.0.2:/remote/directory
def scp (VMWare_Input,selected_VM,VMWare_Address,Xen_SSH_Key):
	combinescpagain = 'scp '+selected_VM+'.vmdk '+' -i '+Xen_SSH_Key+' '+VMWare_Input+'@'+VMWare_Address+':/C:/Users/V/Documents/'
#	print(combinescpagain)
	scp_result=subprocess.run([combinescpagain],shell=True, capture_output=True,text=True)
	return scp_result.stdout								# rezultātu izvade
#

#Pseudocode:
# qemu-img -f qcow2 -O vmdk selected_VM.qcow2 selected_VM.vmdk
def qemu_img(selected_VM):
	combineqemu='qemu-img convert -p -f qcow2 -O vmdk ' +selected_VM+".qcow2"+' '+ selected_VM+".vmdk" 
#	print(combineqemu)
	Qemu_result=subprocess.run([combineqemu],shell=True,capture_output=True,text=True)
	return Qemu_result.stdout								# izvada rezultātu no konvertācijas
#

#Pseudocode:
#scp -i ssh_key.private user@server:/path/to/remotefile.zip /Local/Target/Destination
#scp -i nintendo toor@192.168.122.122:/home/toor/TestaVM.qcow2 /home/toor

def failsafe(Xen_input,Xen_address,VM_filepath,selected_VM,Xen_SSH_Key):
	combinescp = 'scp -i '+Xen_SSH_Key+' '+Xen_input+'@'+Xen_address+':'+VM_filepath+'/'+selected_VM+".qcow2"+' '+os.path.abspath(os.getcwd())
#	print(combinescp)
	failsafe=subprocess.run([combinescp],shell=True,capture_output=True,text=True)						#saglabājam esošajā datnē
	return failsafe.stdout									#izvadam rezultātu.

#

#ienākošie mainīgie
parser = argparse.ArgumentParser(description=cPURP+"Bakalaura darba prototipa programma VM migrācijai"+e)
parser.add_argument('-i',dest='Xen_input',  help=cRED+" Nepieciešams: "+e+"Xen servera lietotājvārds", required=True)
parser.add_argument('-iX',dest='Xen_SSH_Key',  help=cRED+" Nepieciešams: "+e+"Xen servera privātā ssh atslēga", required=True)
parser.add_argument('-p',dest='Xen_address',  help=cRED+" Nepieciešams: "+e+"Xen servera adrese", required=True)
parser.add_argument('-vm',dest='selected_VM', help=cRED+" Nepieciešams: "+e+"Xen servera VM nosaukums", required=True)
parser.add_argument('-xP',dest='Xen_Password',  help=cRED+" Nepieciešams: "+e+"Xen servera parole ", required=True)
parser.add_argument('-vmp',dest='VM_filepath', help=cRED+" Nepieciešams: "+e+"Xen servera VM atrašanās vieta", required=True)
parser.add_argument('-P',dest='VMWare_Input',  help=cRED+" Nepieciešams: "+e+"VMWare servera adrese", required=True)
parser.add_argument('-vPU',dest='VMWare_Address', help=cRED+" Nepieciešams: "+e+"VMWare servera lietotājvārds", required=True)
parser.add_argument('-O',dest='VM_output_name',  help=cRED+" Nepieciešams: "+e+"Pārtaisītās KVM VM formāta nosaukums", required=True)
parser.add_argument('-F',dest='Failsafe_mode',  help=cYEL+" Failsafe variants, palaist gadījumā ja virt-v2v neiet."+e, required=False, action="store_true", default=False)
if __name__ == '__main__':	
	args = parser.parse_args()
							# ienākošo mainīgo piešķiršana/main logic
	Xen_input      = args.Xen_input
	Xen_address    = args.Xen_address
	Xen_Password   = args.Xen_Password
	Xen_SSH_Key    = args.Xen_SSH_Key
	VM_filepath    = args.VM_filepath
	selected_VM    = args.selected_VM
	VMWare_Input   = args.VMWare_Input
	VM_output_name = args.VM_output_name
	VMWare_Address = args.VMWare_Address

	filecheck()
	#1.
	#virt-v2v
	if (args.Failsafe_mode):
		print(cMGNT+"Failsafe mode activated!"+e)
		failsafe(Xen_input,Xen_address,VM_filepath,selected_VM,Xen_SSH_Key)
		print(failsafe)
		print("To manually add and install migrated VM do the following steps :")
		print("virt-install --name=TestaVM --memory 1024 --vcpu 1 --disk Testa_Pamateksemplāra_VM.qcow2 --import --os-variant ubuntu20.04")
	else:
		virt_v2v(Xen_input,Xen_Password,selected_VM)
		print(virt_v2v)											#izvada funkcijas rezultātu
	#2.
	qemu_img(selected_VM)									#pārveido doto VM par .vmdk formātu
	print(qemu_img)											#izvada funkcijas rezultātu
	#3.
	scp(VMWare_Input,selected_VM,VMWare_Address,Xen_SSH_Key)			#pārvieto doto VM uz VMWare servera
	print(scp)#izvadīt progresu
