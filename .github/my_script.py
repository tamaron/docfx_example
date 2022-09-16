import os
import glob
from xml.etree.ElementInclude import include

# def find_all_files(directory):
#     for root, dirs, files in os.walk(directory):
#         yield root
#         for file in files:
#             yield os.path.join(root, file)

# for file in find_all_files(os.getcwd()):
#     print(file)

print(os.getcwd())
os.chdir('_site/api')
os.getcwd()

files = glob.glob("./*")
for fileName in files:
    with open(fileName ,"r",encoding="utf_8_sig") as file:
        lines=file.read()

    if 'SampleNamespace.TypeA' in lines:
        print(fileName)
        lines = lines.replace('cs.temp.dll.dll', 'SampleNamespace.TypeA.dll')
    elif 'SampleNamespace.TypeB' in lines:
        lines = lines.replace('cs.temp.dll.dll', 'SampleNamespace.TypeB.dll')
    

    print(lines)
    with open(fileName ,"w",encoding="utf_8_sig") as file:
        file.write(lines)
    
