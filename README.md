# Logic Obfuscation Project

## Members: Megan Stanton, Jessica Stevens, Kishan Tailor

### Script Location and Purpose
NLtoVHDL.py -> Main Directory -> Convert Original Netlist to VHDL   
EncNLtoEncVHDL.py -> Main Directory -> Convert Encrypted Netlist to VHDL   
NLtoTB.py -> Main Directory -> Convert Any Netlist to Corresponding Testbench File   
NLtoExperimental -> Main Directory -> Not Completely Functional, Reduced Time Required to Make Experimental Files   
faultAnalysis.py -> faultImpact Folder -> Calculates Fault Impact Given Output From HOPE   
replaceGates.py -> replaceGates Folder -> Used to Insert Gates and Produce Encrypted Netlist   
FindObfuscation.py -> Obfuscated Folder -> Calculates Hamming Distance   

### Other Folders
EncNetlists -> Contains Encrypted Netlists Files for the 3 Circuits    
EncVHDL_Files -> Contains Encrypted VHDL Files for the 3 Circuits   
ExperimentalConstraints -> Contains the Constraint Files used in Experimental Testing   
Experimental VHDL -> Contains the VHDL Files used in Experimental Testing   
Netlists -> Contains Original Netlist Files for the 3 Circuits   
TB_Files -> Contains Testbench Files for the 3 Circuits Encrypted and Basic   
VHDL_Files -> Contains Original VHDL Files for the 3 Circuits   
simResults -> Contains the Simulation Results Outputted by the Testbench Files   

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

#### How to Move Files From "replaceGates" to "EncNetlists" (from main repository)
	cp replaceGates/c17EncNetlist.txt EncNetlists
	cp replaceGates/c1908EncNetlist.txt EncNetlists
	cp replaceGates/c3540EncNetlist.txt EncNetlists

	Can Also Do:
	cp replaceGates/c17EncNetlist.txt EncNetlists/someothername
	cp replaceGates/c1908EncNetlist.txt EncNetlists/someothername
	cp replaceGates/c3540EncNetlist.txt EncNetlists/someothername
	
#### Create Test Bench Files (Will have to do if Encrypted Circuits are changed)
	python3 NLtoTB.py Netlists/c17Netlist.txt > TB_Files/c17TB.txt 
	python3 NLtoTB.py Netlists/c1908Netlist.txt > TB_Files/c1908TB.txt
	python3 NLtoTB.py Netlists/c3540Netlist.txt > TB_Files/c3540TB.txt
	python3 NLtoTB.py EncNetlists/c17EncNetlist.txt > TB_Files/c17EncTB.txt
	python3 NLtoTB.py EncNetlists/c1908EncNetlist.txt > TB_Files/c1908EncTB.txt
	python3 NLtoTB.py EncNetlists/c3540EncNetlist.txt > TB_Files/c3540EncTB.txt

#### Calculate Hamming Distance
##### Place Simulation Results in Obfuscated/testFile.txt
	cd Obfuscated
	python3 FindObfucation.py



