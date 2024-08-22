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

- In Kubernetes, Deployments don’t manage Pods directly. 
- That’s the job of the ReplicaSet object. 
- When you create a Deployment in Kubernetes, a ReplicaSet is created automatically.
- The ReplicaSet ensures that the desired number of replicas (copies) are running at all times by creating or deleting Pods as needed.

To accomplish this, Kubernetes uses a concept called reconciliation loops. A reconciliation loop is a process that compares the desired state of a system with its current state and takes actions to bring the current state in line with the desired state.



