# Logic Obfuscation Project

## Members: Megan Stanton, Jessica Stevens, Kishan Tailor


### Command Line Instructions for Each Program
#### Calculating Fault Impact (from main repository)
	cd faultImpact  
	python3 faultAnalysis.py c17.fault > c17.faultImpact 
	python3 faultAnalysis.py c1908.fault > c1908.faultImpact
	python3 faultAnalysis.py c3540.fault > c3540.faultImpact

#### Replacing Gates (from main repository)
##### Replace # By Number Of Gates Wanted
	cd replaceGates
	python3 replaceGates.py c17Netlist.txt c17.faultImpact # > c17EncNetlist.txt
	python3 replaceGates.py c1908Netlist.txt c1908.faultImpact # > c1908EncNetlist.txt
	python3 replaceGates.py c3540Netlist.txt c3540.faultImpact # > c3540EncNetlist.txt

#### Converting Netlist to VHDL (Encrypted Versions) (from main repository)
##### Unencrypted Netlists are already converted and included in the "VHDL_Files" folder
	python3 EncNLtoEncVHDL.py EncNetlists/c17EncNetlist.txt > EncVHDL_Files/c17VHDLEnc.txt
	python3 EncNLtoEncVHDL.py EncNetlists/c1908EncNetlist.txt > EncVHDL_Files/c1908VHDLEnc.txt
	python3 EncNLtoEncVHDL.py EncNetlists/c3540EncNetlist.txt > EncVHDL_Files/c3540VHDLEnc.txt

### How to Move Files From "replaceGates" to "EncNetlists" (from main repository)
	cp replaceGates/c17EncNetlist.txt EncNetlists
	cp replaceGates/c1908EncNetlist.txt EncNetlists
	cp replaceGates/c3540EncNetlist.txt EncNetlists

	Can Also Do:
	cp replaceGates/c17EncNetlist.txt EncNetlists/someothername
	cp replaceGates/c1908EncNetlist.txt EncNetlists/someothername
	cp replaceGates/c3540EncNetlist.txt EncNetlists/someothername




