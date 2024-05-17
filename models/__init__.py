#!/usr/bin/python3
"""initializes the package"""
from models.engine.file_storage import filestorage
storage = filestorage()
storage.reload()

