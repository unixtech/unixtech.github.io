title: Central SSH Key management using CA
Date: 2014-12-15 13:02
Category: Server    
Tags: Security, SSH 
Slug: Central-SSH-key-management-CA-1
Status: draft
Authors: Unixer
Summary: Part 1 of Managing OpenSSH keys on large scale Securely.


{% img center /images/openssh.gif 600px 400px "Ping1" %}

## Intro 
It's always challenge in itself to handle SSH private keys, Managing authentication ( Without-password ) and keeping it upto date. Things like taking control of the keys plus revoking the keys as needed is formidable challenge for any senior admin.  
One can do it via traditional `authorized_keys` file but overtime it becomes messy to maintain and more prone to errors. This becomes all the more important when you can't handle key management to you users whom you deem undesirable to be able to comprehend . 

Menta ike 

So, Decided to move to CA based authentication with OpenSSH with OpenLDAP. In this part we will cover just CA based key management later parts we will do it with OpenLDAP integration and how does one maintain the whole ssh keys management via ansible.  

It doesn't really matter which methods you adopt as long as you have prior policy to deal with regular management of keys.  

## Lab Topology 
{% img center /images/sshca_topology1.png 600px 400px "SSHCA_Topology" %}
<span  {align= center;}  >** *Fig1*- Strong SSH manta:** Scopus SSH lie manteld. Mentali menta so. </span>

> CA server will only be used to generate CA key and Sign and generate certificates for public keys that you have received from various users.  

> Remember: At no point in time private key of user is supposed to leave his/her computer, Only public keys are required to generate certs. 


## Configure Host certificates 
Utility: `ssh-keygen`

We will start by configurign our host certificates. Host certificates replaces public keyfiles of users's know_host files.  It will replace it with CA's public key in users known_host file.  
To avoid confusion here are the files required on various machines for Host certificates.  

| Machine  | Files                                 | Purpose                                                                                                                              |
| -------- | :-----:                               |                                                                                                                                      |
| CA       | CA Private KEY ( server_ca ) - Hosted | For signing certificate that will certify the host's authenticity                                                                    |
|          | CA Public KEY (server_ca.pub)         | This will go to every host that we want to trust this CA                                                                             |
|          |                                       |                                                                                                                                      |
| Client   | known_hosts                           | Only file that changes on client, Here the file `server_ca.pub` will come as `@cert-authority`.                                      |
|          |                                       |                                                                                                                                      |
| Server   | sshd_config                           | Server's sshd_config file will be changed with appropriate configuration for that server to 'trust' that particular <b>authority</b> |


---

  
> Note: Don't confuse `Server` and `Client` here, they interchangeable terms, Mostly depends upon where you need authentication done. 

### Generate CA keys 
```bash
 #Generate CA for our infrastructure.
 ssh-keygen -f server_ca
```
Now You should have two files in your CWD.
```bash
 #!sh
 ls
 server_ca  server_ca.pub
```

### Signing Host keys 
Now that we have our CA keys, We can sign our host keys. 

#### Example: 
Start by signing any example key for trial:
```bash
 ssh-keygen -s server_ca.pub -I "Identifier" -h -n "HOST_NAME" -V +52w host_rsa_key
```

Let's have look at what each of these options means:

| -s | Private key of CA that we just created server_ca                                                               |
| -I | This is identifier, This name will show up in logs when this certificate is used for authentication. It can be name of host |
| -h | Generate certificate for host as oppose to client                                                                           |



