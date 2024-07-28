### kubernetes quick commands
- In this file, we will have notes related to the `kubernetes` commands.
- Commands related to `kubectl` and `kubeadm`.
- `kubectl`: This is the official kubernetes client.
- `kubectl` a command-line tool for interacting with the `kubernetes API`.
- `kubectl` can be used to `manage` most `kubernetes` `objects`, such as `Pods`, `ReplicaSes` and `Services`.
- `kubectl` can also be used to `explore` and `verify` the overall health of the cluster.



<br>
<br>
<br>
<br>

---

### Command related to kubernetes.


<br>
<br>
<br>
<br>

---

### Note

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

---


### Installing Kubernetes in GCP with Google Kubernetes Engine(GKE)

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

---

### Installing Kubernetes with Azure Kubernetes Service

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

---

### Installing kubernetes on Amazon Web Services

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

---


### commands

```
# To display pods for a given namespace.
kubectl get pod --namespace kube-system


```


<br>
<br>
<br>
<br>

---
---


### kubectl

```
kubectl version
```

output:
```
Client Version: v1.28.3
Server Version: v1.27.4
```
<br>

Will display the version of 
- the local `kubectl` and 
- version of `kubernetes API` server.
- Although these are `backward` and `forward` compatible try to keep sync within two minor version.
- Don't try to use newer features on an older cluster.




<br>
<br>

Get a simple diagnostic for the cluster:
```
kubectl get componentstatuses
```

output:
```
NAME                 STATUS    MESSAGE   ERROR
controller-manager   Healthy   ok        
etcd-0               Healthy             
scheduler            Healthy   ok      
```

<br>

<u>Note:</u>

The `controller-manager` is responsible for running various `controllers` that `regulate behavior` in the cluster:

-  Example: Ensuring that all of the replicas of a service are availale and healthy.

The `scheduler` is responsible for placing different `Pods` onto different nodes in the cluster.

The `etcd` server is the storage for teh cluster where all of the API object are stored.

<br>
<br>

