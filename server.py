# -*- coding: utf-8 -*-
# Filename: server.py
from appliction import Application
from waitress import serve  # pip install waitress

app = Application()

if __name__ == '__main__':
    serve(app.api, host='0.0.0.0', port=3005)

# gunicorn -c gunicorn_cfg.py application:app.api --reload