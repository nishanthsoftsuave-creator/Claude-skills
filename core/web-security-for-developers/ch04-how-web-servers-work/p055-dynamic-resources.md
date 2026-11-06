---
id: WS-C04-004
title: Dynamic Resources
source_pages: "55-61"
chapter: 4
concepts: [dynamic-resource, templates, sql-database, nosql-database, distributed-cache, microservices, web-programming-languages, client-side-javascript, angular, react, dom-based-xss]
related: [WS-C04-002, WS-C04-003, WS-C04-005, WS-C03-003, WS-C06-002, WS-C07-004, WS-C08-001, WS-C14-002]
time_sensitive: true
---
# Dynamic Resources
(Source: PDF pp. 55-61, tail PDF p. 62. The Figure 4-2 image and caption at the top of PDF p. 55 belong to WS-C04-003. The tail page text above the "Summary" heading belongs here; the Summary is WS-C04-005.)

## What the section covers
Why most modern sites use dynamic resources, how templates work, the databases and caches those resources draw on, the main server-side programming languages and their security profiles, and client-side JavaScript frameworks (PDF pp. 55-62).

## Meaning and why it matters
- Hand-writing an HTML file for every page is slow. Picture a shop coding a new page for each inventory item. So most modern sites use dynamic resources, whose code often loads data from a database to fill the HTTP response. The output is usually HTML, though other content types can be returned to match what the browser expects (PDF p. 55).
- A retail site can have one product page that displays any product: it takes the product code from the URL, loads price, image and description from the database, and interpolates them into HTML. Adding a product then only means adding database rows (PDF p. 55).
- Other uses: a bank site looks up and shows your account details; a search engine builds a results page from its index; social media and webmail sites look different for each user because the HTML is built after login (PDF p. 55).
- The price is new vulnerabilities. Interpolating content into HTML can be attacked. Malicious injected JavaScript is handled in Chapter 7 and harmful cross-site requests in Chapter 8 (PDF p. 56). See WS-C07-004 and WS-C08-001.

## Templates
- The first dynamic resources were simple scripts, often in Perl, that the server ran and that wrote out the page HTML (PDF p. 56).
- Such code is hard to read: one language writes content in another that the browser later renders, and a static file shows its structure at a glance whereas a thousand lines of Perl do not. Changing the code while picturing the final output is difficult (PDF p. 56).
- Template files fix this. They are mostly HTML with simple logic embedded that instructs the server to do one of three things: fetch data from a database or the HTTP request and insert it, render a section only under a condition, or loop over a data structure to repeat a block of HTML (PDF p. 56). All modern web frameworks use templates, with differing syntax (PDF p. 56).

## Databases
- Dynamic pages commonly read from a database: the product lookup on a retail site, or the timeline and notifications on a social site. Most modern sites keep user information in databases, and the link between server and database is a frequent hacker target (PDF p. 56).
- Databases predate the web. From the 1960s companies digitised and centralised records for easier searching and maintenance, and putting a web front end on an inventory database was a natural move to online retail (PDF p. 56).
- Databases also back authentication: the site records who signed up and checks returning users' login details against stored credentials (PDF p. 57).
- The two most common kinds are SQL and NoSQL (PDF p. 57).

### SQL databases
- Most used today are relational databases using Structured Query Language (SQL), a declarative language for maintaining and fetching data (PDF p. 57). The pronunciation note says it can be said letter by letter or as "sequel" (PDF p. 57).
- Relational means data sits in tables related in formally defined ways. A table resembles a spreadsheet: each row is an item and each column a data point, with predefined column types such as text strings, numbers or dates (PDF p. 57).
- Tables link through keys. Each row normally has a unique numeric primary key, and other tables point at rows through foreign keys. Example: an orders table has a user_id column holding foreign-key values that refer to the id primary key in the users table. This means no order can exist without its user, and each user has one single source of truth (PDF p. 57).
- Data integrity constraints prevent corruption and make queries uniform. Examples: require the email address column in a users table to be unique so every user has a different address, or make it non-null so every user must have one (PDF p. 57).
- SQL databases are transactional and consistent. A transaction is a batch of SQL statements; transactional means all-or-nothing, so if any statement fails the whole batch fails and leaves the database unchanged. Consistent means a successful transaction always moves the database from one valid state to another, and inserting invalid data makes the whole transaction fail (PDF p. 57).
- Because SQL data is often highly sensitive, hackers steal it to sell on the black market and also exploit insecurely built SQL statements; Chapter 6 shows how (PDF p. 58). See WS-C06-002.

