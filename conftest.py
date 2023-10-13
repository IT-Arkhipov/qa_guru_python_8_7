import zipfile

import pytest
import os
import shutil
from zipfile import ZipFile


@pytest.fixture(scope="function", autouse=True)
def tmp_folder():

    root_folder = os.getcwd()
    files_folder = os.path.join(root_folder, "resources")
    zip_folder = os.path.join(root_folder, "tmp")
    if not os.path.exists(zip_folder):
        os.mkdir(zip_folder)

    files = os.listdir(files_folder)
    zip_file = os.path.join(zip_folder, "files.zip")

    with ZipFile(zip_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            add_file = os.path.join(files_folder, file)
            zf.write(add_file, arcname=file)

    yield

    shutil.rmtree(zip_folder)



