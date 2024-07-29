# Quick README notes related to kubernetes.

# Kubernetes Jargon:

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

- daemon sets

- deployments

- jobs

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





