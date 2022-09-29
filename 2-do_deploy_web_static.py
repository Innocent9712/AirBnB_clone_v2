#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.25.39.90', '44.200.178.6']


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
=======
Fabric file to generate Project Deploy Static
"""
from fabric.api import env, sudo, run, local, put

env.hosts = ['3.235.225.96', '34.236.187.99']


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
>>>>>>> 3a8481dacf820165e6faab8d6a01b3ca689df150
