class BaseConfig():
    HEADER = {
        'Content-type': 'application/json'
        }

class ProdConfig(BaseConfig):
    BASE_URL = 'https://api.spacetraders.io/v2'
    
class TestConfig(BaseConfig):
    BASE_URL = 'https://stoplight.io/mocks/spacetraders/spacetraders/96627693'