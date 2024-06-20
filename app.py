from minio import Minio
from datetime import datetime
import io

client = Minio(
    "localhost:9000",
    access_key="sQTWYbkJoNcF9qH764Je",
    secret_key="IgJTU0NLuzm8xyTNsvrmyw3JFGzQNdpfaw5ORUyV",
    secure=False,
)

def minio_func(request):
    bucket_name = "testbucket"
    object_key = "log.txt"

    try:
        response = client.get_object(bucket_name, object_key)
        current_content = response.read().decode('utf-8')
        print('connection successful')

    finally:
        response.close()
        response.release_conn()

    timestamp = datetime.now().isoformat()
    new_log_entry = f"log-{timestamp}\n"
    updated_content = current_content + new_log_entry

    client.put_object(
        bucket_name,
        object_key,
        io.BytesIO(updated_content.encode('utf-8')),
        len(updated_content),
        content_type='text/plain'
    )
    
    data = client.get_object(bucket_name, object_key).read()
    print(data)
    return data

def hello_world(request):
    if request.is_json:
        print(request.json)
    else:
        print(request.data)
        print(request.form)
    
    minio_func(request)

    print("Hello world")
    return "hello world"