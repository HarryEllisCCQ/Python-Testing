
import clr
import sys

import time
start_time = time.time()
sys.path.append(r"C:\Program Files\dotnet\packs\Microsoft.NETCore.App.Ref\6.0.1\ref\net6.0")
#clr.AddReference("pythonTesting.dll")

#path = "C:\Users\44784\Documents\CCQ\pythonTesting\pythonTesting\bin\Debug\net6.0\pythonTesting.dll"

#clr.AddReference(r"C:\Users\44784\Documents\CCQ\pythonTesting\pythonTesting\bin\Debug\net6.0\pythonTesting")

#from pythonTesting import DataTransfer

sourcePath = "C:\ZDPtest1\Run_942-20210702@021959";
destinationPath = "C:\ZDPtest2";
#DataTransfer.transfer(sourcePath, destinationPath)

#print("--- %s seconds ---" % (time.time() - start_time))


from clr import System
from System import Reflection
full_filename = r'C:\Users\44784\Documents\CCQ\pythonTesting\pythonTesting\bin\Debug\net6.0\pythonTesting.dll'
dll_ref = Reflection.Assembly.LoadFile(full_filename)

#from pythonTesting import DataTransfer
some_class_type = dll_ref.GetType('pythonTesting.DataTransfer')
my_instance = System.Activator.CreateInstance(some_class_type)
#my_instance.a = 4 # setting attribute
my_instance.transfer(sourcePath, destinationPath) # calling methods

# C:\Program Files\dotnet\packs\Microsoft.NETCore.App.Ref\6.0.1\ref\net6.0