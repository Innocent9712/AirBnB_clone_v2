#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
=======
Fabric file to generate a .tgz compressed file for
the web_static directory
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to create the compressed file
    """
    curr_datetime = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = "./versions/web_static_" + curr_datetime + ".tgz"
    local("mkdir -p ./versions")
    if local("tar -cvzf " + path + " ./web_static").succeeded:
        return path
    return None
>>>>>>> 3a8481dacf820165e6faab8d6a01b3ca689df150
