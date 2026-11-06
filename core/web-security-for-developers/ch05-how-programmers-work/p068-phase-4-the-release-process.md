---
id: WS-C05-005
title: Phase 4 - The Release Process
source_pages: "68-70"
chapter: 5
concepts: [release-process, reliable-releases, checksums, reproducible-releases, revertible-releases, paas, iaas, devops, containerization, docker, build-process, minification, css-preprocessors, database-migrations]
related: [WS-C05-004, WS-C05-006, WS-C05-008, WS-C11-001]
time_sensitive: true
---
# Phase 4 - The Release Process
(Source: PDF pp. 68-70, tail PDF p. 71. The row starts part-way down PDF p. 68 at the "Phase 4" heading; the test environment text above it is WS-C05-004. On the tail page, content above the "Phase 5" heading belongs here; Phase 5 is WS-C05-006.)

## What the section covers
The fourth SDLC phase: getting code onto the production server. It sets three qualities a release process must have, then covers standardised deployment (PaaS, IaaS with DevOps tools, containers), the build process and database migration scripts (PDF pp. 68-71).

## Meaning
A website release takes code from source control, copies it to a web server and typically restarts the server process. How you do it depends on hosting and technology, but the process must be reliable, reproducible and revertible (PDF p. 68).
- Reliable: you can guarantee exactly which code, dependencies, resources and configuration files are deployed. An unreliable process may leave you running a different version than you think, a serious security risk. Release scripts commonly use checksums, digital fingerprints confirming the files on the server are identical to those in source control (PDF p. 68).
- Reproducible: it can be rerun with the same results in other environments or with other code versions. This leaves less room for manual error; if success needs an administrator to perform 24 steps flawlessly in order, mistakes will happen. Script and automate as much as possible. A reproducible process is also essential for building good test environments (PDF pp. 68-69).
- Revertible: you can roll back a release when something unexpected happens, and the rollback should be seamless. Partly rolled-back code is dangerous because an insecure configuration or software with known vulnerabilities may be left in place. Whatever process you choose, you must be able to return reliably to a previous version with minimal fuss (PDF p. 69).

## Options for standardised deployment
### Platform as a Service
- PaaS offerings from hosting companies make releasing easy and reliable: "as a service" means running on others' servers with helpful automation and an admin website. Named providers are Microsoft Azure, Amazon Web Services Elastic Beanstalk, Google App Engine and Heroku (PDF p. 69).
- They let developers release with a single command-line call. The platform sets up virtualised servers, installs the operating system and virtual machines, runs the build, loads dependencies, deploys code to disk and restarts the web server. Releases can be monitored and rolled back from a web console or command line, and safety checks help ensure a clean deploy. Benefits: minimal downtime, clean deployment and a full audit trail (PDF p. 69).
- Trade-offs: only certain languages and operating systems are supported, server configuration is limited, and complex network layouts are not supported, so retrofitting legacy applications can be hard (PDF p. 69).

### Infrastructure as a Service and DevOps
- If PaaS is unsuitable because the application is too complex or old or the cost too high, code is deployed to individual servers, self-hosted, in a data centre, or virtualised under Infrastructure as a Service (IaaS) such as Amazon Elastic Compute Cloud (EC2). You then write your own release process (PDF p. 69).
- Traditionally dedicated system administrators designed and ran releases. DevOps (developer operations) tools, such as Puppet, Chef and Ansible, have blurred that line and given developers more control. They let you describe standard deployment scenarios and modularise release scripts, and are generally much more reliable than custom scripts that copy files to servers. Most scenarios are already covered by existing "recipes" so best practice is easy to follow (PDF pp. 69-70).

### Containerization
- Technologies such as Docker use configuration scripts called images that describe the operating system, disk layout, third-party software and web application to deploy. An image is deployed to a container that abstracts parts of the underlying operating system; everything specific to the release lives in the image and the container itself is generic (PDF p. 70).
- Images deploy reproducibly to real or virtual servers, giving a reliable release. Developers can test locally with the exact image used in production, so fewer surprises at release (PDF p. 70).
- The book calls containerization relatively new. Related tools such as Docker Swarm and Kubernetes describe complex multi-server layouts in machine-readable files, making whole environments easy to rebuild; a team could start a new test environment with several web servers and a database from a single configuration file (PDF p. 70).

## The build process
- Most codebases have a build process, run from the command line or development tools, that turns static code into something deployable. Java and C# compile source into a deployable binary format, while languages with package managers download and validate third-party code (dependencies) during the build (PDF p. 70).
- Website builds often prepare client-side assets. Languages such as TypeScript and CoffeeScript must be compiled to JavaScript. Whether hand-written or generated, JavaScript is usually minified or obfuscated into a compressed, less readable, functionally equivalent file that loads faster (PDF pp. 70-71).
- CSS (covered in Chapter 3) is hard to manage on big sites because styling is duplicated in many places. Developers often use preprocessors such as Sass and SCSS that are converted to CSS at build time (PDF p. 71).
- Each language has a preferred build tool that the team should know well. Run the build locally before committing code, so you know it works before it reruns during release, and use a continuous integration server to make sure that happens (PDF p. 71).

## Database migration scripts
- New features often need new tables or changes to existing ones. Databases hold data that must persist across releases, so you cannot wipe and reinstall one each time. Create and run database migration scripts as part of release, updating the structures before deploying the code, and undo them when rolling back code (PDF p. 71).
- Some technologies, such as Ruby on Rails, can run migrations during the build. Otherwise keep the scripts in source control and run them with temporarily elevated database permissions during the release window. Big, complex databases often have dedicated database administrators (DBAs) who manage this as gatekeepers (PDF p. 71).
- Security risk: if staff can change database structures outside a release, that is a hazard. Chapter 11 discusses ways to lock down permissions (PDF p. 71). See WS-C11-001.

## Time-sensitive statements
Named services and tools: Azure, AWS Elastic Beanstalk, Google App Engine, Heroku, EC2, Puppet, Chef, Ansible, Docker, Docker Swarm, Kubernetes, Sass, SCSS, TypeScript, CoffeeScript. The "relatively new" description of containers reflects the time the book was written.

## Relations
Follows test environments (WS-C05-004); post-release testing is WS-C05-006. Recapped in the chapter summary, WS-C05-008.
