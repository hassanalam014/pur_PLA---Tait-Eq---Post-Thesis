# Author: Kier von Konigslow
# Date: April 2017
#
# Description: The purpose of this file is to plot PMMA density information based on experiment and theory for comparison.
#

import os,sys,math,matplotlib.pyplot as plt,numpy as npy
from matplotlib.ticker import AutoMinorLocator
from all_p_params import *
from loadExperimentalData import *
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from loadPhysicalConstants import *
from findVectors import findVectors
from calculatePureVariables import calculateNewMolecularParameters,calculateCharacteristicParametersGamma
from wrapperFunctions import calculatePressure,calculateTemperature,calculateDensity


Pstar =  464.127112 #+/- 13.7891457 (2.97%) (init = 572.96)
Tstar =  566.767133 #+/- 2.72170304 (0.48%) (init = 591.56)
Rstar =  1.37495743 #+/- 0.00161557 (0.12%) (init = 1.364)

kwargs = {'Pstar':Pstar,'Tstar':Tstar,'Rstar':Rstar,'Pc0':Pc0,'Tc0':Tc0,'Rc0':Rc0}

isobars = ['22','40','60']

P_exp_min = min(P0)
P_exp_max = max(P0)
T_exp_min = min(T0)
T_exp_max = max(T0)
R_exp_min = min(R0)
R_exp_max = max(R0)

#Initializing the array of densities.
R0 = npy.linspace(0.01,0.99*Rstar,300)

gamma,vh,epsilon = calculateNewMolecularParameters(Pstar,Tstar,Rstar,M0[0])
vh = vh/NA
epsilon = epsilon/NA
print('The molecular parameters are: gamma = {}, vh = {}, and epsilon = {}.'.format(gamma,vh,epsilon))

Pmin = min(P0)
Pmax = max(P0)
Tmin = min(T0)
Tmax = max(T0)

print('The pressure range is {}-{}MPa and the temperature range is {}-{}K.'.format(Pmin,Pmax,Tmin,Tmax))

#==============================================================================================================
#Calculating Isotherms.
#==============================================================================================================

# for i in range(0,len(isobars)):
# 	exec "result = calculatePressure(T0_%sMPA,R0,M0_%sMPA,Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)" % (isobars[i],isobars[i])
# 	exec "T%sMPA_P = npy.array(result[1])" % (isobars[i])

# T493_P,R0 = calculatePressure(493.3,R0,M0[0],Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)

isotherms = False
isobars = True

P_exp_min = min(P0)
P_exp_max = max(P0)
T_exp_min = min(T0)
T_exp_max = max(T0)
R_exp_min = min(R0)
R_exp_max = max(R0)
V_exp_max = 1.0/R_exp_min
V_exp_min = 1.0/R_exp_max

Pmin = min(P0)
Pmax = max(P0)
Tmin = min(T0)
Tmax = max(T0)

print('The pressure range is {}-{}MPa and the temperature range is {}-{}K.'.format(Pmin,Pmax,Tmin,Tmax))

if isobars:
	V0_22MPA = 1/npy.array(R0_22MPA)
	V0_40MPA = 1/npy.array(R0_40MPA)
	V0_60MPA = 1/npy.array(R0_60MPA)

	T = npy.linspace(Tmin,Tmax,num=10)

	V_22MPA = npy.zeros(len(T))
	V_40MPA = npy.zeros(len(T))
	V_60MPA = npy.zeros(len(T))

	result = calculateDensity(P0_22MPA[0],T,M0[0],**kwargs)
	V_22MPA = 1/npy.array(result[1])
	result = calculateDensity(P0_40MPA[0],T,M0[0],**kwargs)
	V_40MPA = 1/npy.array(result[1])
	result = calculateDensity(P0_60MPA[0],T,M0[0],**kwargs)
	V_60MPA = 1/npy.array(result[1])

if isotherms:
	# V0_313K = 1/npy.array(R0_313K)
	# V0_333K = 1/npy.array(R0_333K)
	# V0_353K = 1/npy.array(R0_353K)
	# V0_373K = 1/npy.array(R0_373K)
	# V0_393K = 1/npy.array(R0_393K)
	# V0_413K = 1/npy.array(R0_413K)
	# V0_433K = 1/npy.array(R0_433K)
	V0_453K = 1/npy.array(R0_453K)
	V0_473K = 1/npy.array(R0_473K)
	V0_493K = 1/npy.array(R0_493K)

	P = npy.linspace(Pmin,Pmax,num=10)

	# V_313K = npy.zeros(len(P))
	# V_333K = npy.zeros(len(P))
	# V_353K = npy.zeros(len(P))
	# V_373K = npy.zeros(len(P))
	# V_393K = npy.zeros(len(P))
	# V_413K = npy.zeros(len(P))
	# V_433K = npy.zeros(len(P))
	V_453K = npy.zeros(len(P))
	V_473K = npy.zeros(len(P))
	V_493K = npy.zeros(len(P))

	# result = calculateDensity(P0,T0_313K[0],M0[0],**kwargs)
	# V_313K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_333K[0],M0[0],**kwargs)
	# V_333K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_353K[0],M0[0],**kwargs)
	# V_353K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_373K[0],M0[0],**kwargs)
	# V_373K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_393K[0],M0[0],**kwargs)
	# V_393K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_413K[0],M0[0],**kwargs)
	# V_413K = 1/npy.array(result[1])
	# result = calculateDensity(P0,T0_433K[0],M0[0],**kwargs)
	# V_433K = 1/npy.array(result[1])
	result = calculateDensity(P0,T0_453K[0],M0[0],**kwargs)
	V_453K = 1/npy.array(result[1])
	result = calculateDensity(P0,T0_473K[0],M0[0],**kwargs)
	V_473K = 1/npy.array(result[1])
	result = calculateDensity(P,T0_493K[0],M0[0],**kwargs)
	V_493K = 1/npy.array(result[1])

