## Questions:
How Iptables inspecting and filtering network traffic.


# Random notes:

- https://santoshk.dev/posts/2023/iptables-explained-an-introduction-to-linux-firewalling/
- iptables is a tool to manipulate network packets.
- Iptables is a powerful and versatile firewall tool that is used to protect and secure networks


#### Three constructs:

- Tables  (`5 types of tables`)
    - `Filter` Table:
        - This is the default tables. Meaning that if on command line if you don’t specify any table, program will assume filter table.
        - Role of this table is to filter packets based on criteria such as the source and destination IP addresses, port numbers, and protocols.
        - This table contains `three built-in chains`, that are used to process incoming, forwarded, and outgoing packets, respectively.
            - `Input` (built-in chains)
            - `Forward` (built-in chains)
            - `Output` (built-in chains)

    - `NAT` Table:
        - Role of this table is to modify destination or source headers in order to route packet in NAT setup where direct access is not possible.
        - NAT Table is used to translate IP addresses and/or port numbers in packets as they pass through the firewall.
        - This table contains `three built-in chains`, that are used to modify packets before and after routing.
            - `PREROUTING` (built-in chains)
            - `POSTROUTING` (built-in chains)
            - `OUTPUT` (built-in chains)

    - `Mangle` Table:
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

    - `Security` Table:
        - SELinux policy is applied on the packets.


- `Chains` (There are `5 chains` in iptables)
    - Chains are like points in route of a packet where you can apply rules.

    - Pre-routing Chain:
        - Pre-routing chain is applied to any incoming packet very soon after entring the network. This chain is processed before any routing descision have been made regarding where to send the packet. It is typically used to modify the destination IP address of incoming packets, such as when implementing port forwarding.


        


- Rules

