---
id: WS-C13-003
title: Enabling HTTPS
source_pages: "150-154"
chapter: 13
concepts: [digital-certificate, certificate-authority, certificate-signing-request, domain-verification, extended-validation, self-signed-certificate, lets-encrypt, nginx, https-redirect, hsts, tls-termination]
related: [WS-C13-002, WS-C13-004, WS-C13-005, WS-C05-005]
time_sensitive: true
---
# Enabling HTTPS
(Source: PDF pp. 150-154, tail PDF p. 155. The section begins at its heading part-way down PDF p. 150; the text above it is the end of WS-C13-002. The tail is the text at the top of PDF p. 155 above the "Attacking HTTP (and HTTPS)" heading, which begins WS-C13-004; it holds the redirect listing and the HSTS discussion.)

## What the section covers
The practical steps for serving a site over HTTPS: what a digital certificate is and why it is needed, how to obtain and install one, how a typical web server and application server pair is set up, redirecting HTTP traffic, and HTTP Strict Transport Security (PDF pp. 150-155).

## Why it matters
Securing traffic is much easier than understanding the algorithms behind it. Browsers are mostly self-updating and track modern TLS standards, and current web server software supports modern algorithms, so the developer's only remaining job is to get a digital certificate and install it on the web server (PDF p. 150).

## Meaning: digital certificates
- A digital certificate (also called a public-key certificate) is an electronic document proving ownership of a public encryption key. In TLS it associates keys with internet domains such as example.com (PDF p. 150).
- Certificates are issued by certificate authorities (CAs), trusted third parties that vouch that a particular key should be used to encrypt data sent to a domain. Browsers trust a few hundred CAs; the book names Comodo, DigiCert and, more recently, the nonprofit Let's Encrypt (PDF p. 150).
- When a trusted CA vouches for a key and domain, the browser knows it is talking to the right site with the right key, which blocks an attacker from presenting a malicious site or certificate (PDF p. 150).
- Why a third party? An asymmetric public key could be published by the server itself, but fetching it on the internet relies on the Domain Name System (DNS), which maps domain names to IP addresses. DNS can sometimes be spoofed to direct traffic to an attacker's IP address, and an attacker who spoofs a domain could supply their own key without victims noticing (PDF pp. 150-151).
- CAs prevent spoofed encrypted traffic. If an attacker diverts traffic to their own server, they lack the private key matching the real certificate, so they cannot decrypt intercepted traffic. If they present their own certificate, it will not have been verified by a trusted CA, and the browser shows a security warning that strongly discourages the user from continuing (PDF p. 151).
- You can view a site's certificate by clicking the padlock icon in the browser bar; the details are not very interesting, but browsers warn clearly when a certificate is invalid (PDF p. 151).

## How it works: obtaining a certificate
1. Generate a key pair, a small file containing randomly generated public and private keys (PDF p. 151).
2. Use the key pair to create a certificate signing request (CSR) containing the public key and the site's domain name, and upload it to a CA (PDF p. 151).
3. The CA requires you to prove you control the domain in the CSR before issuing the certificate (PDF p. 151).
4. After verification, download the certificate and install it on the web server together with the key pair (PDF p. 151).
The exact steps differ by CA (PDF p. 151).

### Generating the key pair and CSR
- Typically done with the openssl command line tool. A CSR can also contain applicant details such as legal organization name and location; these are put into the signed certificate but are not mandatory unless the CA chooses to validate them. The domain name is historically called the distinguished name (DN) or fully qualified domain name (FQDN) (PDF p. 151).
- Listing 13-1 shows the command (PDF p. 152):

```
openssl req -new -key ./private.key -out ./request.csr
```

The file private.key must already hold a newly generated private key (openssl can also generate that). The tool prompts for details to include in the request, including the domain name (PDF p. 152).

### Domain verification
- The CA checks that the applicant really controls the domain, because applying for a certificate amounts to claiming you need to decrypt traffic sent to it (PDF p. 152).
- This usually means temporarily editing the domain's DNS entries, which proves edit rights in the DNS. That requirement is what defends against DNS spoofing: an attacker cannot get a certificate without edit rights (PDF p. 152).

### Extended validation (EV) certificates
Some CAs issue EV certificates, for which the CA collects and verifies information about the applicant's legal entity. That information goes into the certificate and is visible to users in the browser. Large organizations like them because the company name often appears next to the padlock in the URL bar, encouraging trust (PDF p. 152).

### Expiring and revoking
- Certificates have a finite lifespan, typically months or years, after which the CA must reissue them. CAs also track certificates their holders voluntarily revoke (PDF p. 152).
- If the private key behind your certificate is compromised, apply for a new certificate and revoke the old one. Browsers warn users about expired or revoked certificates (PDF p. 152).

