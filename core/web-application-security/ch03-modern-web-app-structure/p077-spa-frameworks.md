---
id: WAS-C03-011
title: SPA Frameworks
source_pages: "77"
chapter: 3
concepts: [spa-frameworks, single-page-application, reactjs, vuejs, emberjs, angularjs, ui-components, application-state]
related: [WAS-C03-010, WAS-C03-012, WAS-C06-002, WAS-C03-001]
time_sensitive: true
---
# SPA Frameworks
(Source: PDF p. 77 from the "SPA Frameworks" heading, plus the top of PDF p. 78 above "Authentication and Authorization Systems")

## What the section covers
Why single-page application (SPA) frameworks arose, what they provide, and which ones are the largest.

## Background
- Older websites were built with ad hoc script that manipulated the DOM plus a lot of reused HTML template code. That model did not scale. It worked for delivering static content but not for complex, logic-rich applications (PDF p. 77).
- Desktop software at the time was robust and let users store and maintain application state. Websites then could not do this, although many companies would have preferred to deliver complex applications over the web for benefits ranging from ease of use to piracy prevention (PDF p. 77).

## Meaning and purpose
SPA frameworks were designed to bridge the functionality gap between websites and desktop applications. They allow complex JavaScript applications that store their own internal state and are composed of reusable UI components. Each component has its own self-maintained life cycle, from rendering to logic execution (PDF p. 77).

## Where they are used
- SPA frameworks are rampant today, backing the largest and most complex applications such as Facebook, Twitter and YouTube, where functionality is key and a near-desktop experience is delivered (PDF p. 78).
- The largest open source SPA frameworks named are ReactJS, EmberJS, VueJS and AngularJS. All are built on JavaScript and the DOM but add complexity from both security and functionality perspectives (PDF p. 78).
- Figure 3-4 (rendered and read) is the VueJS home page. It carries the tagline "The Progressive JavaScript Framework", buttons for why Vue.js, get started and GitHub, a special sponsor logo, and three claims: approachable (knowing HTML, CSS and JavaScript is enough), versatile (an incrementally adoptable ecosystem) and performant (a 20KB min+gzip runtime). The caption describes Vue as building on top of web components (PDF p. 78).

## When and how to apply
INTERPRETATION: expect any large modern interface to be built this way, which is why recon in Chapter 6 includes fingerprinting the framework and its version.

## Time-sensitive statements
The list of largest frameworks, their well-known users, and the figure's claims (including the runtime size) are from the time of writing.

## Relations
The DOM they build on is in WAS-C03-010. The architecture shift they belong to is in WAS-C03-001, and detection of frameworks is in WAS-C06-002.
