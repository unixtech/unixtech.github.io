Title: PF Firewall-1
Date: 2014-12-04 13:02
Modified: 2014-12-06 13:30
Category: Unix    
Tags: Unix, Monitor
Slug: pf-firewall-1 
Authors: Unixer
Summary: Securing your environment via `PF`

## FreeBSD and OpenBSD 
PF (Packet filter) is default firewall for OpenBSD and included in other OS's like [FreeBSD](http://www.freebsd.org) and [Apple](http://www.apple.com "Apple") IOS operating systems. Many other "Commercial firewall" appliances are inspired by PF.

##History of PF

PF was originally designed as replacement for Darren Reed's IPFilter, from which it derives much of its rule syntax. IPFilter was removed from OpenBSD's CVS tree due to OpenBSD developers' problems with its license. Specifically, Reed distributed some versions of his software with the license clause, "Derivative or modified works are not permitted without the author's prior consent." Due to this, the OpenBSD team decided to replace the software. This decision became the subject of wrangling among the parties involved, degenerating into a discussion that failed to reach mutual understanding. On the subject, OpenBSD project leader Theo de Raadt wrote, "Software which OpenBSD uses and redistributes must be free to all... for any purpose including... modification."

PF has since evolved quickly and now has several advantages over other available firewalls. Network Address Translation (NAT) and Quality of Service (QoS) have been integrated into PF, QoS by importing the ALTQ queuing software and linking it with PF's configuration. Features such as pfsync and CARP for failover and redundancy, authpf for session authentication, and ftp-proxy to ease firewalling the difficult FTP protocol, have also extended PF.

One of the many innovative feature is PF's logging. Logging is configurable per rule within the pf.conf and logs are provided from PF by a pseudo-network interface called pflog. Logs may be monitored using standard utilities such as tcpdump, which in OpenBSD has been extended especially for the purpose, or saved to disk in a modified tcpdump/pcap binary format using the pflogd daemon.

> For more info, **Read  - [History of pf](http://en.wikipedia.org/wiki/PF_%28firewall%29)**

## PF setup
Usually `PF` is deployed  in conjuction with other tools provided by OpenBSD ecosystem.
These includes:
* HFSC Queuing system for QoS
* FTP-Proxy
* Application proxies such as Relayd ( Mainly used as HTTPs termination point )
* OS detection using fingerprint - `pf.os`
* CARP firewall failover for HA environments ( UCARP for FreeBSD users )

### How to deploy PF firewall in your environment

> Note: Both OpenBSD and FreeBSD OS uses different syntax for maintaining `PF` firewall.
> We will mainly focus on OpenBSD OS but there are benefits of using `PF` with FreeBSD OS since it provides multi-processing capable version of `PF`.

<!--{% include_code pf.conf [lang:sh] [pf.conf] %}-->

File - `/etc/rc.conf.local`

    :::bash
    pf=YES
    pf_rules=/etc/pf.conf
    pflogd_flags="-s 1500" # Ex. Snaplen, Log filename 

File - `/etc/pf.conf`

    :::bash
    ### My master pf.conf

    ### Interfaces
    EXTIF ="em0"
    INTIF ="em1"
    DMZ = "em2"
    EXTRAIF ="em3"

    ### Hosts
	ADMIN ="10.0.11.1"
    ADMIN1 ="10.0.11.31"
    BOTHADMIN ="{" $ADMIN $ADMIN1 "}"
    EXTDNSSERVER ="4.2.2.2"
    INTDNSSERVER ="$INTIF:0"
    #DNSSERVERS ="{" $INTDNSSERVER $EXTDNSSERVER "}"
    DNSSERVER ="{$INTDNSSERVER}"
    LOGSERVER = "{ 10.0.11.22, 10.0.11.31  }"

* All these variable defined are called MACROS inside `pf.conf` file.
* These are used for convinience and ease of use
* Defining nested macros are possible as well.
* Take a look at `INTIF` macro, If you want to include that whole internal network in your rules then `INTIF:network` in your rule.

Now, We will have a look at some of the rules itself.

    :::bash
    #External Interface
    #Block all on External interface
    block log on $EXTIF

    ## Network address translation with outgoing source 
    #match out log on $EXTIF from $INTIF to any received-on $INTIF tag EGRESS nat-to ($EXTIF:0) 
    match out log on $EXTIF from $INTIF:network to any received-on $INTIF tag EGRESS nat-to ($EXTIF:0)
    #If you have difficulties with any box with static port forwarding then you should use
    #match out log on $EXTIF from $INTIF to any received-on $INTIF tag EGRESS nat-to ($EXTIF:0) static-port

    #Traffic generated from firewall it self will be tagged as EGRESS
    match out log on $EXTIF from $EXTIF to any tag EGRESS
    #More on these later on.

    #EXTIF inbound
    pass in log (to pflog1) on $EXTIF inet proto tcp from any to any port 22 
    pass in on $EXTIF inet proto tcp from any to $EXTIF port >10000

    #External interface outbound
    pass out log on $EXTIF inet  from ($EXTIF) to any $TCPSTATE $EXTIFSTO queue (bulk, ack) tagged EGRESS
    #pass out log on $EXTIF inet proto udp from ($EXTIF) to any $UDPSTATE $EXTIFSTO queue (bulk, ack) tagged EGRESS
    pass out log on $EXTIF inet proto tcp from ($EXTIF) to any port $TCPPORTS $TCPSTATE $EXTIFSTO queue (web, ack) tagged EGRESS
    pass out log on $EXTIF inet proto udp from ($EXTIF) to any port 53 $UDPSTATE $EXTIFSTO queue (dns, ack) tagged EGRESS

* These are some of the rules that I have defined in my DMZ firewall to prevent other users from coming in from outside.
* After deploying this ruleset only SSH is allowed from outside interface of firewall. 
* From inside essential end-user services such as Internet browsing, DNS are enabled. 
* Take a look at `match out` rules on `EXTIF` to have a look at how nat rules are working. 

### Turning on routing
To turn on routing functionality of the box, You need to make sure you have enabled ip forwarding in `sysctl`

    :::bash
    # To check the ip forwarding status
    sysctl net.inet.ip.forwarding
    # If it's 0 then turn it on
    sysctl net.inet.ip.forwarding=1

    #To make it permanent 
    ### /etc/sysctl.conf
    net.inet.ip.forwarding = 1

### PFCTL utility
After making changes inside `pf.conf` file, rules are not automatically loaded. To load the rules We need to use `pfctl`

To load rules - Assuming rule file is `/etc/pf.conf`

    :::bash
    pfctl -vf /etc/pf.conf

To see which rules are currently loaded, It will also show related counters. 

    :::bash
    pfctl -vsr 

{% img center /images/pf_rules.png 600px 400px "pf.conf" %}


## Conclusions
PF is one of the most popular and powerful firewall for managing your network traffic. We have barely even scratched surface of what PF can provide. It's functionality is much more then many of the commercial offerings offers.  
We will also cover some extended functionality such as usage of Anchors, Preventing torrent traffic, Blacklisting and preventing brute-forcing attack etc.
Being open-source it places no restrictions on usage. Users can use it any which way they would prefer.  

Having been used PF and OpenBSD for nearly 10 years in all of my setups I can say PF is most secure firewall there is and With combination of OpenBSD and PF you can be pretty sure you are one step ahead then rest  in process of being NSA proof.


