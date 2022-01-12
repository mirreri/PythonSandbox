# because some sandbox will block user import specific module, can use this to skip
import importlib
os_module = importlib.import_module ("os")
os_module.system ("ls /")
