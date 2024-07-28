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

More details:
- https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster


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
az group create --name=k8s --location-westus


# creating kubernetes cluster
az aks create --resource-group=k8s --name=k8s-cluster

# getting credentials
az aks get-credentials --resource-group=k8s --name=k8s-cluster

# installing k8s toolkit
az aks install-cli
```

More details:
- https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli



<br>
<br>
<br>
<br>

# Installing kubernetes on Amazon Web Services

```
EKS - Elastic Kubernetes Service (https://eksctl.io/)

- Install the eksctl command-line tool

eksctl create cluster

eksctl create cluster --help



```


<br>
<br>

kubernetes install tools:
- https://kubernetes.io/docs/tasks/tools/





<br>
<br>
<br>
<br>


### Learning kubernetes from its home link
https://kubernetes.io/docs/tasks/tools/



<br>
<br>
<br>
<br>


## commands

```
# To display pods for a given namespace.
kubectl get pod --namespace kube-system


```