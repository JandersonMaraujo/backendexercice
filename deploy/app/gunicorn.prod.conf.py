import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/var/log/backendexercice/access.log"
errorlog = "/var/log/backendexercice/gunicorn.log"
reload = False
loglevel = 'info'
capture_output = True