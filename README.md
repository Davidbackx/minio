### Onpremise exploration

# function deployment

`minio-dev.yaml` is used to run a local version of minio on k8s.

`function.yaml` contains the deployment config for a basic hello world function

`function_latest.yaml` is 
``

### local setup

`kubectl apply -f minio-dev.yaml` applies and deploys the configuration for minio on kubernetes

Run `kubectl get pods -n minio-dev` to check if your pod is started

`kubectl port-forward pod/minio 9000 9090` Minio should be running at
http://localhost:9090

Login credentials should be:
`minioadmin | minioadmin`

If at any place in these steps something goes wrong check out the official docs: [minio docs](https://min.io/docs/minio/kubernetes/upstream/index.html)

### function setup

`pack build python-sample --builder openfunction/gcp-builder:v1 --env GOOGLE_FUNCTION_TARGET=hello_world
`

`docker run --rm --env="FUNC_CONTEXT={\"name\":\"python-sample\",\"version\":\"v1.0.0\",\"port\":\"8080\",\"runtime\":\"Knative\"}" --env="CONTEXT_MODE=self-host" --name python-sample -p 8080:8080 python-sample
`

`curl http://localhost:8080` should return hello, world 2

### Some next steps I was thinking about

Either webhook on minio or Minio python sdk to execute a function on some event.