### Self-signed certificates
- In some environments, especially testing ones on an internal network, a CA cannot verify the domain or it is impractical to ask one. You may still want HTTPS there, so you generate your own certificate, a self-signed certificate, easily done with openssl (PDF pp. 152-153).
- Browsers usually show a strident warning ("This site's security certificate is not trusted!") but let the user accept the risk and continue. Make sure anyone using the test environment knows about this limitation and why the warning appears (PDF p. 153).

### Should you pay for certificates?
CAs were traditionally commercial and many still charge per certificate. Since 2015 the California nonprofit Let's Encrypt, founded by (among others) the Mozilla Foundation and the Electronic Frontier Foundation, has issued free certificates. Hence there is little reason to pay unless you need the extended validation offered by commercial CAs (PDF p. 153).

## Installing a certificate
Once you hold a certificate and key pair, the web server must switch to HTTPS and present the certificate during the TLS handshake. The process varies with hosting provider and server technology but is normally straightforward and well documented (PDF p. 153).

### Web servers vs. application servers
- A website is usually deployed as a pair of applications (PDF p. 153). The web server serves static content and does low-level TCP work, for example Nginx or Apache HTTP Server, written in C and optimized for this (PDF p. 153).
- The application server sits downstream of the web server and hosts the code and templates that produce dynamic content. Examples given: Tomcat or Jetty for Java, Puma or Unicorn for Ruby on Rails, and Django, Flask or Tornado for Python (PDF p. 153).
- Developers often casually call the application server "the web server". An application server can be deployed on its own, doing everything a web server does but less efficiently, which is a typical setup when coding and testing on a local machine (PDF p. 154).

### Configuring the web server for HTTPS
- Certificates and keys are almost always deployed on the web server, which is much faster than the application server (PDF p. 154).
- Switching to HTTPS means configuring the web server to accept traffic on the standard HTTPS port 443 and telling it where the certificate and key pair are (PDF p. 154).
- Listing 13-2, an Nginx server block, listens on 443 with SSL, names the server (www.example.com), points to the certificate file and key file, restricts protocols to TLS 1.2 and 1.3, and sets the cipher string HIGH:!aNULL:!MD5, which the book does not explain (PDF p. 154). SUPPLEMENTARY: in OpenSSL cipher-string notation this selects "high" strength suites and excludes anonymous (aNULL) and MD5-based ones. The listing:

```
server {
    listen              443 ssl;
    server_name         www.example.com;
    ssl_certificate     www.example.com.crt;
    ssl_certificate_key www.example.com.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;
}
```

- A web server that handles TLS decrypts incoming HTTPS requests and passes those needing the application server downstream as unencrypted HTTP. This is terminating HTTPS at the web server. The hop between web and application server is unencrypted, which is usually not a risk because the traffic stays on one machine or at most a private network (PDF p. 154).

### What about HTTP?
- You must also decide how to treat unencrypted traffic on the standard HTTP port 80. The usual choice is to redirect insecure requests to the matching secure URL: a visit to the http version of a page gets an HTTP 301 response pointing to the https version, and the browser repeats the request on port 443 after a TLS handshake (PDF p. 154).
- Listing 13-3 is an Nginx server block that listens on port 80 as the default server, matches any server name, and returns a 301 to the https scheme with the original host and request URI (PDF p. 155):

```
server {
    listen 80 default_server;
    server_name _;
    return 301 https://$host$request_uri;
}
```

### HTTP Strict Transport Security
- Remaining loophole: sensitive data must not be sent during any initial connection over HTTP (PDF p. 155).
- A browser that has visited a site before sends the cookies the site previously supplied in the Cookie header. If the first connection is over HTTP, those cookies travel insecurely even if later requests are upgraded to HTTPS (PDF p. 155).
- The fix is an HTTP Strict Transport Security (HSTS) policy, set by returning the Strict-Transport-Security header. A modern browser that sees it remembers to use only HTTPS for the site, even if the user types an http address, switching without prompting. This protects cookies from being stolen on the initial connection (PDF p. 155).
- Listing 13-4 adds the header in Nginx, inside a server block, with a max-age of 31536000 seconds (PDF p. 155):

```
add_header Strict-Transport-Security "max-age=31536000" always;
```

- The browser follows the policy for the number of seconds in max-age, after which it checks again whether the site changed its policy (PDF p. 155).

## When and how to apply
INTERPRETATION: a workable order of work is to get a certificate (or a self-signed one for internal tests), install it on the web server, listen on 443, redirect port 80 to 443, then add HSTS. The book's HSTS description concerns cookies in the first connection; a short max-age is sensible while testing, because the browser keeps enforcing the policy for that period.

## Time-sensitive statements
- Browser-trusted CAs named (Comodo, DigiCert, Let's Encrypt) and Let's Encrypt's free certificates since 2015.
- The Nginx TLS protocol and cipher settings (TLS 1.2 and 1.3) reflect the book's recommended configuration at its time of writing.

## Relations
Builds on WS-C13-002. The reasons to do all this are shown in WS-C13-004. Release processes for deploying configuration are in Chapter 5 (WS-C05-005).
