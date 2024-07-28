# minikube related details

- https://minikube.sigs.k8s.io/docs/start/


### Managing minikube cluster
```
# start minikube cluster
minikube start

# Access the Kubernetes dashboard running within the minikube cluster:
minikube dashboard

# pause minikube cluster
minikube pause

# unpause minikube cluster
minikube unpause

# stop minikube cluster
minikube stop

# Change the default memory limit (requires a restart):
minikube config set memory 9001


# Browse the catalog of easily installed Kubernetes services:
minikube addons list


# Create a second cluster running an older Kubernetes release:
minikube start -p aged --kubernetes-version=v1.16.1


# Delete all of the minikube clusters:
minikube delete --all

```

<br>
<br>
<br>
<br>

```
kubectl get pod
NAME              READY   STATUS    RESTARTS      AGE
web               1/1     Running   3 (13m ago)   268d
web-declarative   1/1     Running   3 (13m ago)   268d


kubectl get pod -A
NAMESPACE              NAME                                         READY   STATUS      RESTARTS       AGE
default                web                                          1/1     Running     3 (13m ago)    268d
default                web-declarative                              1/1     Running     3 (13m ago)    268d
ingress-nginx          ingress-nginx-admission-create-xc6cf         0/1     Completed   0              268d
ingress-nginx          ingress-nginx-admission-patch-26rv8          0/1     Completed   1              268d
ingress-nginx          ingress-nginx-controller-7799c6795f-bc5fd    1/1     Running     4 (13m ago)    268d
kube-system            coredns-5d78c9869d-dsrnh                     1/1     Running     5 (13m ago)    268d
kube-system            etcd-minikube                                1/1     Running     5 (13m ago)    268d
kube-system            kube-apiserver-minikube                      1/1     Running     5 (13m ago)    268d
kube-system            kube-controller-manager-minikube             1/1     Running     5 (13m ago)    268d
kube-system            kube-proxy-646rn                             1/1     Running     5 (13m ago)    268d
kube-system            kube-scheduler-minikube                      1/1     Running     5 (13m ago)    268d
kube-system            metrics-server-7746886d4f-7hhff              1/1     Running     3 (13m ago)    268d
kube-system            storage-provisioner                          1/1     Running     10 (12m ago)   268d
kubernetes-dashboard   dashboard-metrics-scraper-5dd9cbfd69-stn4j   1/1     Running     2 (13m ago)    173d
kubernetes-dashboard   kubernetes-dashboard-5c5cfc8747-6sfqh        1/1     Running     2 (13m ago)    173d

```
<br>
<br>
<br>
<br>


### minikube to download the appropriate version of kubectl

```
minikune kubectl -- get po -A
```





