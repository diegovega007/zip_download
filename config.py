class Config():
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    ALFRESCO_BASE_URL = "URL_DE_LA_API_ALFRESCO"

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:hola@localhost:5432/PostgresDMB"

config = {
    'development': DevelopmentConfig
}
