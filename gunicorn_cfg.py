# gunicorn_cfg.py
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = ":3005"
pidfile = 'gunicorn_pid'
timeout = 300

print("Server is running")