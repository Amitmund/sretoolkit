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

- cheat-sheet: https://kubernetes.io/docs/reference/kubectl/quick-reference/


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



### knowing kubectl client and kubernetes API version:

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
<br>
<br>

---


#### Get a simple diagnostic for the cluster:
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

Note:

The `controller-manager` is responsible for running various `controllers` that `regulate behavior` in the cluster:

-  Example: Ensuring that all of the replicas of a service are availale and healthy.

The `scheduler` is responsible for placing different `Pods` onto different nodes in the cluster.

The `etcd` server is the storage for teh cluster where all of the API object are stored.

<br>
<br>
<br>
<br>

---

### Listing kubernetes Nodes

```
kubectl get nodes
```


output:

```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   8h    v1.27.4
```

<br>

Note:

In kubernetes, nodes are separated into:

- control-plane 

    - Which contain containers like:
    - API Server
    - Scheduler

- worker nodes

k8s won't generally schedule work onto control-plane node, ensuring that user workloads don't harm the overall of the cluster.

<br>
<br>
<br>
<br>

---


### Getting details about nodes

```
kubectl describe nodes {node_name}


# Example:

kubectl describe nodes minikube
```
<br>
<br>


> First you will see basic information about node.


Output:
<br>
Cleaned up few line for quick understanding.

```
Name:               minikube
Roles:              control-plane
Labels:             beta.kubernetes.io/arch=arm64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=arm64
...
...
                    minikube.k8s.io/version=v1.31.2
...
...
Annotations:        kubeadm.alpha.kubernetes.io/cri-socket: unix:///var/run/cri-dockerd.sock
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
...
...
Lease:
  HolderIdentity:  minikube
  AcquireTime:     <unset>
  RenewTime:       Sun, 28 Jul 2024 16:35:35 +0530
                    
```
<br>
<br>

Next it will let you know the conditions about the node with respect to kubelet point of view.

(Date fields have been removed for a cleanr view.)



```
Conditions:
  Type             Status                  Reason                       Message
  ----             ------                  ------                       -------
  MemoryPressure   False    KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure     False    KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure      False    KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready            True     KubeletReady                 kubelet is posting ready status

```
<br>
<br>

Next it will display the `capacity` and `allocatable` of the node

```
Capacity:
  cpu:                2
  ephemeral-storage:  17784760Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  hugepages-32Mi:     0
  hugepages-64Ki:     0
  memory:             2147728Ki
  pods:               110

```

<br>
<br>

Then, it will let you know about the `software` of the node.

```
System Info:
  Machine ID:                 0528261e35bc492aa593f1f9cac58016
  System UUID:                0528261e35bc492aa593f1f9cac58016
  Boot ID:                    a97be68f-b4ff-4412-991c-310e44cbcf94
  Kernel Version:             5.10.57
  OS Image:                   Buildroot 2021.02.12
  Operating System:           linux
  Architecture:               arm64
  Container Runtime Version:  docker://24.0.4
  Kubelet Version:            v1.27.4
  Kube-Proxy Version:         v1.27.4
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
```


<br>
<br>
Information about the `Pods, `allocated resources` and `Events` that are currently running on this node.

```
Non-terminated Pods:          (7 in total)  <---------


Namespace                   Name                                CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                ------------  ----------  ---------------  -------------  ---
  kube-system                 coredns-5d78c9869d-hwzck            100m (5%)     0 (0%)      70Mi (3%)        170Mi (8%)     9h
  kube-system                 etcd-minikube                       100m (5%)     0 (0%)      100Mi (4%)       0 (0%)         9h
  kube-system                 kube-apiserver-minikube             250m (12%)    0 (0%)      0 (0%)           0 (0%)         9h
  kube-system                 kube-controller-manager-minikube    200m (10%)    0 (0%)      0 (0%)           0 (0%)         9h
  kube-system                 kube-proxy-vpq8f                    0 (0%)        0 (0%)      0 (0%)           0 (0%)         9h
  kube-system                 kube-scheduler-minikube             100m (5%)     0 (0%)      0 (0%)           0 (0%)         9h
  kube-system                 storage-provisioner                 0 (0%)        0 (0%)      0 (0%)           0 (0%)         9h



Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                750m (37%)  0 (0%)
  memory             170Mi (8%)  170Mi (8%)
  ephemeral-storage  0 (0%)      0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
  hugepages-32Mi     0 (0%)      0 (0%)
  hugepages-64Ki     0 (0%)      0 (0%)



Events:
  Type    Reason                   Age                From             Message
  ----    ------                   ----               ----             -------
  Normal  Starting                 7h52m              kube-proxy       
  Normal  Starting                 74m                kube-proxy       
  Normal  NodeNotReady             7h53m              kubelet          Node minikube status is now: NodeNotReady
  Normal  RegisteredNode           7h52m              node-controller  Node minikube event: Registered Node minikube in Controller
  Normal  Starting                 74m                kubelet          Starting kubelet.
  Normal  NodeHasSufficientMemory  74m (x8 over 74m)  kubelet          Node minikube status is now: NodeHasSufficientMemory
  Normal  NodeHasNoDiskPressure    74m (x8 over 74m)  kubelet          Node minikube status is now: NodeHasNoDiskPressure
  Normal  NodeHasSufficientPID     74m (x7 over 74m)  kubelet          Node minikube status is now: NodeHasSufficientPID
  Normal  NodeAllocatableEnforced  74m                kubelet          Updated Node Allocatable limit across pods
  Normal  RegisteredNode           73m                node-controller  Node minikube event: Registered Node minikube in Controller

