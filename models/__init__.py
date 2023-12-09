#!/usr/bin/python3

"""the init package file"""


# import the FileStorage class from the file_storage module
from models.engine.file_storage import FileStorage


# create dummy attributes as arguments for filestorage
storage = FileStorage()
storage.reload()
