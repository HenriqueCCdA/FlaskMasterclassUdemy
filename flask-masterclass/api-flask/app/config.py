class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5434/flask_contacts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    Debug = True


class Testing(Config):
    pass


config = {
    'development': Development,
    'testing': Testing
}