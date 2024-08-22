# Kubernetes objects


**Table of content:** <a id="Home"></a>
- [Pods](#Pods)
- [Deployment](#Deployment)
- [ReplicaSet](#ReplicaSet)
- [StatefulSet](#StatefulSet)
- [DaemonSets](#DaemonSets)
- [PersistentVolume](#PersistentVolume)
- [Stateful-vs-PersistentVolume](#Stateful-vs-PersistentVolume)
- [Service](#Service)
- [Namespaces](#Namespaces)
- [ConfigMaps-and-Secrets](#ConfigMaps-and-Secrets)
- [Jobs](#Jobs)




<!-- headings -->

<br><br>
<a id="Pods"></a>
### Pods [⇪](#Home)

Pods are the fundamental building blocks of the Kubernetes system. They are used to deploy, scale, and manage containerized applications in a cluster.

<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="Deployment"></a>
### Deployment [⇪](#Home)

In Kubernetes, a Deployment object is used to manage the lifecycle of one or more identical Pods. A Deployment allows you to declaratively manage the desired state of your application, such as the number of replicas, the image to use for the Pods, and the resources required. 

Declaratively managing the state means specifying the desired end state of an application, rather than describing the steps to reach that state.

When you create a Deployment, you provide a Pod template, which defines the configuration of the Pods that the Deployment will manage. The Deployment then creates Pods that match this template, using a ReplicaSet. A ReplicaSet is responsible for creating and scaling Pods, and for ensuring that Pods that fail are replaced. When you update a Deployment, it will update the ReplicaSet, which in turn updates the Pods.

It's important to note that Deployment objects are used to manage stateless applications. Stateless applications are those that do not maintain any persistent data or state. This means that if a container running the application crashes or is terminated, it can be easily replaced. There's no need to preserve any data before deleting the old container and replacing it with a new one. Examples of stateless applications include web servers and load balancers.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="ReplicaSet"></a>
### ReplicaSet [⇪](#Home)

- In Kubernetes, `Deployments don’t manage Pods directly`. 
- `That’s the job of the ReplicaSet object`. 
- When you create a `Deployment in Kubernetes, creates a ReplicaSet is created automatically`.
- The `ReplicaSet ensures that the desired number of replicas (copies) are running` at all times by creating or deleting Pods as needed.

To accomplish this, Kubernetes uses a concept called reconciliation loops. A reconciliation loop is a process that compares the desired state of a system with its current state and takes actions to bring the current state in line with the desired state.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="StatefulSet"></a>
### StatefulSet [⇪](#Home)

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

<a id="DaemonSets"></a>
### DaemonSets [⇪](#Home)

A DaemonSet `ensures that a copy of a Pod is running across all, or a subset of nodes in a Kubernetes cluster`.

Example: `You want a monitoring pods tools` need to be installed through-out your kubernetes cluster. 

DaemonSets are `useful for running system-level services`, such as `logging or monitoring agents`, that need to run on every node in a cluster. Logging agents are used to collect log data from all the nodes in a cluster and send it to a centralized logging system for storage and analysis. Monitoring agents are used to collect metrics and performance data from all the nodes in a cluster, and send it to a monitoring system for analysis and alerting.

Like `ReplicaSets, DaemonSets are managed by a reconciliation loop`. A reconciliation loop is a mechanism that continuously checks and compares the desired state of a resource with the current state. The loop runs periodically and ensures that the DaemonSet is always in the desired state, automatically creating or deleting Pods as necessary.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="PersistentVolume"></a>
### PersistentVolume [⇪](#Home)

PersistentVolume `represents a piece of storage that you can attach to your Pod(s)`.

The reason it's called "persistent" is because it's not tied to the life cycle of your Pod. In other words, even if your Pod gets deleted, the PersistentVolume will survive.

And there are a lot of different types of storage that you can attach using a PersistentVolume, like local disks, network storage, and cloud storage.

There are a few different `use cases for PersistentVolumes in Kubernetes`. One common use case is for `databases`. If you're running a database inside a Pod, you'll likely want to store the database files on a separate piece of storage that can persist even if the Pod gets deleted. And PersistentVolume can do that.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->


<a id="Stateful-vs-PersistentVolume"></a>
### Question: StatefulSet Vs PersistentVolume: [⇪](#Home)

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

<a id="Service"></a>
### Service [⇪](#Home)

A Kubernetes `Service` is `a way to access a group of Pods that provide the same functionality`. It creates a single, `consistent point of entry for clients to access the service`, regardless of the location of the Pods.

For example, imagine you have a Kubernetes cluster with multiple Pods running a web application. Each Pod has its own IP address, but this can change at any time if the Pod is moved to another node, or recreated. So the IP address becomes a "moving target". The destination(s) that clients should reach is unstable, and hard to track.

To make it easier for clients to access the web application, you can `create a Kubernetes Service that has a stable IP address`. Clients can then connect to that IP, and their requests will be routed to one of the Pods running the web application.

One of `the key benefits of using a Service is that it provides a stable endpoint that doesn't change even if the underlying Pods are recreated or replaced`. This makes it much easier to update and maintain the application, as clients don't need to be updated with new IP addresses.

Furthermore, the `Service also provides some simple load balancing`. If clients would connect to a certain IP address of a specific Pod, that Pod would be overused, while the other ones would be sitting idle, doing nothing. But the Service can spread out requests to multiple Pods (load balance). By spreading these out, all Pods are used equally. However, each one has less work to do, as it only receives a small part of the total number of incoming requests.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="Namespaces"></a>
### Namespaces [⇪](#Home)

A Kubernetes namespace is `a way to divide a single Kubernetes cluster into multiple virtual clusters`. This allows resources to be isolated from one another. Once a namespace is created, you can launch Kubernetes objects, like Pods, which will only exist in that namespace.

Imagine AppA, and AppB are almost identical. One is version 1.16 of an app, the other is version 1.17. They use almost the same objects, the same Pod structures, the same Services, and so on. Since they're so similar, there's a risk of them interfering with each other. For example, AppA might accidentally send requests to a similar Service or Pod used by AppB. But you want to test the new 1.17 version in a realistic scenario in the same cluster, using the same objects and definitions.


By using namespaces, you can `perform as many operations as you need while eliminating the risk of impacting resources that are in another namespace`. It's almost as if you have a second Kubernetes cluster. AppA runs in its own (virtual) cluster. AppB runs in a separate (virtual) cluster. But you don't actually have to go through the trouble of setting up an additional cluster. AppA and AppB are logically isolated from each other when they exist in separate namespaces. Even if they run identical Pods that want to access Services with identical names, there's no risk of them interfering with each other.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="ConfigMaps-and-Secrets"></a>
### ConfigMaps & Secrets [⇪](#Home)

ConfigMaps and Secrets are two very important objects that `allow you to configure the apps that run in your Pods`. Configuring apps refers to setting various parameters or options that control the behaviors of the apps. This can include things like database connection strings or API keys.


`ConfigMaps are used to store non-sensitive configuration values`. For example, environment variables used to provide runtime configuration information such as the URL of an external API, rather than confidential information such as passwords, are considered non-sensitive data.

`Secrets, on the other hand, are meant to hold sensitive configuration values`, such as database passwords, API keys, and other information that only authorized apps should be able to access.

`ConfigMaps and Secrets can be injected into Pods with the help of environment variables`, command-line arguments, or configuration files included in the volumes attached to those Pods.

`By using ConfigMaps and Secrets, you decouple the applications running in your Pods from their configuration values`. This means you can easily update the configuration of your applications without having to rebuild or redeploy them.


<br><br>


<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<a id="Jobs"></a>
### Jobs [⇪](#Home)

A job object is used to `run specific tasks` that have the following properties:

- They are short-lived.
- They need to be executed once.
- But most importantly, Kubernetes has to make sure that the task has been executed correctly and finished its job.

- Somewhat like `cron jobs`.

An `example` of where a Kubernetes job can be useful is a `database backup`. This does not run continuously, so it's a short-lived process. It just needs to start, complete, then exit. It has to be executed once. Even if the backup needs to happen weekly, there will be one separate job per week (CronJobs can be used for jobs that repeat periodically).

Each job has to finish its own weekly task. But it needs to ensure that the Pod executing the backup fully completes this job. For example, a Pod might start a backup. But the database is huge, so this can take hours. For some reason, the backup process fails at 68% progress. Kubernetes sees that the Pod has failed the task, so it can create another one to retry. It will keep on retrying until, finally, one Pod manages to back up the entire database.

In this case, the job required one Pod, and one successful run for one Pod (to ensure the task was completed successfully). But other jobs might require multiple Pods (which can run in parallel) and/or multiple successful runs. For example, a job will be considered complete, only when at least 3 Pods had successful runs and achieved 100% progress on their tasks.
