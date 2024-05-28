from datetime import datetime

def hello_world(request):
    with open('logs.txt', 'rw') as f:
        log = f"Hello World was invoked at {datetime.now()}\n"
        f.write(log)
    
    return "hello, world"