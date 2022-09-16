import os
import glob
from xml.etree.ElementInclude import include

os.chdir('../')
os.chdir('_site/api')
path = os.getcwd()

files = glob.glob("./*")
for fileName in files:
    with open(fileName ,"r",encoding="utf-8") as file:
        lines=file.read()

    if 'SampleNamespace.TypeA' in lines:
        print(fileName)
        lines = lines.replace('cs.temp.dll.dll', 'SampleNamespace.TypeA.dll')
    elif 'SampleNamespace.TypeB' in lines:
        lines = lines.replace('cs.temp.dll.dll', 'SampleNamespace.TypeB.dll')
    

    print(lines)
    with open(fileName ,"w",encoding="utf-8") as file:
        file.write(lines)
    
