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






<br>

---

<br>
<br>


<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>




## Just command for now, more details later


> kubectl get ns

> kubectl get po --namespace kube-system


<br><br>

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

> kubectl create namespace custom-namespace

> kubectl create -f kubia-manual.yaml -n custom-namespace

> alias kcd='kubectl config set-context $(kubectl config current- context) --namespace '


<br><br>

<!------------------------------------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------------>


> kubectl delete po kubia-gpu





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

