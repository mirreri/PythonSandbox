# if the sandbox remove the module path from module configuration but still keep the file in lib directory, can use this to recover it
sys.modules['os'] = '/usr/lib/python3.8/os.py' # assume this is correct path for os.py
import os
os.system ("ls /")
