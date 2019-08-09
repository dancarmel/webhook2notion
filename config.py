

class Config(object):
    DEBUG = False
    TESTING = False
    TOKEN = 'c1e6f792c61011f397312209ac24ba1911a991965628757217c2921c1b72b2d725646c6e623bb92c3a332a39814d045bfde7db021d2d892f328fbdf8e939e915dd1379ffa60313990b5bf1d6a071'
    URL = "https://www.notion.so/dancarmel/030d26a82a19462296d9accf36584b4f?v=fa60f271887c4d819602dd4ad0bfd208"


class ProductionConfig(Config):

    pass


class DevelopmentConfig(Config):
    DEBUG = True

    TOKEN = 'c1e6f792c61011f397312209ac24ba1911a991965628757217c2921c1b72b2d725646c6e623bb92c3a332a39814d045bfde7db021d2d892f328fbdf8e939e915dd1379ffa60313990b5bf1d6a071'
    URL = "https://www.notion.so/dancarmel/030d26a82a19462296d9accf36584b4f?v=fa60f271887c4d819602dd4ad0bfd208"


class TestingConfig(Config):
    TESTING = True
