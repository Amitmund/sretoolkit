
# Kubernetes Jargon:


<br>
<br>
<br>
<br>

---

# Quick README notes related to kubernetes.

- https://kubernetes.io/docs/home/
- https://medium.com/@seifeddinerajhi




- Documentation
- Getting Started
- Concepts
- Tasks
- Tutorials
- Reference
- Contribute



<br>
<br>
<br>
<br>

---


### Controller-manager

```
The `controller-manager` is responsible for running various `controllers` that `regulate behavior` in the cluster.

Example: 
Ensuring that all of the replicas of a service are availale and healthy.
```

<br>
<br>

---



### scheduler

```
The `scheduler` is responsible for placing different `Pods` onto different nodes in the cluster.
```


<br>
<br>

---

### etcd

```
The `etcd` server is the `storage` for the cluster where all of the `API` object are stored.
```

<br>
<br>

---








- relieable

- scalable distributed system

- minikube

- docker-in-docker

- kubeadm

- kubernetes cron jobs


<br>
<br>
<br>
<br>

---

### daemon sets

https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/


```
What is Kubernetes Daemonset? DaemonSet is a Kubernetes feature that lets you run a Kubernetes pod on all cluster nodes that meet certain criteria. Every time a new node is added to a cluster, the pod is added to it, and when a node is removed from the cluster, the pod is removed.
```

<br>
<br>
<br>
<br>

---

### deployments

```
A Kubernetes deployment represents the desired state for your application pods and ReplicaSets. It allows you to declare how many replicas of a pod should be running at a given time. If pods fail or need to be updated, the deployment ensures the desired state is maintained by starting new pods.

```


<br>
<br>
<br>
<br>

---


- jobs



<br>
<br>
<br>
<br>

---

- pods

- replica sets

- replication controllers

- stateful sets

- services

- ingresses

- ingress classes

- config maps

- persistent volume claims

- secrets

- storage classes

- cluster

- cluster role bindings

- cluster roles

- events


<br>
<br>
<br>
<br>

---


### namespaces

https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/


In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. 

Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects (e.g. Deployments, Services, etc.) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc.).

Namespaces cannot be nested inside one another and each Kubernetes `resource can only be in one namespace`.

Namespaces are a way to divide cluster resources between multiple users (via resource quota).

Kubernetes namespaces are a method by which a single cluster used by an organization can be divided and categorized into multiple sub-clusters and managed individually.

- In general, there is a default namespace where all the resources exist.

- When are the namespaces used:
    - Project Compartmentalization.
    - Sandbox Development
    - Access and Permissions
    - Resource Control

- Benefits of kubernetes namespaces
    - Optimization and Efficiency
    - Easy Resource Distribution
    - Insident Response
    - Increased Scalability

<br>

For a production cluster, consider not using the default namespace. Instead, make other namespaces and use those.

<br>


`Initial namespaces`

```
Kubernetes starts with four initial namespaces:

default:

Kubernetes includes this namespace so that you can start using your new cluster without first creating a namespace.


kube-node-lease:

This namespace holds Lease objects associated with each node. Node leases allow the kubelet to send heartbeats so that the control plane can detect node failure.


kube-public:

This namespace is readable by all clients (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.


kube-system:

The namespace for objects created by the Kubernetes system.

```

Avoid creating namespaces with the prefix `kube-`, since it is reserved for Kubernetes system namespaces.

```
kubectl get pods --namespace=<insert-namespace-name-here>
```


<br>
<br>
<br>
<br>

---

### resource quota








<br>
<br>
<br>
<br>

---

- network policies

- nodes

- persistent volumes

- role bindings

- roles

- service accounts

- coredns

- kube-apiserver

- kube-proxy

- storage-provisioner

- labes


<br>
<br>
<br>
<br>

---

### Links:

- https://medium.com/slalom-technology/5-constructs-you-must-know-to-get-started-with-kubernetes-85e0079f9ace
- https://chkrishna.medium.com/kubernetes-objects-e0a8b93b5cdc




`pod`:

```
pod is the smallest deployable unit that exists in Kubernetes. Pods are simply a collection of containers with shared network and storage.
```

<br>

`Deployment`:

```
A deployment is a Kubernetes construct that controls the creation and destruction of pods. This construct is particularly important because it is what keeps our application alive! A deployment is essentially a contract you make with Kubernetes that states the running conditions of your application. To better understand what we’re talking about, let’s take a look at the following declarative YAML file.
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-kubernetes
spec:
  selector:
    matchLabels:
      app: hello-kubernetes
  replicas: 1
  template:
    metadata:
      labels:
        app: hello-kubernetes
    spec:
      containers:
      - name: hello-kubernetes
        image: docker.io/bricerisingslalom/hello-k8s:latest
        ports:
        - containerPort: 80
```

```
kubectl apply -f path/to/deployment.yaml
```


<br>

`Service`:

```
A deployment ensures that our application is running inside of our cluster, but we have no way to access it from outside! This is where a service comes in handy. A service is used to manage how network traffic makes it to pods running somewhere within a cluster.
```

```
kind: Service
apiVersion: v1
metadata:
  name: hello-kubernetes
spec:
  type: NodePort
  selector:
    app: hello-kubernetes
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```


<br>

`ConfigMaps` and `Secrets`

```
ConfigMaps and Secrets are actually two different Kubernetes constructs, but they are both used to externalize pod configurations; also, 5 is a more clickbaity number than 6. Both ConfigMaps and Secrets are essentially key-value stores that you can use to inject application configurations either as environment variables or a configuration file on your pods.
```

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-kubernetes
data:
  CONFIGMAP_CONFIG: Custom configmap config!
```

```
apiVersion: v1
kind: Secret
metadata:
  name: hello-kubernetes
type: Opaque
data:
  SECRET_CONFIG: Q3VzdG9tIHNlY3JldCBjb25maWch

```

