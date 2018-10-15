import os


class Config:
    """
    General configuration parent class
    """


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    pass


class DevConfig(Config):
    """
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    MONGO_URI = "mongodb://localhost:27017/myDatabase"
    DEBUG = True


class TestConfig(Config):
    """
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    MONGO_URI = "mongodb://localhost:27017/myTestDatabase"
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}