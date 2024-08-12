# lifecycle of pod

Understanding the `pod lifecycle` is important because it provides insight into the different stages that a pod goes through, from `creation` to `termination`, and the actions that are taken by the system at each stage.

<br>

#### Links:
- https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions

- https://pwittrock.github.io/docs/concepts/workloads/pods/pod-lifecycle/

<br>


#### `state` of of pod:

<br>

![Alt text](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vg1x1jEQ8pWyNzu9.png "Pod State")

<br><br>

![Alt text](https://miro.medium.com/v2/format:webp/1*WDJmiyarVfcsDp6X1-lLFQ.png "Pod creation")



- Pending 

    - Pod is waiting to be `scheduled` and the `worker node is already assigned`. The images of its containers are pulled and started, it remains in this phase.

- Running 
    - A Pod is to be in the `running` phase, when it's `linkedin to a node`, and `all the containers are active`.

- `Succeeded`
    - All Containers in the Pod have `terminated successfully`, and will not be restarted.

- Failed
    - All container(s) of the Pod have exited and at least one container has returned non-zero status.


- Unknown
    - The state of the pod is shown as `unknown`, when the `kubelet` stops reporting to the API server.

- CrashLoopBack
    - The container fails to start and is tried again and again.


- Terminated


<br>

The pod’s status field is a PodStatus object, which has a phase field. 

