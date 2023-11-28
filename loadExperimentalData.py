import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

Pc0 = 1000.0
Tc0 = 1000.0
Rc0 = 1.2

#======================================================
#Loading Isobars
#======================================================
with open('Data/isobars/22MPA_PLA_19E4_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_22MPA = range(0,numpts)
			T0_22MPA = range(0,numpts)
			R0_22MPA = range(0,numpts)
			M0_22MPA = range(0,numpts)
			I0_22MPA = range(0,numpts)
		if index1 >= 6:
			P0_22MPA[index2] = float(row[0])
			T0_22MPA[index2] = float(row[1])
			R0_22MPA[index2] = float(row[2])
			M0_22MPA[index2] = float(row[3])
			I0_22MPA[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1
		
P0 = P0_22MPA
T0 = T0_22MPA
R0 = R0_22MPA
M0 = M0_22MPA
I0 = I0_22MPA

with open('Data/isobars/40MPA_PLA_19E4_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_40MPA = range(0,numpts)
			T0_40MPA = range(0,numpts)
			R0_40MPA = range(0,numpts)
			M0_40MPA = range(0,numpts)
			I0_40MPA = range(0,numpts)
		if index1 >= 6:
			P0_40MPA[index2] = float(row[0])
			T0_40MPA[index2] = float(row[1])
			R0_40MPA[index2] = float(row[2])
			M0_40MPA[index2] = float(row[3])
			I0_40MPA[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_40MPA),axis=0)
T0 = npy.concatenate((T0,T0_40MPA),axis=0)
R0 = npy.concatenate((R0,R0_40MPA),axis=0)
M0 = npy.concatenate((M0,M0_40MPA),axis=0)
I0 = npy.concatenate((I0,I0_40MPA),axis=0)

with open('Data/isobars/60MPA_PLA_19E4_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_60MPA = range(0,numpts)
			T0_60MPA = range(0,numpts)
			R0_60MPA = range(0,numpts)
			M0_60MPA = range(0,numpts)
			I0_60MPA = range(0,numpts)
		if index1 >= 6:
			P0_60MPA[index2] = float(row[0])
			T0_60MPA[index2] = float(row[1])
			R0_60MPA[index2] = float(row[2])
			M0_60MPA[index2] = float(row[3])
			I0_60MPA[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_60MPA),axis=0)
T0 = npy.concatenate((T0,T0_60MPA),axis=0)
R0 = npy.concatenate((R0,R0_60MPA),axis=0)
M0 = npy.concatenate((M0,M0_60MPA),axis=0)
I0 = npy.concatenate((I0,I0_60MPA),axis=0)

'''
#======================================================
#Loading Isotherms
#======================================================

with open('Data/Isotherms/493K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_493K = range(0,numpts)
			T0_493K = range(0,numpts)
			R0_493K = range(0,numpts)
			M0_493K = range(0,numpts)
			I0_493K = range(0,numpts)
		if index1 >= 6:
			P0_493K[index2] = float(row[0])
			T0_493K[index2] = float(row[1])
			R0_493K[index2] = float(row[2])
			M0_493K[index2] = float(row[3])
			I0_493K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
		
P0 = P0_493K
T0 = T0_493K
R0 = R0_493K
M0 = M0_493K
I0 = I0_493K

with open('Data/Isotherms/473K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_473K = range(0,numpts)
			T0_473K = range(0,numpts)
			R0_473K = range(0,numpts)
			M0_473K = range(0,numpts)
			I0_473K = range(0,numpts)
		if index1 >= 6:
			P0_473K[index2] = float(row[0])
			T0_473K[index2] = float(row[1])
			R0_473K[index2] = float(row[2])
			M0_473K[index2] = float(row[3])
			I0_473K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_473K),axis=0)
T0 = npy.concatenate((T0,T0_473K),axis=0)
R0 = npy.concatenate((R0,R0_473K),axis=0)
M0 = npy.concatenate((M0,M0_473K),axis=0)
I0 = npy.concatenate((I0,I0_473K),axis=0)

with open('Data/Isotherms/453K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_453K = range(0,numpts)
			T0_453K = range(0,numpts)
			R0_453K = range(0,numpts)
			M0_453K = range(0,numpts)
			I0_453K = range(0,numpts)
		if index1 >= 6:
			P0_453K[index2] = float(row[0])
			T0_453K[index2] = float(row[1])
			R0_453K[index2] = float(row[2])
			M0_453K[index2] = float(row[3])
			I0_453K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_453K),axis=0)
T0 = npy.concatenate((T0,T0_453K),axis=0)
R0 = npy.concatenate((R0,R0_453K),axis=0)
M0 = npy.concatenate((M0,M0_453K),axis=0)
I0 = npy.concatenate((I0,I0_453K),axis=0)

with open('Data/Isotherms/433K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_433K = range(0,numpts)
			T0_433K = range(0,numpts)
			R0_433K = range(0,numpts)
			M0_433K = range(0,numpts)
			I0_433K = range(0,numpts)
		if index1 >= 6:
			P0_433K[index2] = float(row[0])
			T0_433K[index2] = float(row[1])
			R0_433K[index2] = float(row[2])
			M0_433K[index2] = float(row[3])
			I0_433K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_433K),axis=0)
T0 = npy.concatenate((T0,T0_433K),axis=0)
R0 = npy.concatenate((R0,R0_433K),axis=0)
M0 = npy.concatenate((M0,M0_433K),axis=0)
I0 = npy.concatenate((I0,I0_433K),axis=0)

with open('Data/Isotherms/413K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_413K = range(0,numpts)
			T0_413K = range(0,numpts)
			R0_413K = range(0,numpts)
			M0_413K = range(0,numpts)
			I0_413K = range(0,numpts)
		if index1 >= 6:
			P0_413K[index2] = float(row[0])
			T0_413K[index2] = float(row[1])
			R0_413K[index2] = float(row[2])
			M0_413K[index2] = float(row[3])
			I0_413K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_413K),axis=0)
T0 = npy.concatenate((T0,T0_413K),axis=0)
R0 = npy.concatenate((R0,R0_413K),axis=0)
M0 = npy.concatenate((M0,M0_413K),axis=0)
I0 = npy.concatenate((I0,I0_413K),axis=0)

with open('Data/Isotherms/393K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_393K = range(0,numpts)
			T0_393K = range(0,numpts)
			R0_393K = range(0,numpts)
			M0_393K = range(0,numpts)
			I0_393K = range(0,numpts)
		if index1 >= 6:
			P0_393K[index2] = float(row[0])
			T0_393K[index2] = float(row[1])
			R0_393K[index2] = float(row[2])
			M0_393K[index2] = float(row[3])
			I0_393K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_393K),axis=0)
T0 = npy.concatenate((T0,T0_393K),axis=0)
R0 = npy.concatenate((R0,R0_393K),axis=0)
M0 = npy.concatenate((M0,M0_393K),axis=0)
I0 = npy.concatenate((I0,I0_393K),axis=0)

with open('Data/Isotherms/373K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_373K = range(0,numpts)
			T0_373K = range(0,numpts)
			R0_373K = range(0,numpts)
			M0_373K = range(0,numpts)
			I0_373K = range(0,numpts)
		if index1 >= 6:
			P0_373K[index2] = float(row[0])
			T0_373K[index2] = float(row[1])
			R0_373K[index2] = float(row[2])
			M0_373K[index2] = float(row[3])
			I0_373K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_373K),axis=0)
T0 = npy.concatenate((T0,T0_373K),axis=0)
R0 = npy.concatenate((R0,R0_373K),axis=0)
M0 = npy.concatenate((M0,M0_373K),axis=0)
I0 = npy.concatenate((I0,I0_373K),axis=0)

with open('Data/Isotherms/353K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_353K = range(0,numpts)
			T0_353K = range(0,numpts)
			R0_353K = range(0,numpts)
			M0_353K = range(0,numpts)
			I0_353K = range(0,numpts)
		if index1 >= 6:
			P0_353K[index2] = float(row[0])
			T0_353K[index2] = float(row[1])
			R0_353K[index2] = float(row[2])
			M0_353K[index2] = float(row[3])
			I0_353K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_353K),axis=0)
T0 = npy.concatenate((T0,T0_353K),axis=0)
R0 = npy.concatenate((R0,R0_353K),axis=0)
M0 = npy.concatenate((M0,M0_353K),axis=0)
I0 = npy.concatenate((I0,I0_353K),axis=0)

with open('Data/Isotherms/333K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_333K = range(0,numpts)
			T0_333K = range(0,numpts)
			R0_333K = range(0,numpts)
			M0_333K = range(0,numpts)
			I0_333K = range(0,numpts)
		if index1 >= 6:
			P0_333K[index2] = float(row[0])
			T0_333K[index2] = float(row[1])
			R0_333K[index2] = float(row[2])
			M0_333K[index2] = float(row[3])
			I0_333K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_333K),axis=0)
T0 = npy.concatenate((T0,T0_333K),axis=0)
R0 = npy.concatenate((R0,R0_333K),axis=0)
M0 = npy.concatenate((M0,M0_333K),axis=0)
I0 = npy.concatenate((I0,I0_333K),axis=0)

with open('Data/Isotherms/313K_PLA_39E3_PVT.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(float(row[0]))
			P0_313K = range(0,numpts)
			T0_313K = range(0,numpts)
			R0_313K = range(0,numpts)
			M0_313K = range(0,numpts)
			I0_313K = range(0,numpts)
		if index1 >= 6:
			P0_313K[index2] = float(row[0])
			T0_313K[index2] = float(row[1])
			R0_313K[index2] = float(row[2])
			M0_313K[index2] = float(row[3])
			I0_313K[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1

P0 = npy.concatenate((P0,P0_313K),axis=0)
T0 = npy.concatenate((T0,T0_313K),axis=0)
R0 = npy.concatenate((R0,R0_313K),axis=0)
M0 = npy.concatenate((M0,M0_313K),axis=0)
I0 = npy.concatenate((I0,I0_313K),axis=0)
'''