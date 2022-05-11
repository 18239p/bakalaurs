#!/usr/bin/env python3

#nepieciešams pārbaudīt visi /usr/bin programmas ir
#virt-tools
#Debian -> sid
#apt install libguestfs-tools/curl?
#
#pseudocode : /usr/bin

#Python programma
#Pseudocode : python -> spawn bash shell -> virt-v2v [args] -> qemu-img [args] -> scp [args]
#
import argparse
import subprocess
import os.path

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
	filepath='/usr/bin/'
	if (filepath+'virt-v2v'):
		print(cGRN+"virt-v2v found"+e)
		if(filepath+'qemu-img'):
			print(cGRN+"qemu-img found"+e)
			if(filepath+'scp'):
				print(cGRN+"scp found!"+e)
			else:
				print(cRED+"scp not found!?"+e+quit())
		else:
			print(cRED+"qemu-img not found!"+e+quit())
		
	else:
		print(cRED+"virt-v2v not found!"+e+quit())
			


#Pseudocode:
# virt-v2v -ic 'xen+ssh://root@xen.example.com' -ip password Guest_name
def virt_v2v(Xen_input,Xen_password,selected_VM):
	virt_result=subprocess.run(['virt-v2v',
	Xen_input,						# ievade priekš XEN lietotāja
	Xen_password,						# ievade priekš XEN paroles
	selected_VM], shell=True, capture_output=True,text=True)
	return virt_result.stdout				# rezultātu izvade
#

#Pseudocode:
# scp selected_VM.vmdk root@vm.wa.re.address /sshrootdir/ 
def scp (VMWare_Input,VMWare_Password,selected_VM):
	scp_result=subprocess.run(['scp',
 	VMWare_Input,						# ievade priekš VMWare lietotājvārda
	VMWare_Password,					# ievade priekš VMWare paroles
	selected_VM], '/',shell=True, capture_output=True,text=True)
	return scp_result.stdout				# rezultātu izvade
#

#Pseudocode:
# qemu-img -f qcow2 -O vmdk selected_VM.qcow2 selected_VM.vmdk
def qemu_img(selected_VM):
	Qemu_result=subprocess.run(['qemu-img', '-p -f qcow2 -O vmdk',
	selected_VM+'.qcow2',					# virtuālās mašīnas nosaukums
	selected_VM+'.vmdk'],shell=True,capture_output=True,text=True)
	return Qemu_result.stdout				# izvada rezultātu no konvertācijas
#ienākošie mainīgie
parser = argparse.ArgumentParser(description=cPURP+"Bakalaura darba prototipa programma VM migrācijai"+e)
parser.add_argument('-i',dest='Xen_input',  help=cRED+" Nepieciešams: "+e+"Xen servera adrese", required=True)
parser.add_argument('-p',dest='Xen_password',  help=cRED+" Nepieciešams: "+e+"Xen servera parole", required=True)
parser.add_argument('-vm',dest='selected_VM', help=cRED+" Nepieciešams: "+e+"Xen servera VM nosaukums", required=True)
parser.add_argument('-P',dest='VMWare_Input',  help=cRED+" Nepieciešams: "+e+"VMWare servera adrese", required=True)
parser.add_argument('-vP',dest='VMWare_Password', help=cRED+" Nepieciešams: "+e+"VMWare servera parole", required=True)
parser.add_argument('-O',dest='VM_output_name',  help=cRED+" Nepieciešams: "+e+"Pārtaisītās KVM VM formāta nosaukums", required=True)

def main():
	args = parser.parse_args()				# ienākošo mainīgo piešķiršana/main logic
	Xen_input      = args.Xen_input
	Xen_password   = args.Xen_password
	selected_VM    = args.selected_VM
	VMWare_Input   = args.VMWare_Input
	VM_output_name = args.VM_output_name
if __name__ == '__main__':
	main()
	filecheck()
	#1.
	#virt-v2v
	virt_v2v(Xen_input,Xen_password,selected_VM)		#izsauc virt-v2v no bash termināļa, skaitās kā child process
	print(virt_v2v)						#izvada funkcijas rezultātu
	#2.
	qemu_img(selected_VM)					#pārveido doto VM par .vmdk formātu
	print(qemu_img)						#izvada funkcijas rezultātu
	#3.
	scp(VMWare_Input,VMWare_Password,selected_VM)		#pārvieto doto VM uz VMWare servera
	#izvadīt progresu