### NoSQL databases
- SQL databases are often a performance bottleneck: if most requests trigger a database call, the server is heavily loaded and the site slows for everyone (PDF p. 58).
- This popularised NoSQL databases, which give up SQL's strict integrity rules to scale better. The term covers many approaches, but trends exist (PDF p. 58).
- They are often schemaless, so you can add fields to new records without upgrading any structure. Data is commonly held as key-value pairs or in JavaScript Object Notation (JSON) (PDF p. 58).
- They tend to favour wide replication of data over absolute consistency. SQL guarantees simultaneous queries from different clients see identical results; NoSQL often promises only eventual consistency (PDF p. 58).
- Storing unstructured or semistructured data is easy, but extraction and querying are somewhat harder: some offer a programmatic interface, others invent query languages adapted from SQL syntax (PDF p. 58).
- NoSQL databases can suffer injection attacks much like SQL ones, though an attacker has to guess the database type correctly (PDF p. 58).

## Distributed caches
- Dynamic resources can also read from in-memory distributed caches, another route to the scale big sites need. Caching means keeping a copy of data held elsewhere in an easily retrievable form to speed access (PDF p. 58).
- Redis and Memcached are the named examples. They make caching easy and let software on different servers and processes share data structures regardless of language. A cache shared among web servers suits frequently accessed data that would otherwise be fetched from a database (PDF p. 58).
- Large web firms typically build their stack as microservices, simple modular services each performing one action on demand, and use distributed caches for communication between them. Services often exchange work through queues kept in a cache, which hold tasks in a waiting state for numerous worker processes to finish one at a time. They may also use publish-subscribe channels, where many processes register interest in an event type and are notified together when it happens (PDF pp. 58-59).
- Caches are open to attack the same way databases are. Redis and Memcached were written when such threats were well known, so good practice is mostly built into the software development kits (SDKs), the code libraries used to connect to them (PDF p. 59).

## Web programming languages
Server code runs while dynamic resources are evaluated. Many languages are usable and each has its own security considerations; later chapters use these languages in code samples (PDF p. 59).
- Ruby (on Rails): Ruby appeared in Japan in the mid 1990s and became popular about a decade later with Ruby on Rails. Rails builds in many best practices for large applications with minimal configuration, and its community takes security seriously; it was among the first stacks to protect against cross-site request forgery. Its ubiquity still makes it a target, and several major vulnerabilities were found and hastily patched in recent years. Microframeworks such as Sinatra are lighter alternatives: you combine single-purpose libraries to keep the server deliberately small, in contrast to Rails' kitchen-sink approach, and get extra features from the RubyGems package manager (PDF p. 59).
- Python: invented in the late 1980s, popular for clean syntax, flexible style and many modules, and the usual choice for data science and scientific computing. Whitespace and indentation carry meaning, which surprises newcomers and has fuelled community arguments over tabs versus spaces. Web developers can choose among actively maintained servers such as Django and Flask. That diversity acts as a security feature because attackers are less likely to focus on one platform (PDF pp. 59-60).
- JavaScript and Node.js: JavaScript began as a small in-browser scripting language, then took off on servers with the Node.js runtime, which sits on the V8 engine that Chrome uses. Using one language on client and server made Node the fastest-growing web platform. Its largest security risk comes from rapid growth, with hundreds of modules added daily, so take extra care with third-party code (PDF p. 60). See WS-C14-002.
- PHP: grew from a set of C binaries for building dynamic Linux sites into a full language, but its unplanned evolution shows in inconsistent built-in functions (variable names are case-sensitive, function names are not). It once powered about 10 percent of sites. Writing PHP often means maintaining a legacy system, and older PHP frameworks have some of the worst vulnerabilities; legacy systems should move to modern libraries. Command execution, directory traversal and buffer overflows have all affected PHP programmers (PDF p. 60).
- Java: the JVM runs compiled bytecode across operating systems and is widely used in enterprises; it is a good workhorse when performance matters. Used for robotics, mobile apps, big data and embedded devices. Its popularity for web work has declined but millions of lines still run. Security-wise it is haunted by past popularity: legacy applications run old language and framework versions, so Java developers must upgrade to secure versions promptly. Other JVM languages with access to the Java ecosystem are Clojure (a Lisp dialect), Scala (functional with static typing) and Kotlin (newer, object-oriented, backward compatible with Java and easier for scripting) (PDF pp. 60-61).
- C#: Microsoft designed it for .NET, where C# and others like VB.NET run on the Common Language Runtime virtual machine. It is less abstracted from the OS than Java and can mix with C++. The reference implementation is now open source and the Mono project runs .NET on Linux and other systems, but most C# companies deploy on Windows servers and the typical Microsoft stack. Windows has a troubling security history, being the most common target platform for viruses, so adopters should be aware of the risks (PDF p. 61).

