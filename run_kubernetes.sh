
#!/usr/bin/env bash

dockerpath="akshaypunwatkar/logoclassifier"

# Run in Docker Hub container with kubernetes
kubectl run logoclassifierdemo\
    --generator=run-pod/v1\
    --image=$dockerpath\
    --port=8088 --labels app=logoclassifierdemo

# List kubernetes pods
kubectl get pods

# Forward the container port to host
kubectl port-forward logoclassifierdemo 8088:8088
