import os
import shutil

# upload and scan mobsf
try:
    os.system("python mass_static_analysis.py -s 10.108.102.20:8000 -k 4ce655e2522ca0b659ebb91b33d4901c63c74f12815596e43b67dbbef6464794 -d /opt/massa/uploads")
except:
    print("Error uploading to MobSF")

# move files
try:
    fromDirectory = "/opt/massa/uploads"
    toDirectory = "/opt/massa/uploaded_mobsf"
    files = os.listdir(fromDirectory)

    for f in files:
        if files:
            mimetype = {'.apk': 'application/octet-stream',}
            shutil.move(os.path.join(fromDirectory, f), os.path.join(toDirectory,f))
        else:
            print("not support")

except:
    print("Error moving uploaded files")

'''
# copy files
fromDirectory = "opt/massa/uploads"
toDirectory = "/opt/massa/uploaded_mobsf"
copy_tree(fromDirectory, toDirectory)

# delete files
files = glob.glob('/opt/massa/uploads')
for f in files:
    os.remove(f)
'''