# file : ds29_osFileList.py
# desc : 윈도우 파일 리스트

import os

fnameAry = []
folderName = 'c:/Sources/ds-and-algorithm'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)


print(fnameAry)
print(len(fnameAry))

fnameAry.sort(reverse=True)
print(fnameAry)
