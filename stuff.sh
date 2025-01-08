docker build -t gke-starter-flask:latest .
docker tag gke-starter-flask:latest us-central1-docker.pkg.dev/starter-project-447001/starter-project/gke-starter-flask:latest
docker push us-central1-docker.pkg.dev/starter-project-447001/starter-project/gke-starter-flask:latest

kl delete -f k8s/deployment.yaml
kl apply -f k8s/deployment.yaml
