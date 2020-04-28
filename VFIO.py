#!/usr/bin/python3
import subprocess
import sys


#Displays PCI deivces with VGA componets

def list_pci():
	pcidevice = subprocess.run(["lspci | grep VGA"], shell=True)
	for x in len(pcidevice):
		print(x)

list_pci()
#Functions to list the enabled CPU features for Virtulization
def ck_cpu():
	def list_cpu_AMD():
		CPU = subprocess.run(["dmesg | grep VT-d"], shell=True)
		CPU

	def list_cpu_INTEL():
		CPU = subprocess.run(["dmesg | grep AMD-Vi"], shell=True)
		CPU

	cputype = input("Is your CPU AMD or INTEL?")

	if cputype=="INTEL":
		list_cpu_INTEL()

	elif cputype=="AMD":
		list_cpu_AMD()

	else:
		print("Not a valid CPU")

ck_cpu()


