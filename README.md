# DEPRECATED AND ARCHIVED
I am no longer supporting this repo and image. I have a new repo, image, and helm chart available here https://github.com/jsknnr/project-zomboid-server that is not based on a fork. The new repo is similar to my other work and I like consistency.

Helm Chart for for deploying Project Zomboid server

## Usage
This chart utilizes container image built from https://github.com/jsknnr/zomboid-dedicated-server

Refer to the above repository for more information about how the container is built and the environment variables required.

Your cluster should be capable of either a LoadBalancer or NodePort service.

Your cluster should be capable of provisioning PVCs

For documentation on using Helm, refer to their documentation https://helm.sh/docs/intro/using_helm/
