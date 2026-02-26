import configparser

config=configparser.RawConfigParser() #Creation object for config parser
config.read(".\\Configuration\\config.ini.py")  #provide path of config file

class ReadConfig:
    @staticmethod
    def appCreds(group,key):
        data=config.get(group,key)
        return data