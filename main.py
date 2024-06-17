def hello_world(request):
    if request.is_json:
        print(request.json)
    else:
        print(request.data)
        print(request.form)
        
    # write to log
    with open("/tmp/log.txt", "a") as f:
        f.write("Hello world\n")
    

    print("Hello world")
    return "hello world"
