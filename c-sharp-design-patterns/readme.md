# Versions
.NET 6.0, C# 10

# Gang of Four (23 patterns)

- Intent of the pattern
- Structure of the pattern
- Variations, points of interests, alternatives, extensions, ...
- User-cases, consequences, related patterns.


# Pattern types
## Creational

### Singleton 
Intent: ensure that a class only has one instance, and to provide a global point of access to it

Example: a logger.

- The intent should be the responsibility of the class itself (or another component as inversion-of-control container).

- Make class constructor private (protected is acceptable if you want to subclass the logger).

- Static method/property that returns an instance of itself.

- Accessed the first time - gets created and stored, after that - the previously created instance is returned.

- Preferred lazy instantiation.

Singleton pattern structure:
1. Defines an instance operation that lets clients access its unique instance.
1. On it, a public static property instance exists.
1. A private backing field contains the stored instance value.
1. SingletonOperation() is an operation on the singleton instance, such as `Log()`.

(!) Violates single responsibility principle.

### Factory Method
Intent: to define an interface for creating an object, but to let a subclass decide which class to instatiate.
FM lets a class differ instantiation to one or more subclasses.

Use-cases: 
1. When a class can't anticipate the class of objects it must create.
1. When a class wants its subclasses to specify the objects it creates.

Product and Creator can be implemented as interface instead of an abstract base class.

### Abstract Factory
Intent: to provde an interface for creating families of related or dependant objects without specifying their concrete classes.

Use-cases:
1. When a system should be independent of how ots products are created, composed and represented.
1. When you want to provide a class library of products and only reveal their interfaces, but not their implementations.
1. When a system should be considered with one of multiple families of products.

| Factory method | Abstract Factory |
|---|---:|
|Exposes an interface with a method on it, the factory method, to create an object of a certain type| Exposes an interface to create related objects: families of objects|
|Produces one product| ... a family of products|
|Creates objects through inheritance | ... through composition|

Related patterns:
* A concrete factory is often implemented as a singleton
* Often implemented with factory methods
* Can be implemented using prototypes


### Builder
Related patterns:
* Can be implemented as a singleton


### Prototype
Related patterns:
* Can be implemented as a singleton
* In relation to FM - no subclassing is needed, not based on inheritance, but an initialize action on Product is often required
  

## Structural
  - Adapter
  - Bridge
  - Composite
  - Decorator
  - Facade
  - Flyweght
  - Proxy

## Behavioral

### Chain of Responsibility

Passes a request along a chain of receivers

### Command
Connects senders withe receivers unindirectionally

### Interpreter
### Iterator
### Mediator
### Momento
### Observer
### State
Related patterns:
* State objects are often implemented as singletons)


### Strategy
### Template method
Related patterns:
* FMs are often called from within template methods


### Visitor


# Common Object-Oriented pricipals
- Program to an interface, not an implementation
  - Interface as the object's type - a set of requests an object can respond to
- Favor object composition over class inheritance