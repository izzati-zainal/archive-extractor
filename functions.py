import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(r"D:\ThinkerCube\2022 Project - Python\Python By Ardit\App-ArchiveExtractor\dest\compressed.zip", r"D:\ThinkerCube\2022 Project - Python\Python By Ardit\App-ArchiveExtractor\dest")