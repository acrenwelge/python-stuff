import tarfile
import glob

def create_tarfile():
    tfile = tarfile.open("mytarfile.tar", "w")
    for file in glob.glob(pathname="./test/*.txt"):
        tfile.add(file)
    tfile.close()

create_tarfile()
