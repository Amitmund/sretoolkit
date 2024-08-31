
## Chapter 5 (Services):

- In the case of microservices, pods will usually respond to HTTP requests coming either from other pods inside the cluster or from clients outside the cluster.

- Pods are ephemeral—They may come and go at any time.
                                                                   
- Kubernetes assigns an IP address to a pod after the pod has been scheduled to a node and before it’s started

- Horizontal scaling means multiple pods may provide the same service

### Introducing Services:

- A Kubernetes Service is a resource you create to make a single, constant point of entry to a group of pods providing the same service.

- Each service has an IP address and port that never change while the service exists.

- A service can be backed by more than one pod.

- It worked based on the "label selector".

- Label selectors determine which pods belong to the Service.


```
Service: my-service
Selector: app=my-app
```

<br>

```
apiVersion: v1
kind: Service
metadata:
  name: my_service
spec:
  ports:
  - port: 80
    targetPort: 8080
  selector:
app: my_app
```

> kubectl create my-service.yaml

- verify the service:

> kubectl get service

> kubectl get svc

#### if command don't have any options, we don't have to use `--`
> kubectl exec my-pod -- curl -s http://the-client-port






