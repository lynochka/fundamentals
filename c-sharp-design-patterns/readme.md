## Versions
.NET 6.0, C# 10

## Gang of Four (23 patterns)

- Intent of the pattern
- Structure of the pattern
- Variations, points of interests, alternatives, extensions, ...
- User-cases, consequences, related patterns.


## Pattern types
### Creational

#### Singleton 

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

#### Abstract Factory
#### Builder
#### Factory Method
#### Prototype
  

### Structural
  - Adapter
  - Bridge
  - Composite
  - Decorator
  - Facade
  - Flyweght
  - Proxy

### Behavioral
  - Chain of Responsibility

Passes a request along a chain of receivers

  - Command

Connects senders withe receivers unindirectionally

  - Interpreter
  - Iterator
  - Mediator
  - Momento
  - Observer
  - State
  - Strategy
  - Template Method
  - Visitor


## Common Object-Oriented pricipals
- Program to an interface, not an implementation
  - Interface as the object's type - a set of requests an object can respond to
- Favor object composition over class inheritance