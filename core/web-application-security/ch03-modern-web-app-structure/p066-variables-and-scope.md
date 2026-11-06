---
id: WAS-C03-005
title: Variables and Scope
source_pages: "66-67"
chapter: 3
concepts: [javascript-variables, scope, global-scope, var, let, const, hoisting, window-object, block-scope, es6]
related: [WAS-C03-004, WAS-C03-006, WAS-C03-007, WAS-C03-010]
time_sensitive: false
---
# Variables and Scope
(Source: PDF pp. 66-67 from the "Variables and Scope" heading, plus PDF p. 68 above the "Functions" heading)

## What the section covers
The four ways to define a variable in ES6 JavaScript (a recent version at the time of writing), what each one does to scope, and the book's advice on which to prefer.

## Meaning: the four declarations
The book lists them with their effect (PDF p. 66):
- a bare assignment with no keyword;
- `var`, function scoped;
- `let`, block scoped;
- `const`, block scoped and not reassignable.

They look alike but behave very differently.

## How each one works
- **No identifier (a bare assignment).** The variable is hoisted into global scope, so any child of the global scope can access it. The book calls this generally a bad practice to avoid, and notes it could cause significant security vulnerabilities or functional bugs (PDF p. 66).
- In the browser such a variable also gets a pointer on the `window` object. Reading it directly or through the window property returns the same value (PDF p. 67). This can create naming conflicts on `window`, the object the browser DOM uses to maintain window state, which is another reason to avoid it (PDF p. 67).
- **`var`.** Scoped to the nearest function, or global if there is no outer function (in the global case it also appears on `window`). The book calls it confusing, probably the reason `let` was introduced (PDF p. 67). Its example defines a `var` inside an `if` block within a function and then logs it after the block ends: the log still prints 25. In most modern languages the value would be undefined there, but `var` binds to the function, not the block, which can lead new JavaScript developers into debugging confusion (PDF p. 67).
- **`let`.** ECMAScript 6 introduced `let` and `const`, two ways of creating a variable that act more like those in other modern languages. `let` is block scoped (PDF p. 67). In the matching example the variable is defined inside an `if` block and logging it outside returns undefined (this example is printed at the top of the next page). Block scope is considered better for readability and reduces scope-related bugs (PDF p. 68).
- **`const`.** Also block scoped, but it cannot be reassigned after creation, similar to `final` in Java. Assigning a new value throws a TypeError ("invalid assignment to const"). If the value is an object its properties can still change: `const` fixes the pointer in memory, not the value or its properties (PDF p. 68).

## When and how to apply
- The book's recommendation is to use `let` and `const` in your code to avoid bugs and improve readability (PDF p. 68).
- INTERPRETATION: during a code review or recon of client code, treat bare global assignments and heavy `var` use as signs that code may share state or collide on `window` unexpectedly.

## Limitations and failure modes
Bare globals and function-scoped `var` can leak a value outside the block where the author expected it to live, and global leaks can clash with the browser's own `window` properties (PDF p. 67).

## Relations
Functions are objects assigned with these same declarations (WAS-C03-006). `window` is a core DOM object (WAS-C03-010). The next quirk, context, uses the `this` keyword (WAS-C03-007).
