import os

workers = 2
threads = 4
timeout = 120
bind = "0.0.0.0:" + os.environ.get("PORT", "8000")
