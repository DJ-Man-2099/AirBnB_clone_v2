#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo,
using the function do_pack
"""

from datetime import datetime
from fabric.api import local, put, run, env

env.hosts = ['100.25.146.3', '34.207.120.217']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    name = f"web_static_{date}.tgz"
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(name))
    if result.failed:
        return None
    return local(f'versions/{name}')


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if not archive_path:
        return False
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    name = archive_path.split("/")[-1].split(".")[0]
    result = run(
        f"tar -xvf {archive_path} -C /data/web_static/releases/{name}")
    if result.failed:
        return False
    result = run(f"rm {archive_path}")
    if result.failed:
        return False
    result = run(
        f"ln -s /data/web_static/releases/{name} /data/web_static/current")
    if result.failed:
        return False
    return True
