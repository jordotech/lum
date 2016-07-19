from unipath import Path
import logging
PROJECT_DIR = Path(__file__).ancestor(2)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(name)s:%(module)s line %(lineno)s %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': PROJECT_DIR.child('logs').child('lum.log'),
        },
        'lum_log': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR.child('logs').child('lum.log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'lum': {
            'handlers': ['lum_log'],
            'level': 'DEBUG',
        },
    },
}
LOGFILE = "default.log"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=PROJECT_DIR.child(LOGFILE),
                    filemode='w')
