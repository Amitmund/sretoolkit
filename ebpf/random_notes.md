
## Links

https://www.youtube.com/watch?v=Eb_OGnLEzsA&list=PLDUda1obogQ87G2bxWum74tk0p2OjeJc8


## Quick notest:

Packet tracer:

- Packet tracer is a network simulator that allows you to create and test network topologies.

## Tools:
Dynamips/GNS3

## Things to understand:


### BGP protocol
- BGP is a routing protocol that allows for the exchange of routing information between autonomous systems.
- https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-bgp/
- 


### Speanning tree protocol:
- 


### masquerading
- What is masquerading: 
- NAT

### ifconfig is deprecated.

### ip ( start using ip command.)

### What is wireless mash network


### https://www.civo.com/



## OSI layer

(1) Physical > Its the physical layer of the OSI model. It defines the physical means of transmitting data between devices. It includes the physical media, such as copper cables, fiber optic cables, and wireless transmission. 
(2) Data Link > It is the second layer of the OSI model. It is responsible for framing, error detection and correction , and flow control. It is divided into two sublayers: the Media Access Control (MAC) sublayer and the Logical Link Control (LLC) sublayer. 
(3) Network > It is the third layer of the OSI model. It is responsible for routing data between devices on a network. It uses logical addresses, such as IP addresses, to identify devices on a network. 
(4) Transport > It is the fourth layer of the OSI model. It is responsible for providing reliable data transfer between devices . It uses protocols such as TCP and UDP to ensure that data is delivered in the correct order and that errors are detected and corrected.
(5) Session > It is the fifth layer of the OSI model. It is responsible for establishing, maintaining, and terminating connections between applications running on different devices. 
(6) Presentation > It is the sixth layer of the OSI model. It is responsible for converting data into a format that can be understood by the receiving device. It includes data compression, encryption, and formatting. 
(7) Application > 

Is the tools L7 (Example HTTP)
Is the tools is L4 (Example Port)
Is the tools is L3 (Example IP) (Globally identifiable address)
L2 --> Its knows the MAC address. (MAC learning...) (Locally idenifiable address.)


## CCA - Cilium certified associate exam
- Cilium Certified Associate (CCA)
- https://isovalent.com/blog/post/cilium-certified-associate-cca/ 
- 

```

https://isovalent.com/blog/post/cilium-certified-associate-cca/

Documentation
The Cilium docs are the primary reference for the exam. Make sure you are familiar with the core concepts explained in the Cilium docs. This includes:

Introduction to Cilium & Hubble
Cilium Component Overview
Cilium installation
Hubble Introduction
Hubble CLI
Cilium Terminology
Cilium Networking Concepts
Kubernetes Networking with Cilium
BGP with Cilium
LB IPAM
eBPF Datapath
Multi Cluster Networking
Cilium Service Mesh
Network Security with Cilium
Overview of Cilium Network Policy
Layer 7 Protocol Visibility
Cilium configuration
Cilium troubleshooting  

```


## RAFT algorathem
- RAFT is a distributed consensus algorithm that is used in distributed systems to achieve consensus among nodes.
- etcd takes part of for the leader k8s control plain


---
---

kubelet
API server
scheduler

### Under Kubernetes

CNI: Container Network Interface
CRI (CRI-O): Container Runtime Interface
CSI: Container Storage Interface

CNI plugins: calico, cilium, flannel, etc.
CRI plugins: containerd, rkt, etc.
CSI plugins: gluster, ceph, etc.

---
---

### Cilium
- Cilium is a network and security solution for Kubernetes that provides a single, unified platform for
- network and security policies.
- Cilium is built on top of eBPF (extended Berkeley Packet Filter) and provides
- a number of features, including:
- Network policies: Cilium provides a simple and flexible way to define network policies
- that can be applied to pods and services.
- Security policies: Cilium provides a number of security features, including
- network segmentation, traffic filtering, and intrusion detection.
- Service mesh: Cilium provides a service mesh that allows for the creation of
- service-level network policies and security policies.
- Monitoring and logging: Cilium provides a number of monitoring and logging features,
- including network traffic analysis and security event logging.
- Cilium is designed to be highly scalable and performant, and is
- optimized for use in large-scale Kubernetes environments.
- Cilium is also highly customizable, and provides a number of APIs and
- tools for customizing and extending its functionality.
- Cilium is a popular choice for Kubernetes environments that require
- advanced network and security features.
- Cilium is also a popular choice for environments that require
- high levels of scalability and performance.



---
---

### Kubernetes Componets:
- https://kubernetes.io/docs/concepts/overview/components/

Control Plane Components:
 - etcd: stores the cluster state
 - API Server: exposes the Kubernetes API
 - Controller Manager: runs the control plane components
 - Scheduler: schedules pods onto nodes
 - Cloud Controller Manager: manages cloud resources  (e.g. AWS, GCP)
 - Cluster Autoscaler: scales the cluster
 - Horizontal Pod Autoscaler: scales pods
 - Node Controller: manages nodes
 - Taint/Toleration Controller: manages taints and tolerations
 - Service Controller: manages services
 - Volume Snapshot Controller: manages volume snapshots
 - Volume Controller: manages volumes
 - Volume Snapshot Datastore: stores volume snapshots
 - Volume Snapshot Store: stores volume snapshots
 - Volume Snapshot Store Manager: manages volume snapshots
 - Volume Snapshot Store Writer: writes volume snapshots
 - Volume Snapshot Store Reader: reads volume snapshots
 - Volume Snapshot Store Deleter: deletes volume snapshots
 - Volume Snapshot Store Updater: updates volume snapshots
 - Volume Snapshot Store Cleaner: cleans up volume snapshots
    
- Kubelet ( runs all the hosts.)
- kubeproxy ( runs on all the hosts.)

---
---


You apply manifest: (Where you write, how you want the stuffs to be) > API Server


Manifest file > API server > Scheduler > kubelet's job, in order to have the state of the requrement <--

Scheduler > decide, which of the worker nodes will be the best fit for the pod.


##### Now kubelet talks to:

kubelet > CRI > containerd > Docker > runc > containerd-shim > containerd-shim
kubelet > CNI > Cilium
kubelet > CSI > csi-snapshotter > csi-snapshotter
