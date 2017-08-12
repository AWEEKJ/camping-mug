class Config(object):
    DEBUG = False
    TESTING = False


class RealConfig(Config):
    pass


class StageConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True
    TESTING = True
