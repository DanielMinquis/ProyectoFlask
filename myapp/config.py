class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True #lo que estamos configurando es que nuestro servidor en modo debug o modo desarrollo
    
    #hay dos modos de activar el servidor, el otro se llama en modo produccionm, cuando ya se sube al servidor
    