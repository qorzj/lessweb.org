from lessweb import Application
from lessweb.plugin import database

from lessweb_org.config import get_config

config = get_config()
database.init(dburi=config.db_uri, echo=config.db_echo)

app = Application()

from lessweb_org.controller.frame import view_processor
app.add_get_interceptor('.*', view_processor)

from lessweb_org.controller.cookbook import home, article
app.add_get_mapping('/', home, view="cookbook.homePage")
app.add_get_mapping('/cookbook/(?P<name>.+)', article, view="cookbook.articlePage")

app.add_get_mapping('/__design__/home', lambda:0, view="design.homePage")
