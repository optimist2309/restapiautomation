import configparser


def get_nv_value():
    config_value = configparser.ConfigParser()
    config_value.read("C:\\Users\haris\\PycharmProjects\\restapiautomation\\utils\\properties.ini")
    return config_value
