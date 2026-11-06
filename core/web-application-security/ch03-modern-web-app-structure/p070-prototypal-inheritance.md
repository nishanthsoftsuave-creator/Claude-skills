---
id: WAS-C03-008
title: Prototypal Inheritance
source_pages: "70-72"
chapter: 3
concepts: [prototypal-inheritance, prototype, proto, constructor, class-based-inheritance, runtime-mutation, prototype-pollution, javascript-security]
related: [WAS-C03-007, WAS-C03-009, WAS-C03-010]
time_sensitive: false
---
# Prototypal Inheritance
(Source: PDF pp. 70-72 from the "Prototypal Inheritance" heading)

## What the section covers
How JavaScript's prototype-based inheritance differs from class-based inheritance, a vehicle example, the ability to change prototypes at runtime, and why that matters for security (Prototype Pollution).

## Meaning
- Many server-side languages suggest class-based inheritance. JavaScript instead has a highly flexible prototypal inheritance system. Because few languages use that model, developers often disregard it and try to convert it into a class system (PDF pp. 70-71).
- In a class-based system classes are blueprints that define objects. Classes inherit from other classes to form hierarchies. In Java, subclasses are created with `extends` and objects with `new` (PDF p. 71).
- JavaScript does not truly support such classes, but because prototypes are so flexible it is possible to mimic classes with some abstraction on top. In a prototypal system every created object has a `prototype` property. That property carries a `constructor` property pointing back to the function that owns the prototype, so any object can be used to instantiate new objects (PDF p. 71).

## How it works: the vehicle example
- The book writes a simple "vehicle pseudoclass": a function taking make and model, storing them on `this`, and defining a print function that returns the make and model as a string. `new Vehicle('Toyota', 'Prius')` creates an object whose print call returns the text for the Toyota Prius (PDF p. 71).
- Whenever an object is created, a separate `__proto__` object is created too. It points at the prototype whose constructor was invoked during creation. That allows comparisons: a Prius and a Charger (Dodge) both created from `Vehicle` have equal `__proto__` values, showing both were built from Vehicle (PDF pp. 71-72).

## Runtime mutation
- Developers often modify the `prototype` of an object, which leads to confusing changes in application behaviour. Since all JavaScript objects are mutable by default, prototype properties can change at any time during runtime (PDF p. 72).
- Unlike rigid inheritance models, JavaScript inheritance trees can change at runtime, so objects can morph. Example: calling a get-max-speed function on the Prius fails with "not a function" because Vehicle lacks one. After assigning a function returning 100 (mph) to the Vehicle prototype, both the Prius and the Charger return 100, because changes propagate from the parent to its children in real time (PDF p. 72).

## Why it matters
- Prototypes take a while to get used to, but their power and flexibility outweigh the learning curve. They are especially important to understand when examining JavaScript security because few developers fully understand them (PDF p. 72).
- Because modifications to a prototype propagate to children, a special kind of attack called **Prototype Pollution** exists in JavaScript systems: modifying a parent object unintentionally changes the functionality of child objects (PDF p. 72).

## Limitations and failure modes
The same mutability that makes prototypes flexible lets later code alter behaviour for every child object (PDF p. 72).
INTERPRETATION: an attacker who can write to a parent object could therefore change behaviour for all of its children, which is the Prototype Pollution idea the book names.

## Relations
Context and `this` were covered just before (WAS-C03-007); asynchrony follows (WAS-C03-009). The DOM is another place where objects and prototypes appear (WAS-C03-010).
