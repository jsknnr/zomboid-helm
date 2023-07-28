# zomboid-helm
Helm Chart for for deploying Project Zomboid server

## Usage
This chart utilizes container image built from https://github.com/jsknnr/zomboid-dedicated-server

Refer to the above repository for more information about how the container is built and the environment variables required.

Your cluster should be capable of either a LoadBalancer or NodePort service.

Your cluster should be capable of provisioning PVCs

For documentation on using Helm, refer to their documentation https://helm.sh/docs/intro/using_helm/

I built a quick little python script to help manage mod IDs and workshop IDs if you wish to run a modded server. Those values will need to be supplied to the `values.yaml` file in order for them to get installed. Refer to the `utility` directory for more information on using the script.
