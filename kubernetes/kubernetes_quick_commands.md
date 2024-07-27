# kubernetes quick commands



<br>
<br>
<br>
<br>

# Command related to kubernetes.


<br>
<br>
<br>
<br>

# Note

- Managing a kubernetes cluster is a complicated task in itself.
- For most , it makes sense to defer this management to the cloud, when this service is free in most cloud.
- `minikube` creates a single-node kubernetes cluster.

<br>

- Docker-in-Docker cluster.
- `kubeadm`


<br>
<br>
<br>
<br>

# Installing Kubernetes in GCP with Google Kubernetes Engine(GKE)

Make sure you have `gcloud tool` installed and configured.



```
gcloud config set compute/zone us-west1-a
gcloud container cluster create k8s-cluster1 --num-nodes=3
gcloud container cluster get-credentials k8s-cluster1
```


<br>
<br>
<br>
<br>

# Installing Kubernetes with Azure Kubernetes Service

```
- Azure cloud Shell
- This Shell has the `az tool` automatically installed and configured.
```


```
# Created a resource group
az group create --name=kuar --location-westus


```


