# Kubernetes objects

<br><br>

### Pods 

Pods are the fundamental building blocks of the Kubernetes system. They are used to deploy, scale, and manage containerized applications in a cluster.

<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


### Deployment

In Kubernetes, a Deployment object is used to manage the lifecycle of one or more identical Pods. A Deployment allows you to declaratively manage the desired state of your application, such as the number of replicas, the image to use for the Pods, and the resources required. 

Declaratively managing the state means specifying the desired end state of an application, rather than describing the steps to reach that state.

When you create a Deployment, you provide a Pod template, which defines the configuration of the Pods that the Deployment will manage. The Deployment then creates Pods that match this template, using a ReplicaSet. A ReplicaSet is responsible for creating and scaling Pods, and for ensuring that Pods that fail are replaced. When you update a Deployment, it will update the ReplicaSet, which in turn updates the Pods.

It's important to note that Deployment objects are used to manage stateless applications. Stateless applications are those that do not maintain any persistent data or state. This means that if a container running the application crashes or is terminated, it can be easily replaced. There's no need to preserve any data before deleting the old container and replacing it with a new one. Examples of stateless applications include web servers and load balancers.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


### ReplicaSet

- In Kubernetes, `Deployments don’t manage Pods directly`. 
- `That’s the job of the ReplicaSet object`. 
- When you create a `Deployment in Kubernetes, creates a ReplicaSet is created automatically`.
- The `ReplicaSet ensures that the desired number of replicas (copies) are running` at all times by creating or deleting Pods as needed.

To accomplish this, Kubernetes uses a concept called reconciliation loops. A reconciliation loop is a process that compares the desired state of a system with its current state and takes actions to bring the current state in line with the desired state.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


### StatefulSet

- A StatefulSet is a Kubernetes object that is used to manage stateful applications.
- This state is typically stored in a persistent storage backend, such as a disk, or a database
- The state is maintained even if the underlying Pods/containers are recreated. 
- The most common example of a stateful component in applications is a database such as MySQL or MongoDB.

- The `StatefulSet ensures that each Pod is uniquely identified by a number, starting at zero`.

This allows for a consistent naming scheme for each Pod and its associated resources, such as persistent storage (for example, when Volumes are used).

When a `Pod in a StatefulSet must be replaced`, for example, due to node failure, the new Pod is assigned the same numeric identifier as the previous Pod. This ensures that the new Pod has the same unique identity and is attached to the same persistent storage (Volume) that the previous Pod was using.

This `allows for the preservation of state and data across Pod replacements`. This is important for applications that do work that periodically adds, removes, or changes some data. They basically need to remember "what has happened in the past" (previous state). For example, a Pod can add a new entry to a database, maybe the email address of a new user. If the Pod has to be recreated, you don't want to lose the email address that was previously added.

<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


### DaemonSets

A DaemonSet `ensures that a copy of a Pod is running across all, or a subset of nodes in a Kubernetes cluster`.

Example: `You want a monitoring pods tools` need to be installed through-out your kubernetes cluster. 

DaemonSets are `useful for running system-level services`, such as `logging or monitoring agents`, that need to run on every node in a cluster. Logging agents are used to collect log data from all the nodes in a cluster and send it to a centralized logging system for storage and analysis. Monitoring agents are used to collect metrics and performance data from all the nodes in a cluster, and send it to a monitoring system for analysis and alerting.

Like `ReplicaSets, DaemonSets are managed by a reconciliation loop`. A reconciliation loop is a mechanism that continuously checks and compares the desired state of a resource with the current state. The loop runs periodically and ensures that the DaemonSet is always in the desired state, automatically creating or deleting Pods as necessary.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


### PersistentVolume

PersistentVolume `represents a piece of storage that you can attach to your Pod(s)`.

The reason it's called "persistent" is because it's not tied to the life cycle of your Pod. In other words, even if your Pod gets deleted, the PersistentVolume will survive.

And there are a lot of different types of storage that you can attach using a PersistentVolume, like local disks, network storage, and cloud storage.

There are a few different `use cases for PersistentVolumes in Kubernetes`. One common use case is for `databases`. If you're running a database inside a Pod, you'll likely want to store the database files on a separate piece of storage that can persist even if the Pod gets deleted. And PersistentVolume can do that.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->



### Question: StatefulSet Vs PersistentVolume:

#### Key differences

`Purpose`: PVs focus on providing persistent storage, while StatefulSets focus on managing stateful applications with persistent identity and ordering.

`Scope`: PVs can be used across multiple components, whereas StatefulSets are designed for a specific set of pods with unique identities.

`Data sharing`: PVs allow data sharing across pods, whereas StatefulSets ensure each pod has its own unique persistent volume.

#### When to use each

Use `PVs` when you need to provide `persistent storage for a stateless application or a component that doesn’t require sticky identities.`

Use `StatefulSets` when you n`eed to manage a stateful application` with persistent identity and ordering, such as databases, messaging systems, or distributed systems with unique node identities.


In summary, `Persistent Volumes provide persistent storage`, while `StatefulSets manage stateful applications with sticky identities and ordering`. 

Choose StatefulSets when your application requires persistent identity and ordering, and PVs when you need persistent storage for a stateless application.



<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

### Service

A Kubernetes `Service` is `a way to access a group of Pods that provide the same functionality`. It creates a single, `consistent point of entry for clients to access the service`, regardless of the location of the Pods.

For example, imagine you have a Kubernetes cluster with multiple Pods running a web application. Each Pod has its own IP address, but this can change at any time if the Pod is moved to another node, or recreated. So the IP address becomes a "moving target". The destination(s) that clients should reach is unstable, and hard to track.

To make it easier for clients to access the web application, you can `create a Kubernetes Service that has a stable IP address`. Clients can then connect to that IP, and their requests will be routed to one of the Pods running the web application.

One of `the key benefits of using a Service is that it provides a stable endpoint that doesn't change even if the underlying Pods are recreated or replaced`. This makes it much easier to update and maintain the application, as clients don't need to be updated with new IP addresses.

Furthermore, the `Service also provides some simple load balancing`. If clients would connect to a certain IP address of a specific Pod, that Pod would be overused, while the other ones would be sitting idle, doing nothing. But the Service can spread out requests to multiple Pods (load balance). By spreading these out, all Pods are used equally. However, each one has less work to do, as it only receives a small part of the total number of incoming requests.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

### Namespaces

A Kubernetes namespace is `a way to divide a single Kubernetes cluster into multiple virtual clusters`. This allows resources to be isolated from one another. Once a namespace is created, you can launch Kubernetes objects, like Pods, which will only exist in that namespace.

