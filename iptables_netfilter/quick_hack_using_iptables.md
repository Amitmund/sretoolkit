## To duplicate the http request to another host too, but not to respond back from the duplicate host

Sending traffic to to destination host of 10.0.0.100 and port 8080
> iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.100:8080

On the Destination Host:
(You might like to logs for further analysis)
> iptables -A OUTPUT -d 10.0.0.100 -p tcp --sport 8080 -j DROP

---

## Few key links

- https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/

> iptables -A INPUT -m bpf --object-pinned /sys/fs/bpf/match -j DROP


- https://www.digitalocean.com/community/tutorials/a-deep-dive-into-iptables-and-netfilter-architecture


- https://www.digitalocean.com/community/tutorials