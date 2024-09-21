## Questions:
How Iptables inspecting and filtering network traffic.


# Random notes:

- https://santoshk.dev/posts/2023/iptables-explained-an-introduction-to-linux-firewalling/
- iptables is a tool to manipulate network packets.
- Iptables is a powerful and versatile firewall tool that is used to protect and secure networks

<br>

---
---

Links: https://www.youtube.com/watch?v=6Ra17Qpj68c


<br>

---
---

<br>

## IMP:

Traffic first fall into chain of different tables supporting that chain,and then Rules in that tables related to that chain.

- (`for input to the system`):
    - raw table's PREROUTING chain > mangle table's PREROUTING chain > nat table's PREROUTING chain.
    - mangle table's INPUT chain > filter table's INPUT chain.
    - raw table's OUTPUT chain > mangle table's OUTPUT chain > nat table's OUTPUT chain > filter table's  OUTPUT chain.
    - mangle table's POSTROUTING chain > nat table's POSTROUTING chain.

- (`for forwarding packets`):
    - raw table's PREROUTING chain > mangle table's PREROUTING chain > nat table's PREROUTING chain.
    - mangle table's FORWARD chain > filter table's FORWARD chain.
    - mangle table's POSTROUTING chain > nat table's POSTROUTING chain.
<br>


<br>

---
---

<br>


![iptables-fig1](./images/iptables-fig001.png)


<br>


| Table Name | Description | Built-in Chains |
| --- | --- | --- |
| Filter | Default table, used to filter packets based on criteria such as source and destination IP addresses, port numbers, and protocols. | INPUT, FORWARD, OUTPUT |
| NAT | Used to route packets to different hosts on NAT networks by changing the source and destination addresses of packets. | PREROUTING, POSTROUTING, OUTPUT |
| Mangle | Used to alter packet headers in various ways, such as changing TTL values. | PREROUTING, OUTPUT, INPUT, FORWARD, POSTROUTING |
| Raw | Used for connection tracking, allows you to work with packets before the kernel starts tracking its state. | PREROUTING, OUTPUT |
| Security | SELinux policy is applied on the packets. | - |    

<br>


<br>

---
---

<br>



### Chains:

<br>

![iptables-fig2](./images/iptables-fig002.png)

<br>

<b> We organize chains through the tables, but: </b> 

Logically: the traffic flow through `chains` of different `tables` as follows: (`for input to the system`):
- **PREROUTING** (chain) - `Rules in this chain apply to packets as they just arrive on the network interface.`
    - raw table
    - mangle table
    - nat table

- **INPUT** (chain) - `Rules in this chain apply to packets just before they’re given to a local process.`
    - mangle table
    -  filter table

- **OUTPUT** (chain) - `The rules here apply to packets just after they’ve been produced by a process.`
    - raw table
    - mangle table
    - nat table
    - filter table

- **POSTROUTING** (chain) - `The rules in this chain apply to packets as they just leave the network interface`
    - mangle table
    - nat table


<br>

#### for PREROUTING related rules from different tables.

```
sudo iptables -t raw -n -L PREROUTING
sudo iptables -t mangle -n -L PREROUTING
sudo iptables -t nat -n -L PREROUTING   
```

<br>


### Path 1  (for input to the system)

| Chain Name | Description | Table |
| --- | --- | --- |
| PREROUTING | Modify packets before routing. | Raw, Mangle, NAT |
| INPUT | Filter incoming network traffic. | mangle, Filter |
| OUTPUT | Modify locally generated packets. | Raw, Mangle, NAT |
| OUTPUT | Filter outgoing network traffic. | Filter |
| POSTROUTING | Modify packets after routing. |Mangle,  NAT |

<br>


So, logically: the traffic flow through `chains` of different  `tables` is as follows: (for forwarding packets)
- **PREROUTING** (chain)
    - raw table
    - mangle table
    - nat table

- **FORWARD** (chain) - `The rules here apply to any packets that are routed through the current host.`
    - mangle table
    - filter table

- **POSTROUTING** (chain)
    - mangle table
    -  nat table
    

### Path 2 (for forwarding packets)

