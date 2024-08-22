# Kubernetes QA

**Table of Content** <a id="Home"></a>
- [context-vs-namespace](#context-vs-namespace)
- [resource-vs-object-vs-kind](#resource-vs-object-vs-kind)
- [kubectl-syntax](#kubectl-syntax)





<!-- Table of content -->


<br><br>

<!------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------>

<br>
<a id="context-vs-namespace"></a>

## What is the difference between context and namespace in kubernetes? [⇪](#Home) 

Kubernetes Namespace:
When we create a kubernetes cluster, we can create different environments within this cluster. So, we try to group the resources depends on different environment, and each of them are called a "namespace."

Another example, we have few of the following `namespace`:
- default
- kube-system

```
kubectl get namespaces
NAME              STATUS   AGE
default           Active   9d
kube-node-lease   Active   9d
kube-public       Active   9d
kube-system       Active   9d
my-dev            Active   8d
```

The resource name need to be within a nameapces and we can also do quotas in per namespace level. 

<br>

Kubernetes Contexts:
- Its one level up to the `namespace`.
An organizatoin can have multiple kubernetes cluster. And we can configure which user, which cluster and which default namespace by default we can communicate. This is what we can define in `context`.


### Quick Differences:

|Feature	   |             Namespaces	                |            Contexts                 |
|--------------|----------------------------------------|-------------------------------------|
|Scope	       |Within a single cluster	                |Across multiple clusters             |
|Purpose	   |Isolate resources, enforce policies	    |Manage cluster connections           |
|Object	       |Resources (Pods, Deployments, etc.)	    |Cluster, user, default namespace     |
|Configuration |Managed by kubectl create namespace	    |Managed by kubectl config set-context|


<br><br>


<!------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------>


<a id="resource-vs-object-vs-kind"></a>

## what is the difference between resource, object and kind in kubernetes ? [⇪](#Home) 

<br>

### Analogy

Imagine a library:

`Resource`: The library itself (a collection of books).

`Object`: A specific book in the library.

`Kind`: The genre of the book (e.g., fiction, non-fiction).

<br>

### Example:

Let's take a `Pod` as an example:

- The `pods` is a `resource`.

- A specific `Pod` with the name `my-pod` is an `object`.

- The `Pod` is the `kind` of this `object`, defining its structure and attributes.


<br>

### Resource:

In Kubernetes, a resource is a collection of API objects of a specific type.  It's essentially an endpoint in the Kubernetes API. 
 
 For example, the `pods` resource is a `collection of Pod objects`

<br>

### Object:

An object is an `instance of a resource`. It's a concrete representation of a concept within the cluster, such as a `Pod`, `Deployment`, or `Service`. 

 Objects have a defined schema (their kind) and contain information about their desired state and actual state.


<br>

### Kind:

The kind specifies the type of an object.

 It's the schema that defines the structure and attributes of an object. For instance, the `Pod` kind defines the structure of a Pod object, including its containers, volumes, and other properties














<br><br>


<!------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------>


<a id="kubectl-syntax"></a>

## What is the kubectl syntax? [⇪](#Home) 

```
kubectl [command] [TYPE] [NAME] [flags]
```

<br>

`command`: Specifies the operation that you want to perform on one or more resources, for example `create`, `get`, `describe`, `delete`

`TYPE`: Specifies the `resource type`. Resource types are case-insensitive and you can specify the singular, plural, or abbreviated forms. For example, the following commands produce the same output:

```
kubectl get pod pod1
kubectl get pods pod1
kubectl get po pod1
```

<br>

`NAME`: Specifies the `name of the resource`. Names are `case-sensitive`. If the name is omitted, details for all resources are displaye., 

For example `kubectl get pods`.





<br><br>


## resource type:

https://kubernetes.io/docs/reference/kubectl/#resource-types

`kubectl api-resources`


<br><br>
---

### Kuberbetes Objects

```
Common Options
Configuration Files (Manifest files)
Cluster Management & Context
Daemonsets
Deployments
Events
Logs
Namespaces
Nodes
Pods
Replication Controllers
ReplicaSets
Secrets
Services
Service Accounts

```

<br><br>
---




<br><br>
---

### Listing kubernet Kind:

```
kubectl api-resources
NAME                              SHORTNAMES   APIVERSION                             NAMESPACED   KIND
bindings                                       v1                                     true         Binding
componentstatuses                 cs           v1                                     false        ComponentStatus
configmaps                        cm           v1                                     true         ConfigMap
endpoints                         ep           v1                                     true         Endpoints
events                            ev           v1                                     true         Event
limitranges                       limits       v1                                     true         LimitRange
namespaces                        ns           v1                                     false        Namespace
nodes                             no           v1                                     false        Node
persistentvolumeclaims            pvc          v1                                     true         PersistentVolumeClaim
persistentvolumes                 pv           v1                                     false        PersistentVolume
pods                              po           v1                                     true         Pod
podtemplates                                   v1                                     true         PodTemplate
replicationcontrollers            rc           v1                                     true         ReplicationController
resourcequotas                    quota        v1                                     true         ResourceQuota
secrets                                        v1                                     true         Secret
serviceaccounts                   sa           v1                                     true         ServiceAccount
services                          svc          v1                                     true         Service
mutatingwebhookconfigurations                  admissionregistration.k8s.io/v1        false        MutatingWebhookConfiguration
validatingwebhookconfigurations                admissionregistration.k8s.io/v1        false        ValidatingWebhookConfiguration
customresourcedefinitions         crd,crds     apiextensions.k8s.io/v1                false        CustomResourceDefinition
apiservices                                    apiregistration.k8s.io/v1              false        APIService
controllerrevisions                            apps/v1                                true         ControllerRevision
daemonsets                        ds           apps/v1                                true         DaemonSet
deployments                       deploy       apps/v1                                true         Deployment
replicasets                       rs           apps/v1                                true         ReplicaSet
statefulsets                      sts          apps/v1                                true         StatefulSet
tokenreviews                                   authentication.k8s.io/v1               false        TokenReview
localsubjectaccessreviews                      authorization.k8s.io/v1                true         LocalSubjectAccessReview
selfsubjectaccessreviews                       authorization.k8s.io/v1                false        SelfSubjectAccessReview
selfsubjectrulesreviews                        authorization.k8s.io/v1                false        SelfSubjectRulesReview
subjectaccessreviews                           authorization.k8s.io/v1                false        SubjectAccessReview
horizontalpodautoscalers          hpa          autoscaling/v2                         true         HorizontalPodAutoscaler
cronjobs                          cj           batch/v1                               true         CronJob
jobs                                           batch/v1                               true         Job
certificatesigningrequests        csr          certificates.k8s.io/v1                 false        CertificateSigningRequest
leases                                         coordination.k8s.io/v1                 true         Lease
endpointslices                                 discovery.k8s.io/v1                    true         EndpointSlice
events                            ev           events.k8s.io/v1                       true         Event
flowschemas                                    flowcontrol.apiserver.k8s.io/v1beta3   false        FlowSchema
prioritylevelconfigurations                    flowcontrol.apiserver.k8s.io/v1beta3   false        PriorityLevelConfiguration
ingressclasses                                 networking.k8s.io/v1                   false        IngressClass
ingresses                         ing          networking.k8s.io/v1                   true         Ingress
networkpolicies                   netpol       networking.k8s.io/v1                   true         NetworkPolicy
runtimeclasses                                 node.k8s.io/v1                         false        RuntimeClass
poddisruptionbudgets              pdb          policy/v1                              true         PodDisruptionBudget
clusterrolebindings                            rbac.authorization.k8s.io/v1           false        ClusterRoleBinding
clusterroles                                   rbac.authorization.k8s.io/v1           false        ClusterRole
rolebindings                                   rbac.authorization.k8s.io/v1           true         RoleBinding
roles                                          rbac.authorization.k8s.io/v1           true         Role
priorityclasses                   pc           scheduling.k8s.io/v1                   false        PriorityClass
csidrivers                                     storage.k8s.io/v1                      false        CSIDriver
csinodes                                       storage.k8s.io/v1                      false        CSINode
csistoragecapacities                           storage.k8s.io/v1                      true         CSIStorageCapacity
storageclasses                    sc           storage.k8s.io/v1                      false        StorageClass
volumeattachments                              storage.k8s.io/v1                      false        VolumeAttachment

```






