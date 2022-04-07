class Config(object):
    LOGGER = True

    API_KEY = ""
    OWNER_ID = ""
    OWNER_USERNAME = ""

    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  
    MESSAGE_DUMP = None  
    LOAD = []
    NO_LOAD = ['translation', 'rss', 'sed']
    WEBHOOK = False
    URL = None

    SUDO_USERS = [] 
    SUPPORT_USERS = [] 
    WHITELIST_USERS = [] 
    DONATION_LINK = None  
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  
    STRICT_GBAN = False
    WORKERS = 8  
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg' 
    ALLOW_EXCL = True 


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True