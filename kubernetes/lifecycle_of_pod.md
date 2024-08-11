# lifecycle of pod

Understanding the `pod lifecycle` is important because it provides insight into the different stages that a pod goes through, from `creation` to `termination`, and the actions that are taken by the system at each stage.

<br>

Current `state` of of pod:

- Pending 

    - Pod is waiting to be `scheduled` and the worker node is already assigned. The images of its containers are pulled and started, it remains in this phase.

- Running 
    - 

    
- Failed
- Terminated


<br>

The pod’s status field is a PodStatus object, which has a phase field. 

<br>

![Alt text](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vg1x1jEQ8pWyNzu9.png "Pod State")