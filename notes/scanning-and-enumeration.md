# Scanning and Enumeration

## Scanning with Nmap

* Start off with `nmap -T4 -p- -A <target ip>`
* Some useful options:
  * Stealth scan [`-sS`]:
    * Default.
    * Easily detectable.
    * How it works:
	  * Packets exchanged are *SYN SYNACK RST*. (Normally it is *SYN SYNACK ACK*).
  * UDP scan [`-sU`]:
    * Takes very long to scan.
    * Typically just scan the top 1000 ports.
  * Speed of scan [`-T<x>`]:
    * Range from 1 to 5. 1 is very slow, 5 is very fast.
  * Ports to scan [`-p`]:
    * `-p-` to scan all ports.
    * If not specified, nmap scans the top 1000 ports.
  * Tell me everything [`-A`]:
    * Does OS detection, version detection, script scanning, traceroute.

## Enumerating HTTP/HTTPS

* Ports with common exploits:
  * 80 (HTTP)
  * 443 (HTTPS)
  * 139 (SMB)
* Ports with not many exploits:
  * 22 (SSH)
* Steps
  1. If port 80/443 are open, use browser to go to website (type in IP).
    * If a default page is shown, it does reveal some information.
  2. View source code of website to find any useful information.
  3. Nikto: `nikto -h http(s)://<target-ip>`
  4. Dirbuster
    * Start with a small wordlist, then use medium if no results are found.
	* Can put extra file extensions (txt, pdf, etc.) to find these files, but takes longer.
  5. Burp Suite
    * Just to take a peek.
    * Send to repeater to show response in real time. Can modify requests too.
	* Add scope to limit search to in scope items.
	* Server headers will have information.

### Other tools

* Dirb: `dirb http(s)://<target ip>`
  * Use to brute force directories.
* Ffuf: `ffuf -w <wordlist>:FUZZ -u http(s)://<target ip>/FUZZ`
  * Use wordlist to fuzz a parameter.

## Enumerating SMB

* Smbclient: `smbclient -l \\\\<target ip>\\`
  * Try to connect to file share.

## Enumerating SSH

* Just try to connect, sometimes banner may be exposed and show some info.

## Researching Potential Vulnerabilities

* If [cvedetails.com](https://www.cvedetails.com/), can go to website to check vulnerability score. If it's red, then it probably can be attacked.
* If rapid7 page comes up, it's good since it means that metasploit can be used.
* Use *searchsploit* if internet access is not available.
  * Cannot be too specific in keywords use as it searches the exact string.
  * Path shown in results will show what kind of exploit it is.

## Hashes

* Hash Identifier
  * Use to identify hashes.
* Hashcat: `hashcat -m 0 <hashes in a file> <wordlist>`
  * Use to crack hashes.

## Others

* Netdiscover
  * Use to scan a subnet.
  * `netdiscover -r <subnet ip>/<cidr>`