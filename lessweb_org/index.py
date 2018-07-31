from lessweb import Application
from lessweb.plugin import database

from lessweb_org.config import get_config
from lessweb_org.controller.frame import view_processor

config = get_config()
database.init(dburi=config.db_uri, echo=config.db_echo)

app = Application()

app.add_get_interceptor('.*', view_processor)
app.add_get_mapping('/__design__/home', lambda:0, view="design.homePage")
