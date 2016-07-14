# PRODUCTION

FABRIC = {
    "SSH_USER": "deploy", # SSH username
    "SSH_PASS":  "happy", # SSH password (consider key-based authentication)
    "SSH_KEY_PATH":  "", # Local path to SSH key file, for key-based auth
    "HOSTS":['159.203.88.155',],
    "VIRTUALENV_HOME":  "/home/.virtualenvs", # Absolute remote path for virtualenvs
    "PROJECT_NAME": "bravo", # Unique identifier for project
    "REQUIREMENTS_PATH": "/webapps/bravo/requirements.txt", # Path to pip requirements, relative to project
    "GUNICORN_PORT": 8000, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "LIVE_HOSTNAME": "bravoconcealment.com", # Host for public site.
    "REPO_URL": "git@github.com:jordotech/bravo.git", # Git or Mercurial remote repo URL for the project
    "REPO_BRANCH": 'master',
    "STAGING_HOME":'/home/deploy/',
    "LOCAL_CODE_DIR":'/Applications/MAMP/htdocs/sh2/data/bravo/',
    #'/Applications/MAMP/htdocs/sh/data/bravo/',
    "STAGING_CODE_DIR":'/webapps/bravo/',
    "REMOTE_DB_BACKUP_DIR":'/home/deploy/db_backups/',
    "DB_PASS": "happy", # Live database password
    #"SSL_CERT_PATH": "/home/deploy/self-ssl.crt",
    #"SSL_KEY_PATH": "/home/deploy/self-ssl.key",
    #"SSL_CERT_PATH": "/home/deploy/sherrihill.chained.crt",
    #"SSL_KEY_PATH": "/home/deploy/sherrihill.com.key",
}
