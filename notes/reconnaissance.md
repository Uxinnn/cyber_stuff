# Reconnaissance

## Discovering Email Addresses

* [Hunter.io](https://hunter.io)
  * Shows the most common pattern of a company email address.
* [Phonebook.cz](https://phonebook.cz/)
* [Voila Norbert](https://www.voilanorbert.com/)
* [Clearbit Connect](https://connect.clearbit.com/)
* [Email Hippo](https://tools.emailhippo.com/)
  * Use to verify email addresses found from the above websites.
* [Email-Checker.net](https://email-checker.net/)

## Gathering Breached Credentials

* [Breach Parse](https://github.com/hmaverickadams/breach-parse)
  * Very big program (~44GB).
  * FInd list of credentials from past data breaches.
  * Try to find repeat offenders (people who have been breached more than once). Usually they will have similar passwords, so you can try to guess their current password.

## Hunting Subdomains

* Sublist3r
  * `apt-get install sublist3r`
  * `sublist3r -d <domain name>`
  * Use `-t` to specify number of threads to use to speed up search.
* [Crt.sh](https://crt.sh/)
  * Certificate fingerprinting.
* [Owasp Amass](https://github.com/OWASP/Amass)
  * Takes a long time to run, but results are good.
* [Tomnomnom Httprobe](https://github.com/tomnomnom/httprobe)
  * Checks if list of websites given is alive.

## Hunting Website Technologies

* [BuiltWith](https://builtwith.com/)
  * Looks up what type of technology is used by a website.
  * Can find frameworks websites are running on.
* [Wappalyzer](https://www.wappalyzer.com/)
  * More of an active type of reconnaissance.
* [WhatWeb](https://tools.kali.org/web-applications/whatweb)
  * Built into Kali Linux.

## Others

* Google Fu
  * [Search operators](https://ahrefs.com/blog/google-advanced-search-operators/)
* Social Media (Twitter, Linkedin, etc.)
  * To bypass Linkedin's login requirement:
    1. Copy linkedin profile url to [Google mobile friendly test](https://search.google.com/test/mobile-friendly).
	2. Copy the output html code and render it to view page.