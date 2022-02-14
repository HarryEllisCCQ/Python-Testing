
import ctypes

sourcePath = "C:\ZDPtest1\Run_942-20210702@021959\Radar1";
destinationPath = "C:\ZDPtest2";

MyDllObject1 = ctypes.cdll.LoadLibrary("C:\\Users\\44784\\Documents\\CCQ\\pythonTesting\\pythonTesting\\bin\\Debug\\net6.0\\pythonTesting.dll")
#MyDllObject2 = ctypes.WinDLL("C:\\Users\\44784\\Documents\\CCQ\\pythonTesting\\pythonTesting\\bin\\Debug\\net6.0\\pythonTesting.dll")

MyDllObject1.transfer(sourcePath, destinationPath)
# MyDllObject2.transfer(sourcePath, destinationPath)
#MyFunctionObject = MyDllObject.transfer()

# MyFunctionObject.restype = ctypes.c_wchar_p
# MyFunctionObject.argtypes = ctypes.c_wchar_p


# DataTransfer = ctypes.windll("C:\\Users\\44784\\Documents\\CCQ\\pythonTesting\\pythonTesting\\bin\\Debug\\net6.0\\pythonTesting.dll")

