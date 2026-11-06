---
id: WAS-C06-002
title: Detecting SPA Frameworks
source_pages: "120-121"
chapter: 6
concepts: [spa-frameworks, emberjs, angularjs, react, vuejs, global-objects, version-detection, fingerprinting, browser-console]
related: [WAS-C03-011, WAS-C06-001, WAS-C06-003]
time_sensitive: true
---
# Detecting SPA Frameworks
(Source: PDF pp. 120-121; the end of the Vue discussion continues onto PDF p. 122)

## What the section covers
How to recognise the four largest single-page-application frameworks of 2019 from the browser console and the page markup, and how to read their version.

## Meaning
- The frameworks named, in no particular order, are EmberJS (used by LinkedIn and Netflix), AngularJS (Google), React (Facebook) and VueJS (Adobe and GitLab) (PDF p. 120).
- Each has its own syntax and its own way of managing DOM elements, which is what makes it recognisable. Not every framework is this easy to spot; some need fingerprinting or more advanced techniques. Whenever a version is available, write it down (PDF p. 120).

## How it works
**EmberJS.** On start-up it creates a global variable named Ember, visible in the console. Figure 6-1 shows a to-do demo app whose console prints the version string. Ember also tags DOM elements with an ember-id, so the Elements tab shows divs with ids such as ember1, ember2 and ember3, all inside a parent with the class ember-application, usually the body. The version is a constant on that global: reading Ember.VERSION returns it (PDF p. 120).

**AngularJS.** Older releases expose a global object called angular whose version property holds the version. AngularJS 4.0 and later removed that global, so the version is harder to get. You can still tell that you face 4.0 or later by checking whether a global named ng exists. To read the version, collect the app's root elements with getAllAngularRootElements(), take the first, and read its ng-version attribute (the book's example shows 6.1.2) (PDF p. 121).

**React.** React is identified by a global named React, and React.version returns the version (the example prints 0.13.3). Script tags of type text/jsx are a strong sign, because that file format mixes JavaScript, CSS and HTML in one file. Knowing that each component lives in a single .jsx file makes it easier to investigate components one at a time (PDF p. 121).

**VueJS.** Vue exposes a global named Vue with a version constant, read as Vue.version (the example prints 2.6.10). If you cannot inspect elements on a Vue app, the app was probably configured to ignore developer tools, which is a toggled property on the global Vue object (PDF p. 121). Setting Vue.config.devtools to true lets you inspect Vue components in the console again (PDF p. 122).

## When and how to apply
INTERPRETATION: run these global-object checks in the console first, since they cost one line each, and fall back to markup clues such as ember-id attributes or ng-version when a global is missing.

## Limitations and failure modes
Newer AngularJS builds hide the global, so detection depends on attributes. A Vue app may disable developer tools until the devtools flag is changed.

## Relations
SPA frameworks were described as a technology in WAS-C03-011. The next row, WAS-C06-003, covers helper libraries, and WAS-C06-001 explains why versions matter.

## Time-sensitive statements
The list of largest frameworks is "as of 2019", and the customers and version numbers shown (Ember 3.x, Angular 6.x, React 0.13, Vue 2.6) are dated examples.
