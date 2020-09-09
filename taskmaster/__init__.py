from flask import Flask

from taskmaster.config import Config
from taskmaster.urls import URL_RULES

app = Flask(__name__)
app.config.from_object(Config)

for url_rule in URL_RULES:
    app.add_url_rule(**url_rule)
