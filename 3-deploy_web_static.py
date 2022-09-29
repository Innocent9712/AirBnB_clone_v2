#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.25.39.90', '44.200.178.6']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
=======
Fabric file to generate Project Deploy Static
"""
from fabric.api import env, sudo, run, local, put
from datetime import datetime

env.hosts = ['3.235.225.96', '34.236.187.99']


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


def do_deploy(archive_path):
    """
    Function to deploy the static website to all servers
    """
    file_name = archive_path.split('/')[-1][0:-4]
    if local("ls {}".format(archive_path)).failed:
        return False
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}'.format(file_name)).failed:
        return False
    if sudo('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file_name, file_name)).failed:
        return False
    if sudo('chown -R {}:{} /data/web_static/releases/{}'
            .format(env.user, env.user, file_name)).failed:
        return False
    if run('mv /data/web_static/releases/{}/web_static/* /data/web_static/rel'
            'eases/{}'.format(file_name, file_name)).failed:
        return False
    if run('rm /tmp/{}.tgz'.format(file_name)).failed:
        return False
    if run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(file_name)).failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """
    Function to run both do_pack and do_deploy
    """
    tar_path = do_pack()
    if tar_path is None:
        return False
    return do_deploy(tar_path)
>>>>>>> 3a8481dacf820165e6faab8d6a01b3ca689df150