#Setting font size
axis_size = 20
title_size = 20
size = 14
label_size = 20
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

#Setting saved image properties
img_extension = '.png'
img_dpi = None
output_folder = 'plot_density'

#Checking for existence of output directory. If such a directory doesn't exist, one is created.
if not os.path.exists('./'+output_folder):
    os.makedirs('./'+output_folder)

#Defining linetype
line_style = ['-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':','-','--',':']
dot_style= ['ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk','ok','^k','sk']

#General line properties.
linewidth = 3
markersize = 8

arrow_ls = 'dashdot'
show_arrows = True

#==================================================================================
#P versus R plots.
figPUREPMMA=plt.figure(num=None, figsize=(12, 10), dpi=img_dpi, facecolor='w', edgecolor='k')
ax = plt.axes()

if isobars:
	plt.plot(T,V_22MPA,'r',lw=linewidth,ls='-',label='22MPA theory')
	plt.plot(T,V_40MPA,'b',lw=linewidth,ls='-',label='40MPA theory')
	plt.plot(T,V_60MPA,'g',lw=linewidth,ls='-',label='60MPA theory')

	plt.plot(T0_22MPA,V0_22MPA,'^k',ms=markersize,label='22MPA experiment')
	plt.plot(T0_40MPA,V0_40MPA,'sk',ms=markersize,label='40MPA experiment')
	plt.plot(T0_60MPA,V0_60MPA,'sk',ms=markersize,label='60MPA experiment')

	plt.xlabel('Temperature T (K)',fontsize=axis_size)
	plt.ylabel(r'Specific Volume $v$ ($cm^3/g$)',fontsize=axis_size)
	# plt.axis([0.90*T_exp_min,1.15*T_exp_max,0.98*V_exp_min,1.02*V_exp_max])
	plt.legend(loc=4,fontsize=size,numpoints=1)

if isotherms:
	# plt.plot(P,V_313K,'r',lw=linewidth,ls='-',label='313K theory')
	# plt.plot(P,V_333K,'b',lw=linewidth,ls='-',label='333K theory')
	# plt.plot(P,V_353K,'g',lw=linewidth,ls='-',label='353K theory')
	# plt.plot(P,V_373K,'y',lw=linewidth,ls='-',label='373K theory')
	# plt.plot(P,V_393K,'m',lw=linewidth,ls='-',label='393K theory')
	# plt.plot(P,V_413K,'g',lw=linewidth,ls='-',label='413K theory')
	# plt.plot(P,V_433K,'r',lw=linewidth,ls='-',label='433K theory')
	plt.plot(P,V_453K,'b',lw=linewidth,ls='-',label='453K theory')
	plt.plot(P,V_473K,'g',lw=linewidth,ls='-',label='473K theory')
	plt.plot(P,V_493K,'r',lw=linewidth,ls='-',label='493K theory')

	# plt.plot(P0_313K,V0_313K,'^k',ms=markersize,label='313K experiment')
	# plt.plot(P0_333K,V0_333K,'sk',ms=markersize,label='333K experiment')
	# plt.plot(P0_353K,V0_353K,'sk',ms=markersize,label='353K experiment')
	# plt.plot(P0_373K,V0_373K,'^k',ms=markersize,label='373K experiment')
	# plt.plot(P0_393K,V0_393K,'sk',ms=markersize,label='393K experiment')
	# plt.plot(P0_413K,V0_413K,'sk',ms=markersize,label='413K experiment')
	# plt.plot(P0_433K,V0_433K,'^k',ms=markersize,label='433K experiment')
	plt.plot(P0_453K,V0_453K,'sk',ms=markersize,label='453K experiment')
	plt.plot(P0_473K,V0_473K,'sk',ms=markersize,label='473K experiment')
	plt.plot(P0_493K,V0_493K,'^k',ms=markersize,label='493K experiment')

	plt.xlabel('Pressure P (MPA)',fontsize=axis_size)
	plt.ylabel(r'Specific Volume $v$ ($cm^3/g$)',fontsize=axis_size)
	# plt.axis([0.90*T_exp_min,1.15*T_exp_max,0.98*V_exp_min,1.02*V_exp_max])
	plt.legend(loc=4,fontsize=size,numpoints=1)

# figPUREPLA.savefig('./'+output_folder+r'\pure_PLA_density'+img_extension,dpi=img_dpi)

plt.show()
