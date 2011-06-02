#!/usr/bin/python
from fabric.api import *

env.root = '.'

def serve():
    "Start the web2py development server."
    local('python src/web2py.py', capture=False)

def gae_serve():
    "Start the gae dev server. Assumes dev_appserver.py is in path"
    local('dev_appserver.py -d src', capture=False)

def deploy():
    "Deploy on GAE. Assumes appcfg.py is in path."
    local('appcfg.py update src', capture=False)