## Client-side JavaScript
- Server code can be written in many languages, but code that runs in the browser has exactly one option: JavaScript. Server-side JavaScript's popularity is partly credited to developers' prior familiarity with it from client-side work (PDF p. 61).
- Browser JavaScript has moved far past simple form validation and animated widgets. A complex site such as Facebook redraws regions of the page as you interact, for example showing a menu on an icon click, opening a dialog on a photo click, or adding notification markers when background events such as comments occur (PDF p. 61).
- Doing this without reloading the page requires client-side JavaScript to hold a lot of state in memory. Frameworks organise that state, render efficiently and allow modular reuse of code across pages, which matters with millions of lines of JavaScript (PDF p. 61).
- Angular, first released by Google as open source, borrows server-side ideas and uses client-side templates. Its template engine runs in the browser at page load, parsing the server-supplied template HTML and processing directives as it meets them. Because it is plain JavaScript in the browser it can write straight to the DOM and bypass part of the rendering pipeline, and it re-renders the DOM automatically as memory state changes, giving cleaner, more maintainable code (PDF p. 61).
- React, open source from Facebook's team, takes a different path: instead of code in HTML templates, developers put HTML-like tags directly into JavaScript. They usually write JavaScript XML (JSX) files that a preprocessor compiles to JavaScript before the browser gets them (PDF p. 62). A line such as `return <h1>Hello, {format(user)}</h1>` can look odd at first, but making HTML a first-class part of the syntax enables things like syntax highlighting and code completion (PDF p. 62).
- Security note: code that manipulates the DOM directly is prone to a distinct vulnerability, DOM-based cross-site scripting, detailed in Chapter 7 (PDF p. 62). See WS-C07-004.
- Browsers normally run only JavaScript, but you need not write all client code in it. Languages such as CoffeeScript and TypeScript are transpiled to JavaScript at build time. They share JavaScript's runtime vulnerabilities, so the book mostly sticks to plain JavaScript (PDF p. 62).

## Relations
Continues from the static side in WS-C04-003 and the two-way split in WS-C04-002; recapped in WS-C04-005. Browser-side JavaScript background is in WS-C03-003. Build processes that transpile code are discussed in the release material of Chapter 5.

## Time-sensitive statements
Product, language and framework facts reflect the time the book was written: Rails vulnerabilities "in recent years", Django, Flask, Sinatra, Node module growth, PHP powering 10 percent of sites, Java's declining web popularity, Mono and the open-source status of C#, Redis, Memcached, Angular, React, and the named JVM languages.
