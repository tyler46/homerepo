from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import exists


env.hosts = ["spyros@192.168.1.10"]
env.deploy_user = 'deploy'
env.project_dir = '/opt/sites/homerepo/'


def update_server():
    with settings(user=env.deploy_user):
        with cd(env.project_dir):
            # pull latest changes from git
            run("git pull origin master")

            # restart app
            sudo("supervisorctl restart homerepo")

            # print status to make sure if restarted correctly
            sudo("supervisorctl status")

            # restart the web server
            sudo('/etc/init.d/nginx restart')

