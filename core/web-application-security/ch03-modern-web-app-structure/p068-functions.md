---
id: WAS-C03-006
title: Functions
source_pages: "68"
chapter: 3
concepts: [javascript-functions, anonymous-function, arrow-function, iife, function-scope, first-class-functions, function-declaration]
related: [WAS-C03-005, WAS-C03-007]
time_sensitive: false
---
# Functions
(Source: PDF p. 68 from the "Functions" heading, plus the top of PDF p. 69 above the "Context" heading)

## What the section covers
In JavaScript functions are objects, so they can be assigned and reassigned with the same variable declarations just covered. The section lists the forms a function can take.

## Meaning: the forms
The book gives seven examples (PDF pp. 68-69):
1. an **anonymous function** with no name or assignment;
2. a **globally declared named function** (a bare assignment);
3. a **function-scoped named function** (using `var`);
4. a **block-scoped named function** (using `let`);
5. a **block-scoped function without reassignment** (using `const`);
6. an **arrow (shorthand) function** that inherits the context of its parent;
7. an **IIFE**, an immediately invoked function expression.

## How they work
- The anonymous function cannot be referenced after it is created (PDF p. 69).
- The next four are ordinary functions whose scope depends on the declaration, exactly like the variable examples for age earlier (PDF p. 69).
- The arrow function shares `context` with its parent, which the next section explains (PDF p. 69).
- The IIFE is a special form the author expects to be found mostly in JavaScript. It fires immediately when loaded and runs inside its own namespace. More advanced JavaScript developers use it to keep blocks of code from being reachable elsewhere (PDF p. 69).

## When and how to apply
INTERPRETATION: when reading unfamiliar client code, an IIFE wrapper usually signals deliberate encapsulation, so global variables you see on `window` may not include what is declared inside it.

## Relations
Declaration keywords come from WAS-C03-005; the sharing of context by arrow functions is detailed in WAS-C03-007.
