# kubectl command

<br><br>

<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>



> docker run busybox echo "Hello World"

> docker run {image}:{tag}

> docker build -t amitmund .

> docker images

> docker run --name amitmund-container -p 8080:8080 -d amitmund

> docker ps

> docker inspect amitmund-container

> docker exec -it amitmund-container bash

> docker rm amitmund-container

> docker tag amitmund {username}/{imagename}

> docker images | head

<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


> kubectl cluster-info



<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


> gcloud container cluster create kubia --num-nodes 3 --machine-type f1-micro



<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

> kubectl get nodes

> kubectl describe node {one-of-k8s-node}

> kubectl run my-app1 --image=amitmund/my-app1 --port=8080 --generator=run/v1
replicationcontroller "my-app1" created

> kubectl get pods

> kubectl expose rc my-app1 --type=LoadBalancer --name my-app1-service

> kubectl get services

> kubectl get replicationcontrollers

> kubectl scale rc my-app1 --replicas=3

> kubectl get rc

> kubectl get pods

> kubectl get pods -o wide

> kubectl describe pod {your-pod-name}

<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


> kubectl cluster-info | grep dashboard


> gcloud container clusters describe {your-cluster-name} | grep -E "(username|password):"

> minikube dashboard

<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

kubectl get po {your-pod} -o yaml


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

> kubectl explain pods

> kubectl explain pods.spec


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

> kubectl create -f my-pod1.yaml




<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>



> kubectl get pod etcd-minikube -o yaml --namespace kube-system


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

> docker logs {container id}

> kubectl port-forward my-pod 8888:8080





<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## labes

> kubectl get po --show-labels

> kubectl get po -L creation_method,env

> kubectl label po my-pods creator=amitmund

> kubectl label po my-app-2 env=debug --overwrite

> kubectl get po -L creation_method,env

> kubectl get po -l creation_method=manual

> kubectl get po -l env


### excluding a label.
> kubectl get po -l '!env'





<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## Node label

> kubectl label node your-cluster-node key=value

> kubectl label node my-node1 ssh=true gpu=true


> kubectl get nodes -l gpu=true

> kubectl get nodes -L gpu


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## Annotations

> kubectl get pod pod-name -o yaml | grep -A2 "annotations:"


```
kubectl get pods etcd-minikube -n kube-system -o yaml | grep -i -A2 "annotations"
  annotations:
    kubeadm.kubernetes.io/etcd.advertise-client-urls: https://10.0.2.15:2379
    kubernetes.io/config.hash: d3bb814607b61262cc219c8020a27fc0
```

> kubectl annotate pod my-app1 mycompany.com/someannotation="foo bar"



## Adding and modifying annotations

> kubectl annotate pod my-app1 mycompany.com/someannotation="foo bar"


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


## get namespaces


> kubectl get ns

> kubectl get pod --namespace kube-system

> kubectl get po -n kube-system


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


### Creating namespace from a YAML file  "custom-namespace.yaml" 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: custom-namespace
```

<br>

> kubectl create -f custom-namespace.yaml

> kubectl create namespace custom-namespace1


> alias kcd='kubectl config set-context $(kubectl config current- context) --namespace '


<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## creating objects in other namespaces

> kubectl create -f my-app1.yaml -n custom-namespace
> kubectl create -f my-app1.yaml --namespace custom-namespace



<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## To switch between namespaces

Set the following alias in your bash profile.

> alias ks-ns='kubectl config set-context $(kubectl config current-context) --namespace '

> ks-ns some-namespace



<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## Deleting pod (not using deployment or replication controller)

> kubectl delete pod my-app1-pod1

> kubectl delete po -l creation_method=manual

> kubectl delete po -l rel=canary

<br>

> kubectl get ns

> kubectl delete ns custom-namespace1

> kubectl get ns





<br> <br>
<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


## `kubectl get`

Prints a table of the `most important information` about the `specified resources`. 

You can filter the list `using a label selector` and the `--selector` flag.

If the `desired resource type is namespaced` you will `only see results in your current
namespace` unless you pass `--all-namespaces`.

<br>

### options:

`kubectl get --help` to get further details about "get options".     







<br><br>

<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


## kubectl describe




<br><br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


## kubectl --help

```
kubectl --help
kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/

Basic Commands (Beginner):
  create          Create a resource from a file or from stdin
  expose          Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
  run             Run a particular image on the cluster
  set             Set specific features on objects

Basic Commands (Intermediate):
  explain         Get documentation for a resource
  get             Display one or many resources
  edit            Edit a resource on the server
  delete          Delete resources by file names, stdin, resources and names, or by resources and label selector

Deploy Commands:
  rollout         Manage the rollout of a resource
  scale           Set a new size for a deployment, replica set, or replication controller
  autoscale       Auto-scale a deployment, replica set, stateful set, or replication controller

Cluster Management Commands:
  certificate     Modify certificate resources
  cluster-info    Display cluster information
  top             Display resource (CPU/memory) usage
  cordon          Mark node as unschedulable
  uncordon        Mark node as schedulable
  drain           Drain node in preparation for maintenance
  taint           Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe        Show details of a specific resource or group of resources
  logs            Print the logs for a container in a pod
  attach          Attach to a running container
  exec            Execute a command in a container
  port-forward    Forward one or more local ports to a pod
  proxy           Run a proxy to the Kubernetes API server
  cp              Copy files and directories to and from containers
  auth            Inspect authorization
  debug           Create debugging sessions for troubleshooting workloads and nodes
  events          List events

Advanced Commands:
  diff            Diff the live version against a would-be applied version
  apply           Apply a configuration to a resource by file name or stdin
  patch           Update fields of a resource
  replace         Replace a resource by file name or stdin
  wait            Experimental: Wait for a specific condition on one or many resources
  kustomize       Build a kustomization target from a directory or URL

Settings Commands:
  label           Update the labels on a resource
  annotate        Update the annotations on a resource
  completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

Other Commands:
  api-resources   Print the supported API resources on the server
  api-versions    Print the supported API versions on the server, in the form of "group/version"
  config          Modify kubeconfig files
  plugin          Provides utilities for interacting with plugins
  version         Print the client and server version information

Usage:
  kubectl [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
```

<br><br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

## kubecl api-resources

```
NAME


bindings
componentstatuses
configmaps
endpoints
events
limitranges
namespaces
nodes
persistentvolumeclaims
persistentvolumes
pods
podtemplates
replicationcontrollers
resourcequotas
secrets
serviceaccounts
services
mutatingwebhookconfigurations
validatingwebhookconfigurations
customresourcedefinitions
apiservices
controllerrevisions
daemonsets
deployments
replicasets
statefulsets
tokenreviews
localsubjectaccessreviews
selfsubjectaccessreviews
selfsubjectrulesreviews
subjectaccessreviews
horizontalpodautoscalers
cronjobs
jobs
certificatesigningrequests
leases
endpointslices
events
flowschemas
prioritylevelconfigurations
ingressclasses
ingresses
networkpolicies
runtimeclasses
poddisruptionbudgets
clusterrolebindings
clusterroles
rolebindings
roles
priorityclasses
csidrivers
csinodes
csistoragecapacities
storageclasses
volumeattachments
```


<br><br>

<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>

