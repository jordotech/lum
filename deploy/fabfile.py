import os
import re
import sys

from functools import wraps
from getpass import getpass, getuser
from glob import glob
from contextlib import contextmanager

from fabric.api import env, cd, prefix, local, sudo as _sudo, run as _run, hide, task
from fabric.contrib.files import exists, upload_template
from fabric.colors import yellow, green, blue, red
from fabric.operations import _prefix_commands, _prefix_env_vars
conf = {}
if sys.argv[0].split(os.sep)[-1] == "fab":
    # Ensure we import settings from the current dir
    try:
        conf = __import__("settings", globals(), locals(), [], 0).FABRIC
        try:
            conf["HOSTS"][0]
        except (KeyError, ValueError):
            raise ImportError
    except (ImportError, AttributeError):
        print "Aborting, no hosts defined."
        exit()

env.db_name = 'bravo'
env.db_pass = conf.get("DB_PASS", None)
env.admin_pass = conf.get("ADMIN_PASS", None)
env.user = conf.get("SSH_USER", getuser())
env.password = conf.get("SSH_PASS", None)
env.key_filename = conf.get("SSH_KEY_PATH", None)
env.hosts = conf.get("HOSTS", [])


env.proj_name = conf.get("PROJECT_NAME", os.getcwd().split(os.sep)[-1])
env.venv_home = conf.get("VIRTUALENV_HOME", "/home/%s" % env.user)
env.venv_path = "%s/%s" % (env.venv_home, env.proj_name)
env.proj_dirname = "project"
env.proj_path = "%s/%s/%s" % (env.venv_path, env.proj_dirname, env.proj_name)
env.manage = "%s/bin/python /webapps/bravo/manage.py" % (env.venv_path)
env.live_host = conf.get("LIVE_HOSTNAME", env.hosts[0] if env.hosts else None)
env.ssl_cert_path = conf.get("SSL_CERT_PATH", None)
env.ssl_key_path = conf.get("SSL_KEY_PATH", None)
env.repo_url = conf.get("REPO_URL", "")
env.repo_branch = conf.get("REPO_BRANCH", "")
env.git = env.repo_url.startswith("git") or env.repo_url.endswith(".git")
env.reqs_path = conf.get("REQUIREMENTS_PATH", None)
env.gunicorn_port = conf.get("GUNICORN_PORT", 8000)
env.locale = conf.get("LOCALE", "en_US.UTF-8")
env.staging_home = conf.get("STAGING_HOME", "")
env.remote_db_backup_dir = conf.get("REMOTE_DB_BACKUP_DIR", "")

env.staging_code_dir = conf.get("STAGING_CODE_DIR", "")
env.local_code_dir = conf.get("LOCAL_CODE_DIR", "")
env.host_string = '%s:%s' % (env.hosts[0], '333')
env.staging_port = '333'
env.local_db = 'bravodev'
env.static_cache_path = '%ssherrihill/static/CACHE' % env.proj_path
###########################################
# Utils and wrappers for various commands #
###########################################

def _print(output):
    print
    print output
    print

def print_command(command):
    _print(blue("$ ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))
@task
def run(command, show=True):
    """
    Runs a shell comand on the remote server.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _run(command)
def postgres(command):
    """
    Runs the given command as the postgres user.
    """
    show = not command.startswith("psql")
    return run("sudo -u root sudo -u postgres %s" % command, show=show)

@task
def backup(filename):
    """
    Backs up the database.
    """
    return postgres("pg_dump -Fc %s > %s" % (env.db_name, filename))
@task
def scpDb(file):
    """
    Pull down latest db backup
    """
    command = 'scp deploy@%s:%s%s .' % (env.hosts[0], env.remote_db_backup_dir, file)
    local(command)
@task
def dl_staging_media():
    """
    Pull down /media/images folder
    """
    command = 'scp -r deploy@%s:%smedia %smedia/' % (env.hosts[0], env.staging_code_dir, env.local_code_dir)
    local(command)
@task
def dl_staging_slides():
    """
    Pull down latest db backup
    """
    command = 'scp -r deploy@%s:%smedia/slideshows %smedia/' % (env.hosts[0], env.staging_code_dir, env.local_code_dir)
    local(command)
@task
def importDb(file):
    """
    Pull down latest db backup
    """
    command = 'pg_restore -c -d %s < %s' % (env.local_db, file)
    local(command)