```

You can also see information related to :
- Requests of resources and
- Upper limit of the resources.

For `each pod`.

<br>
<br>
<br>
<br>

---

### Few key pod I can see running in this minikube are:

- codedns
- etcd
- kube-apiserver
- kube-controller-manager
- kube-proxy
- kube-scheduler
- storage-provisioner


### NOTE:

```
Resources requested by a Pod are guaranteed to be present on the node, while a Pod's limit is the maximum amount of a given resource that a Pod can consume.

A Pod's limit can be higher than its request. In which case the extra resources are supplied on a best-effort basis. However they are not guaranteed to be present on the node.
```


<br>
<br>
<br>
<br>

---

### Cluster components

One of the interesting aspects of kubernetes is that many of the componentes that make up the kubernetes cluster are actually deployed using kubernetes itself. Also note that, these components run in the `kube-system` namespace.





<br>
<br>
<br>
<br>

---

### Different kubernetes `kind` :



```

[root@hsk-controller ~]# kubectl api-resources
NAME                              SHORTNAMES       KIND
bindings                                           Binding
componentstatuses                 cs               ComponentStatus
configmaps                        cm               ConfigMap
endpoints                         ep               Endpoints
events                            ev               Event
limitranges                       limits           LimitRange
namespaces                        ns               Namespace
nodes                             no               Node
persistentvolumeclaims            pvc              PersistentVolumeClaim
persistentvolumes                 pv               PersistentVolume
pods                              po               Pod
podtemplates                                       PodTemplate
replicationcontrollers            rc               ReplicationController
resourcequotas                    quota            ResourceQuota
secrets                                            Secret
serviceaccounts                   sa               ServiceAccount
services                          svc              Service
initializerconfigurations                          InitializerConfiguration
mutatingwebhookconfigurations                      MutatingWebhookConfiguration
validatingwebhookconfigurations                    ValidatingWebhookConfiguration
customresourcedefinitions         crd,crds         CustomResourceDefinition
apiservices                                        APIService
controllerrevisions                                ControllerRevision
daemonsets                        ds               DaemonSet
deployments                       deploy           Deployment
replicasets                       rs               ReplicaSet
statefulsets                      sts              StatefulSet
tokenreviews                                       TokenReview
localsubjectaccessreviews                          LocalSubjectAccessReview
selfsubjectaccessreviews                           SelfSubjectAccessReview
selfsubjectrulesreviews                            SelfSubjectRulesReview
subjectaccessreviews                               SubjectAccessReview
horizontalpodautoscalers          hpa              HorizontalPodAutoscaler
cronjobs                          cj               CronJob
jobs                                               Job
brpolices                         br,bp            BrPolicy
clusters                          rcc              Cluster
filesystems                       rcfs             Filesystem
objectstores                      rco              ObjectStore
pools                             rcp              Pool
certificatesigningrequests        csr              CertificateSigningRequest
leases                                             Lease
events                            ev               Event
daemonsets                        ds               DaemonSet
deployments                       deploy           Deployment
ingresses                         ing              Ingress
networkpolicies                   netpol           NetworkPolicy
podsecuritypolicies               psp              PodSecurityPolicy
replicasets                       rs               ReplicaSet
nodes                                              NodeMetrics
pods                                               PodMetrics
networkpolicies                   netpol           NetworkPolicy
poddisruptionbudgets              pdb              PodDisruptionBudget
podsecuritypolicies               psp              PodSecurityPolicy
clusterrolebindings                                ClusterRoleBinding
clusterroles                                       ClusterRole
rolebindings                                       RoleBinding
roles                                              Role
volumes                           rv               Volume
priorityclasses                   pc               PriorityClass
storageclasses                    sc               StorageClass
volumeattachments                                  VolumeAttachment

```

A few key one:

```
pods
Namespaces
ReplicationController (Manages Pods)
DeploymentController (Manages Pods)
StatefulSets
DaemonSets
Services
ConfigMaps
Volumes

```

kind: Represent the type of kubernetes object created.



<br>
<br>
<br>
<br>

---

### creating different namespace

```

vi my-namespace.yaml

apiVersion: v1
kind: Namespace
metadata:
  name: namespace1


# apply of the above yaml file.  
kubectl create - ./my-namespace.yaml

```

```
kubectl get namespaces namespace1
```

```
kubectl get namespaces
NAME              STATUS   AGE
default           Active   35h
kube-node-lease   Active   35h
kube-public       Active   35h
kube-system       Active   35h

 
kubectl get namespaces kube-system
NAME          STATUS   AGE
kube-system   Active   35h
 
kubectl get namespaces default    
NAME      STATUS   AGE
default   Active   35h

```

```
kubectl describe namespaces default
Name:         default
Labels:       kubernetes.io/metadata.name=default
Annotations:  <none>
Status:       Active

No resource quota.

No LimitRange resource.
```

<br>
Note:

The namespace name shoud be a valid DNS name.


```
kubectl get pods --namespace=<insert-namespace-name-here>
kubectl get pods --namespace=kube-system

But in this case, "minify" will not get modify. So its good to use get-context...
kubectl config view --minify | grep namespace:


##
kubectl config --help

- current-context   Display the current-context
- get-contexts      Describe one or many contexts
- set-context       Set a context entry in kubeconfig
- use-context       Set the current-context in a kubeconfig file

- get-clusters      Display clusters defined in the kubeconfig
- set-cluster       Set a cluster entry in kubeconfig

```

<br>
<br>

`Setting the namespace preference`:

You can permanently save the namespace for all subsequent kubectl commands in that context.

```

kubectl config use-context my-dev
Switched to context "my-dev".

or

kubectl config set-context --current --namespace=<namespace-name-here>

kubectl config set-context --current --namespace=my-dev

output:
Context "minikube" modified.

kubectl config view --minify | grep namespace:         

output:
namespace: my-dev
```

<br>

`Validate it`

kubectl config view --minify | grep namespace:






