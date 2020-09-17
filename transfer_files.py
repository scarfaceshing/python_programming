import glob, os
import shutil

baseDirectory = "C:/Users/scarfaceshing/Desktop/New folder/scrubbles"
baseDestination = "C:/Users/scarfaceshing/Desktop/New folder/destination"

videoExtensions = [
 # MP4
 "mp4", "m4a", "m4v", "f4v", "f4a", "m4b", "m4r", "f4b", "mov",
 # 3GP
 "3gp", "3gp2", "3g2", "3gpp", "3gpp2",
 # OGG
 "ogg", "oga", "ogv", "ogx",
 # WMV
 "wmv", "wma", "asf*",
 # WEBM
 "webm",
 # FLV
 "flv",
 # AVI
 "avi",
]

filteredItems = []

os.chdir(baseDirectory)
for extensions in videoExtensions:
 for file in glob.glob("*."+extensions):
   filteredItems.append(file)
    # print(file)


for item in filteredItems:
 shutil.move(baseDirectory+"/"+item, baseDestination+"/"+item)