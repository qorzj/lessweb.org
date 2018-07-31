from lessweb_org.config import Config


config = Config(
    db_uri='mysql+mysqlconnector://user:passwd@host:3306/entity',
    db_echo = True,
    is_test = False,
)