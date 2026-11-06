---
id: WS-C02-003
title: Application Layer Protocols
source_pages: "37-40"
chapter: 2
concepts: [application-layer, http, http-request, http-response, get-vs-post, http-methods, trace-method, status-codes, headers, csrf, content-type, cache-control]
related: [WS-C02-002, WS-C02-004, WS-C08-001]
time_sensitive: true
---
# Application Layer Protocols
(Source: PDF pp. 37-40, tail PDF p. 41. The section starts part-way down PDF p. 37 at its heading. On PDF p. 41 only the text above the heading "Stateful Connections" belongs here.)

## What the section covers
How higher-level protocols sit on TCP, then a detailed look at HTTP: the four parts of a request, the main and lesser-known methods, and the structure of a response with its status codes and headers.

## Meaning: application layer protocols
- TCP lets two machines exchange data reliably but does not say how that data should be interpreted. Both sides must agree on a higher-level protocol. Protocols built on TCP (or UDP) are called application layer protocols (PDF p. 37).
- Lower-level protocols provide basic routing; application layer ones add structure for programs exchanging data. Figure 2-1 shows the suite as four layers. Application layer: DNS, FTP, HTTP, IMAP, POP, SMTP, SSH, XMPP. Transport layer: TCP and UDP. Internet layer: IPv4 and IPv6. Network layer: ARP, MAC, NDP, OSPF, PPP (PDF pp. 37-38).
- Examples: SMTP sends email, XMPP is often used for instant messaging, FTP makes files downloadable, and HTTP serves the web. HTTP is the focus (PDF p. 38).

## HTTP basics
- Web servers use HTTP to deliver pages and their resources to user agents such as browsers. The agent sends requests for resources; the server replies with the resource or an error code. Both are plaintext messages, though often compressed and encrypted in transit. The author says every exploit in the book uses HTTP somehow, so the details matter (PDF p. 38).

## HTTP requests
A request from a browser has four elements (PDF p. 38):
- Method (also called the verb): the action the agent wants performed.
- URL: the resource to fetch or manipulate.
- Headers: metadata such as the content type expected or whether compression is accepted.
- Body: optional extra data for the server.

Listing 2-1 is a simple request for the home page of example.com. The first line carries the method GET and the URL. Header lines follow: User-Agent (identifies the browser type, here a Chrome string on a Mac), Accept (content types expected), Accept-Encoding (gzip, deflate) and Accept-Language (English variants with quality weights) (PDF pp. 38-39).

## Methods
- GET: the most common request on the internet. It fetches a resource identified by a URL, such as a page, an image or search results. Listing 2-1 is what a browser generates when a user types example.com in the address bar (PDF p. 39).
- POST: used when the browser must send information to the server, for example when a form is submitted. The data goes in a request body after the headers (PDF p. 39).
- Security point: Chapter 8 explains why POST, not GET, should be used to send data. Sites that use GET for anything other than retrieving resources are open to cross-site request forgery (PDF p. 39).
- PUT, PATCH and DELETE upload, edit and delete resources respectively. They are typically triggered by JavaScript in a page (PDF p. 39).
- Table 2-1, lesser-known methods (PDF p. 39):
  - HEAD: same information as GET but the server omits the body. If you implement GET, the server usually answers HEAD automatically.
  - CONNECT: starts two-way communication; used in HTTP client code when you must go through a proxy.
  - OPTIONS: lets a user agent ask which other methods a resource supports; servers generally infer the answer from the methods you implemented.
  - TRACE: the response echoes the original request exactly, so the client can see changes made by intermediaries. It is generally recommended to disable TRACE, because it can be a security hole; for example, injected malicious JavaScript could use it to reach cookies deliberately made inaccessible to JavaScript.

## HTTP responses
- A response opens with a protocol description, a three-digit status code and usually a status message saying whether the request can be met. Headers give metadata telling the browser how to treat the content. Most responses also have a body containing the resource (PDF p. 40).
- Listing 2-2 is the response from example.com. Its status line reads HTTP/1.1 200 OK. Headers include Content-Encoding gzip, Accept-Ranges bytes, Cache-Control max-age=604800, Content-Type text/html and Content-Length 606. The body is a small HTML document: a head with a title ("Example Domain") and an embedded style block, and a body with a heading and two paragraphs, the second holding a link to more information (PDF p. 40).
- Status code families (PDF pp. 40-41):
  - 2xx: request understood, accepted and answered.
  - 3xx: redirect the client to a different URL.
  - 4xx: client error, an apparently invalid request; the most common is 404 Not Found.
  - 5xx: server error; the request was valid but the server could not fulfil it.
- Headers: almost every response includes Content-Type to say what kind of data is returned. Responses to GET often include Cache-Control, telling the client to cache large resources such as images locally (PDF p. 41).
- Body: for a successful response it holds the requested resource, often HTML describing the page structure, with styling and content in the listing's example. Other responses may return JavaScript, CSS or binary data (PDF p. 41).

## Relations
Builds on the TCP and DNS material in WS-C02-002; the next section, WS-C02-004, covers how HTTP is made stateful with cookies. The GET versus POST point is developed in the book's chapter on cross-site request forgery.

## Time-sensitive statements
The sample User-Agent string in Listing 2-1 names specific browser and OS versions (Chrome, Mac OS X) from the book's era; HTTP/1.1 is used in the response example.
