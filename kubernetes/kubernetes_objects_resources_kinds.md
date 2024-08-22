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