| Chain Name | Description | Table |
| --- | --- | --- |
| PREROUTING | Modify packets before routing. | Raw, Mangle, NAT |
| FORWARD | Filter network traffic that is being forwarded by the firewall. | mangle, Filter |
| POSTROUTING | Modify packets after routing. | Mangle, NAT |



<br>

---
---

<br>





The Linux kernel comes with a packet filtering framework named `netfilter`.  `netfilter` is a set of hooks inside the Linux kernel that allows you to filter network packets. `iptables` is a user-space program that uses the `netfilter` framework to filter network.   `iptables` is a command-line tool that allows you to configure the `netfilter` framework. `iptables` is used to filter network traffic based on various criteria such as source and destination IP. `iptables` is also used to configure network address translation (NAT) and other network-related. 


The packet filtering mechanism provided by iptables is organized into `three different` kinds of structures: `tables`, `chains` and `targets`. The default table is the `filter` table.  The `filter` table is used to filter network traffic. The `filter` table is divided into  `three` different chains: `INPUT`, `OUTPUT` and `FORWARD`. The `INPUT.

`chain` is used to filter incoming network traffic:
The `INPUT` chain is used to filter network traffic that is coming into the firewall.
The `OUTPUT` chain is used to filter outgoing network traffic. 
The `FORWARD` chain is used to filter network traffic that is being forwarded by the firewall.  

<br>

---
---

<br>


### We have 5 tabels and 3 main constructs:

- Tables  (`5 types of tables`)
    - `Filter` Table:
        - This is the default and perhaps the most widely used table. It is used to make decisions about whether a packet should be allowed to reach its destination.
        - This is the default tables. Meaning that if on command line if you don’t specify any table, program will assume filter table.
        - Role of this table is to filter packets based on criteria such as the source and destination IP addresses, port numbers, and protocols.
        - This table contains `three built-in chains`, that are used to process incoming, forwarded, and outgoing packets, respectively.
            - `Input` (built-in chains)
            - `Forward` (built-in chains)
            - `Output` (built-in chains)

            ```
            # iptables -t filter -n -L
            # sudo iptables -t filter --list
            ```


    - `NAT` Table:
        - This table allows you to route packets to different hosts on NAT (Network Address Translation) networks by changing the source and destination addresses of packets. It is often used to allow access to services that can’t be accessed directly, because they’re on a NAT network.
        - Role of this table is to modify destination or source headers in order to route packet in NAT setup where direct access is not possible.
        - NAT Table is used to translate IP addresses and/or port numbers in packets as they pass through the firewall.
        - This table contains `three built-in chains`, that are used to modify packets before and after routing.
            - `PREROUTING` (built-in chains)
            - `POSTROUTING` (built-in chains)
            - `OUTPUT` (built-in chains)
            ```
            sudo iptables -t filter --list
            ```

    - `Mangle` Table:
        - This table allows you to alter packet headers in various ways, such as changing TTL values.
        - The Mangle Table is used to modify packets in ways that are more complex than those allowed by the Filter and NAT Tables.
        - This table can be used to alter packet header information, mark packets for special handling, and perform other advanced packet processing tasks.
        - The Mangle Table contains `five built-in chains, that allow packets to be processed at various stages of their journey through the firewall.
            - `PREROUTING` (built-in chains)
            - `OUTPUT` (built-in chains)
            - `INPUT` (built-in chains)
            - `FORWARD` (built-in chains)
            - `POSTROUTING` (built-in chains)

    - `Raw` Table:
        - Used for connection tracking.
        - iptables is a stateful firewall, which means that packets are inspected with respect to their “state”. (For example, a packet could be part of a new connection, or it could be part of an existing connection.) The raw table allows you to work with packets before the kernel starts tracking its state. In addition, you can also exempt certain packets from the state-tracking machinery.

    - `Security` Table:
        - SELinux policy is applied on the packets.



<br>

---
---

<br>




- `Chains` (There are `5 chains` in iptables)
    - Chains are like points in route of a packet where you can apply rules.

    - Pre-routing Chain:
        - Pre-routing chain is applied to any incoming packet very soon after entring the network. This chain is processed before any routing descision have been made regarding where to send the packet. It is typically used to modify the destination IP address of incoming packets, such as when implementing port forwarding.


        


- Rules

