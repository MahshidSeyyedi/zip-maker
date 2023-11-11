import zipfile
import pathlib


# Creat function using this
def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir , "compressed.zip")
    with zipfile.ZipFile(dest_path , "w") as archive:
        #filepath = pathlib.Path(filepath)
        for filepaht in filepaths:
            filepath = pathlib.Path(filepaht)
            archive.write(filepath , arcname=filepaht)



# Test the function using this
if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py" , "bonus2.py"] , dest_dir="dest")
    