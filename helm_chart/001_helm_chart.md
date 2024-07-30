### What is Helm Chart?

Its an application package for kubernetes. like apt, yum or npm package manager. Its a set of files describing Kubernetes resources, such as `deployments`, `services` and `configuration files` necessary for running an application on kubernetes.


<br>
<br>
<br>
<br>

---


`Helm Charts` can be stored in remote repositories for easy sharing and distributing across kubernetes cluster.

Several YAML files define kubernetes resources for your application. You can create or modify these files based on your application's requirements. There are two main types of configuration files in Helm.

- ```Template files```

- ```Values files```

<br>

There are two types of `values file` in a Helm Chart:

- `values.yaml`: Contains default values for the templates in the Chart. It is typically including in every Chart.

- `User-supplied values files`: Can be used to `override the default values` in the `values.yaml` for when the Chart in installed. 



<br>
<br>
<br>
<br>

---

### Prerequisites:

Before creating the `Helm Chart`, make sure you have the following tools installed:

`Helm`: You will need installed on your local machine.

`kubernetes Cluster`: Ensure you have a running kubernetes cluster to deploy your application. You can set up a local cluster using tools like `Minikube` or a cloud-based kubernetes service.


<br>
<br>
<br>
<br>

---


### Helm Chart example:

Lets create a Helm Chart of a simple web application using NGINX.

1. Initialize the Helm Chart:

```
helm create mywebapp
cd mywebapp
```


2. Define your application in `values.yaml`

<br>

The `values.yaml` file contains `default values for the templates` in a Helm Chart. It is a YAML file that is typically included in every Chart. You can use it to override the defaults when the Chart is installed.

The following are some examples of the information that can be found in a `values.yaml` file:


