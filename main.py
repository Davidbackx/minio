def hello_world(request):
    if request.is_json:
        print(request.json)
    else:
        print(request.data)
        print(request.form)

    print("Hello world")
    return "hello world"