import os
import shutil

!omz_downloader --print_all
model = input()
!omz_downloader --name {model} --precision FP16    
try:
    os.mkdir('model')
except Exception:
    pass
default_directory = os.getcwd()
os.chdir("model")
model_directory = os.getcwd() 
os.chdir(default_directory)
list_int = os.listdir(path=".")
text_length_int = len(os.listdir(path="."))
os.chdir(default_directory)

try:
    for i in range (text_length_int):
        if (list_int[i] == "intel"):
            os.chdir("intel")
            path_int = os.getcwd()
    list_int_1 = os.listdir(path=".")
    text_length_int_1 = len(os.listdir(path="."))

    for i in range (text_length_int_1):
        if (list_int_1[i] == model):
            os.chdir(model)
            path_fac = os.getcwd()
    list_fac = os.listdir(path=".")
    text_length_fac = len(os.listdir(path="."))
    for i in range (text_length_fac):
        if (list_fac[i] == "FP16"):
            os.chdir("FP16")
            path_fac_FP = os.getcwd()
    list_fac_mod = os.listdir(path=".")
    text_length_fac_mod = len(os.listdir(path="."))
    shutil.move(model+'.bin',model_directory)
    shutil.move(model+'.xml',model_directory)
    os.chdir(default_directory)
    shutil.rmtree('intel')
except Exception:
    pass

try:
    
except Exception:
    pass
