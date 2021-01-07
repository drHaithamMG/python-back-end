import os
from pathlib import Path
# import packages.packageA.fileA
# from ..packageB.fileB import g
path = os.getcwd()
os.chdir(path+'/packages/packageA')
print(os.getcwd())
# from ..packageB import g
# path = path.split('/')
# path_len = len(path)
# print(path_len)
# path = '/'.join(path[:5])
# print(path)
