from system_classDec import SystemClass
import os, sys, subprocess

path = os.getcwd()

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", path + "\\requirements.txt"])
print("")
print("All requirements installed.")
print("")

fyldeAeroInvSystem = SystemClass()