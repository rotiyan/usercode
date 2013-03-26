#!/bin/env python

import os

inputTrees = ['/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012A/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012ARecover/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012B/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012C1/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012CEcalRecover/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012C2/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/Run2012D/selection_test.root',
              '/Users/demattia/TMVA-v4.1.2/test/NewTrees/Trees/BsMC/selection_test.root',
              ]
region = ["barrel", "endcaps"]

# This is the value of the rest of event number % 3
splitting = -1

splitString =""
if splitting != -1:
    splitString = "_"+str(splitting)

appendName = "_preselection"+splitString+".root"
appendNameMC = "_preselection.root"


for tree in inputTrees:
    data = "1"
    cut_based = "0"
    if tree.find("MC") != -1: data = "0"
    append = appendName
    if data == "0": append = appendNameMC
    # NO SPACES IN THE ROOT COMMAND
    for regionIndex in [0,1]:
        if cut_based == "0":
            print "Applying preselection cuts"
            outputTree = tree.split("/")[-2]+'_'+region[regionIndex]+append
        else:
            print "Applying analysis cuts"
            outputTree = tree.split("/")[-2]+'_'+region[regionIndex]+'.root'
        blinding = "0"
        if data == "1": blinding = "1"
        os.system('root -l -b -q cutTree_BsMuMu.C\(\\"'+tree+'\\",\\"'+outputTree+'\\",'+str(regionIndex)+','+data+','+cut_based+','+blinding+','+str(splitting)+'\)')


os.system("rm -f Barrel"+appendName)
os.system("hadd Barrel"+appendName+" Run2012A_barrel"+appendName+" Run2012ARecover_barrel"+appendName+" Run2012B_barrel"+appendName+" Run2012C1_barrel"+appendName+" Run2012CEcalRecover_barrel"+appendName+" Run2012C2_barrel"+appendName+" Run2012D_barrel"+appendName)

os.system("rm -f Endcaps"+appendName)
os.system("hadd Endcaps"+appendName+" Run2012A_endcaps"+appendName+" Run2012ARecover_endcaps"+appendName+" Run2012B_endcaps"+appendName+" Run2012C1_endcaps"+appendName+" Run2012CEcalRecover_endcaps"+appendName+" Run2012C2_endcaps"+appendName+" Run2012D_endcaps"+appendName)
os.system("rm -f Run*")

os.system("mv BsMC_barrel"+appendNameMC+" BsMC12_barrel"+appendNameMC)
os.system("mv BsMC_endcaps"+appendNameMC+" BsMC12_endcaps"+appendNameMC)

os.system("root -l -b -q AddMuonID.C+\(\\\"Barrel"+appendName+"\\\"\)")
os.system("root -l -b -q AddMuonID.C+\(\\\"Endcaps"+appendName+"\\\"\)")

print "mv Barrel"+appendName+"_muonID.root Barrel"+appendName
os.system("mv Barrel"+appendName+"_muonID.root Barrel"+appendName)
print "mv Endcaps"+appendName+"_muonID.root Endcaps"+appendName
os.system("mv Endcaps"+appendName+"_muonID.root Endcaps"+appendName)

os.system("root -l -b -q AddMuonID.C+\(\\\"BsMC12_barrel"+appendNameMC+"\\\"\)")
os.system("root -l -b -q AddMuonID.C+\(\\\"BsMC12_endcaps"+appendNameMC+"\\\"\)")

os.system("mv BsMC12_barrel"+appendNameMC+"_muonID.root BsMC12_barrel"+appendNameMC)
os.system("mv BsMC12_endcaps"+appendNameMC+"_muonID.root BsMC12_endcaps"+appendNameMC)