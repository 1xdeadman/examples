# https://docs.python.org/3/library/sys.html
import sys

print("argv:", sys.argv)

print("platform:", sys.platform)
"""
AIX 'aix'
Linux 'linux'
Windows 'win32'
macOS 'darwin'
"""


print("prefix:", sys.prefix)
print("executable:", sys.executable)
print("path:", sys.path)

ff = []
fff = ff

print("getrefcount:", sys.getrefcount(ff))
print("getsizeof:", sys.getsizeof(ff))
ff.append(1)
print("getsizeof:", sys.getsizeof(ff))

print("getdefaultencoding:", sys.getdefaultencoding())
print("getfilesystemencoding:", sys.getfilesystemencoding())


sys.exit()
