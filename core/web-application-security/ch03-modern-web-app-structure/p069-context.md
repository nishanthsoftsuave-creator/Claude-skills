---
id: WAS-C03-007
title: Context
source_pages: "69"
chapter: 3
concepts: [javascript-context, this-keyword, bind-call-apply, arrow-function-context, shorthand-function, runtime-context]
related: [WAS-C03-006, WAS-C03-008, WAS-C03-005]
time_sensitive: false
---
# Context
(Source: PDF p. 69 from the "Context" heading, plus the top of PDF p. 70 above "Prototypal Inheritance")

## What the section covers
What a function's context is, how `this` exposes it, three built-in ways to move context between functions, and how arrow functions differ.

## Meaning
- For someone who can write code in another language, the book says five JavaScript topics need learning: scope, context, prototypal inheritance, asynchrony and the browser DOM (PDF p. 69).
- Every function has its own set of properties and data attached, called the function's **context**. Context is not fixed and can be changed at runtime. Objects held in it are referenced with the keyword `this` (PDF p. 69).
- In the book's example, a function sets `this.age` to 25 and logs it, getting 25. Logging `this.age` outside the function returns undefined (PDF p. 69).

## Why it matters
Many annoying bugs come from context being hard to debug, especially when the context of one object has to be passed to another function (PDF p. 70).

## How it works: moving context
- JavaScript offers `bind`, `call` and `apply` so developers can share context between functions (PDF p. 70).
- `bind` creates a new copy of a function with a given context (the book's example binds the age data to a get-age function, then calls the copy with the name "joe").
- `call` invokes the function immediately with a given context and a list of arguments.
- `apply` does the same with an array of arguments. The only difference between `call` and `apply` is that `call` takes a list and `apply` takes an array. They are interchangeable using spread syntax to destructure the array into a list (PDF p. 70).
- **Arrow (shorthand) functions** inherit context from the parent function, so context passes from parent to child without explicit calling, applying or binding (PDF p. 70).
- Example: a global context sets `garlic` to false, and a `soup` object has `garlic` set to true. A standard function attached to `soup` logs true, because its `this` is the soup. An arrow function attached to `soup` logs false, because its context is the global one (PDF p. 70).

## When and how to apply
The book says mastering these ways of managing context will make reconnaissance through a JavaScript-based server or client faster, and may even expose language-specific vulnerabilities that arise from these complexities (PDF p. 70).

## Relations
Arrow functions were listed in WAS-C03-006. The next language feature, prototypes, is in WAS-C03-008, and scope is in WAS-C03-005.
