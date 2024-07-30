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

```
Template files << values.yaml << User-supplied values files
```

The following are some examples of the information that can be found in a `values.yaml` file:


- Image name and tag for a container image. 
- Number of replicas for a Deployment.
- Port numberfor a Service.
- Environment variables for a container.


> For mac: brew install helm

```
helm --help
The Kubernetes package manager

Common actions for Helm:

- helm search:    search for charts
- helm pull:      download a chart to your local directory to view
- helm install:   upload the chart to Kubernetes
- helm list:      list releases of charts

Environment variables:

| Name                               | Description                                                                                                |
|------------------------------------|------------------------------------------------------------------------------------------------------------|
| $HELM_CACHE_HOME                   | set an alternative location for storing cached files.                                                      |
| $HELM_CONFIG_HOME                  | set an alternative location for storing Helm configuration.                                                |
| $HELM_DATA_HOME                    | set an alternative location for storing Helm data.                                                         |
| $HELM_DEBUG                        | indicate whether or not Helm is running in Debug mode                                                      |
| $HELM_DRIVER                       | set the backend storage driver. Values are: configmap, secret, memory, sql.                                |
| $HELM_DRIVER_SQL_CONNECTION_STRING | set the connection string the SQL storage driver should use.                                               |
| $HELM_MAX_HISTORY                  | set the maximum number of helm release history.                                                            |
| $HELM_NAMESPACE                    | set the namespace used for the helm operations.                                                            |
| $HELM_NO_PLUGINS                   | disable plugins. Set HELM_NO_PLUGINS=1 to disable plugins.                                                 |
| $HELM_PLUGINS                      | set the path to the plugins directory                                                                      |
| $HELM_REGISTRY_CONFIG              | set the path to the registry config file.                                                                  |
| $HELM_REPOSITORY_CACHE             | set the path to the repository cache directory                                                             |
| $HELM_REPOSITORY_CONFIG            | set the path to the repositories file.                                                                     |
| $KUBECONFIG                        | set an alternative Kubernetes configuration file (default "~/.kube/config")                                |
| $HELM_KUBEAPISERVER                | set the Kubernetes API Server Endpoint for authentication                                                  |
| $HELM_KUBECAFILE                   | set the Kubernetes certificate authority file.                                                             |
| $HELM_KUBEASGROUPS                 | set the Groups to use for impersonation using a comma-separated list.                                      |
| $HELM_KUBEASUSER                   | set the Username to impersonate for the operation.                                                         |
| $HELM_KUBECONTEXT                  | set the name of the kubeconfig context.                                                                    |
| $HELM_KUBETOKEN                    | set the Bearer KubeToken used for authentication.                                                          |
| $HELM_KUBEINSECURE_SKIP_TLS_VERIFY | indicate if the Kubernetes API server's certificate validation should be skipped (insecure)                |
| $HELM_KUBETLS_SERVER_NAME          | set the server name used to validate the Kubernetes API server certificate                                 |
| $HELM_BURST_LIMIT                  | set the default burst limit in the case the server contains many CRDs (default 100, -1 to disable)         |
| $HELM_QPS                          | set the Queries Per Second in cases where a high number of calls exceed the option for higher burst values |

Helm stores cache, configuration, and data based on the following configuration order:

- If a HELM_*_HOME environment variable is set, it will be used
- Otherwise, on systems supporting the XDG base directory specification, the XDG variables will be used
- When no other location is set a default location will be used based on the operating system

By default, the default directories depend on the Operating System. The defaults are listed below:

| Operating System | Cache Path                | Configuration Path             | Data Path               |
|------------------|---------------------------|--------------------------------|-------------------------|
| Linux            | $HOME/.cache/helm         | $HOME/.config/helm             | $HOME/.local/share/helm |
| macOS            | $HOME/Library/Caches/helm | $HOME/Library/Preferences/helm | $HOME/Library/helm      |
| Windows          | %TEMP%\helm               | %APPDATA%\helm                 | %APPDATA%\helm          |

Usage:
  helm [command]

Available Commands:
  completion  generate autocompletion scripts for the specified shell
  create      create a new chart with the given name
  dependency  manage a chart's dependencies
  env         helm client environment information
  get         download extended information of a named release
  help        Help about any command
  history     fetch release history
  install     install a chart
  lint        examine a chart for possible issues
  list        list releases
  package     package a chart directory into a chart archive
  plugin      install, list, or uninstall Helm plugins
  pull        download a chart from a repository and (optionally) unpack it in local directory
  push        push a chart to remote
  registry    login to or logout from a registry
  repo        add, list, remove, update, and index chart repositories
  rollback    roll back a release to a previous revision
  search      search for a keyword in charts
  show        show information of a chart
  status      display the status of the named release
  template    locally render templates
  test        run tests for a release
  uninstall   uninstall a release
  upgrade     upgrade a release
  verify      verify that a chart at the given path has been signed and is valid
  version     print the client version information

Flags:
      --burst-limit int                 client-side default throttling limit (default 100)
      --debug                           enable verbose output
  -h, --help                            help for helm
      --kube-apiserver string           the address and the port for the Kubernetes API server
      --kube-as-group stringArray       group to impersonate for the operation, this flag can be repeated to specify multiple groups.
      --kube-as-user string             username to impersonate for the operation
      --kube-ca-file string             the certificate authority file for the Kubernetes API server connection
      --kube-context string             name of the kubeconfig context to use
      --kube-insecure-skip-tls-verify   if true, the Kubernetes API server's certificate will not be checked for validity. This will make your HTTPS connections insecure
      --kube-tls-server-name string     server name to use for Kubernetes API server certificate validation. If it is not provided, the hostname used to contact the server is used
      --kube-token string               bearer token used for authentication
      --kubeconfig string               path to the kubeconfig file
  -n, --namespace string                namespace scope for this request
      --qps float32                     queries per second used when communicating with the Kubernetes API, not including bursting
      --registry-config string          path to the registry config file (default "/Users/amitmund/Library/Preferences/helm/registry/config.json")
      --repository-cache string         path to the file containing cached repository indexes (default "/Users/amitmund/Library/Caches/helm/repository")
      --repository-config string        path to the file containing repository names and URLs (default "/Users/amitmund/Library/Preferences/helm/repositories.yaml")

Use "helm [command] --help" for more information about a command.

```

```
helm create mywebapp
cd mywebapp

```

<br>
<br>

```
helm create helm_app1

Output:
Creating helm_app1

cd helm_app1

# It has created 2 files and 2 directory.
ls
Chart.yaml      charts          templates       values.yaml

```

Example:

```
replicaCount: 1

image:
  repository: nginx
  tag: latest
  pullPolicy: ifNotPresent

service:
  port: 80
```

> Create deployment resources in deployment.yaml

Which is `templates/deployment.yaml`


<br>
<br>
<br>
<br>

---


