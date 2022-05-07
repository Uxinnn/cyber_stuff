# Networking

## OSI Model

|Layer|Name|Examples|
|---|---|---|
|1|Physical|Data cables|
|2|Data Link|MAC Addresses|
|3|Network|Routing|
|4|Transport|
|5|Session|
|6|Presentation|WMV, JPEG, MOV|
|7|Application|HTTP, SMTP|

* Please Do Not Throw Sausage Pizza Away.
* When data is received --> Go down the OSI model.
* When data is transmitted --> Go up the OSI model.

## IP Addresses

* Layer 3 protocol.
* IPv4:
  * 32 bits, 8 bytes
  * 2<sup>32</sup> possible IP addresses.
* IPv6:
  * 128 bits
  * 2<sup>128</sup> possible IP addresses.

### IP Address Classes:

|Class|Private Network|Subnet Mask|Address Range|Number of Networks|Number of Hosts per Network|
|---|---|---|---|---|---|
|A|10.0.0.0|255.0.0.0|10.0.0.0 - 10.255.255.255|126|16,646,144|
|B|172.16.0.0.0 - 172.31.0.0|255.240.0.0|172.16.0.0 - 172.31.255.255|16,383|65,024|
|C|192.168.0.0|255.255.0.0|192.168.0.0 - 192.168.255.255|2,097,151|254|

## Media Access Control (MAC) Address

* Layer 2 protocol.
* Under *ether* in `ifconfig`.
* First 3 bytes are Organization Unique Identifiers (OUIs).
  * Can google to identify which manufacturer the OUI belongs to.

## Common Ports and Protocols

|Transport Layer Protocol|Application Layer Protocol|Port|
|---|---|---|
|TCP|FTP|21|
|TCP|SSH|22|
|TCP|Telnet|23|
|TCP|SMTP|25|
|TCP|DNS|53|
|TCP|HTTP|80|
|TCP|HTTPS|443|
|TCP|POP3|110|
|TCP|SMB|139, 445|
|TCP|IMAP|143|
|UDP|DNS|53|
|UDP|DHCP|67, 68|
|UDP|TFTP|69|
|UDP|SNMP|161|

## Subnetting

* Networking IP: First address in subnet.
* Broadcast IP: Last address in subnet.
* If CIDR block increases, then number of hosts decreases. Vice versa.
* *Number of possible hosts = Number of IP addresses - 2*