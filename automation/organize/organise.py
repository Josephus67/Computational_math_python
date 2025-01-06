
import os
from pathlib import Path

SUBDIRECTORIES = {
    'DOCUMENT':['.pdf','.rtf','.txt'],
    'AUDIO':['.m4a','.m4b','.mp3'],
    'VIDEOS':['.mov','.avi','.mp4'],
    'IMAGES':['.jpg','.jpeg','.png']
}

def pickdir(value):
    for category,suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    else: return "MISCELENIOUS"

print(pickdir('.jpg'))
print(pickdir('.mp4'))


def orgdir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickdir(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

print(orgdir())