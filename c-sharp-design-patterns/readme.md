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
Intent: to provide an interface for creating families of related or dependant objects without specifying their concrete classes.

Use-cases:
1. When a system should be independent of how its products are created, composed and represented.
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
Intent: separate the construction of a complex object from its representation. The same construction process can create different representations.

Use-cases:
1. To make an algorithm for creating complex object independent of the parts that make up the object and how they are assembled.
1. To allow different representations for the object that's constructed.

Related patterns:
* Can be implemented as a singleton.
* With abstract factory both can be used to construct complex objects, but the builder constructs the complex object step by step.
* Composites are often built by builders.


### Prototype
Intent: specify the kinds of objects to create using a prototypical instance and create new objects by copying this prototype.

Use-cases:
1. When a system should be independent of how its objects are created, and (A) to avoid building a set of factories that mimic the class hierarchy, (B) when instances of a class can have one of only a few different combinations of states.

Related patterns:
* Can be implemented as a singleton.
* In relation to FM - no subclassing is needed, not based on inheritance, but an initialize action on Product is often required.
* In relation to abstract factory - a factory might store a set of prototypes from which it clones when a new instance is requested.  
* Decorator can use prototype for convenient object creation.


## Structural

### Adapter (a wrapper pattern)
Intent: to convert the interface of a class into another interface clients expect. It lets classes with otherwise incompatible interfaces work together.

- Class adapter (relies on composition)
- Object adapter (relies on multiple inheritance, C# supports a variation by combining a base class with an interface)

Related patterns:
* Bridge separates interface from implementation, adapter changes the interface of an existing object.
* Decorator changes an object without changing its interface, adapter ... 
* With facade you define a new interface for an entire subsystem, with adapter you are making an existing interface useable via wrapping.
* Proxy defines a surrogate for another object, but does not change its interface.


### Bridge
Intent: decouple an abstraction from its implementation so the two can vary independently.

Separate abstraction from implementation: a means to replace implementation with another implementation without modifying the abstraction. See 'abstraction' as a way to simplify something complex.

Use-cases:
1. Avoid a permanent binding between an abstraction and its implementation, e.g., to enable switching implementations at runtime.
1. When abstraction and implementation should be externsible by subclassing.
1. You don't want changes in the implementation have an impact on the client.

Related patterns:
* Abstract factory can create and cofigure a bridge.
* Adapter lets unrelated classes work together, brigde lets abstractions and implementations vary independently.
* Strategy & State are based on composition, like bridge.


### Decorator
Intent: attach (or withdraw) additional responsibilities to an object dynamically (at runtime). It provides a flexible alternative to subclassing for extending functionality, 

`Component` - an interface for objects that can have responsibilities added to them dynamicaly.

`Decorator` maintains a reference to a Component object and defines an interface that conforms to Component's interface.

* Decorator helps when subclassing is impractical or impossible.
* Use the pattern to split feature-loaded classes until there's just one responsibility left per class.
* Increases the effort to learn the system having many small simple classes.

Related patterns:
* Adapter gives a new interface to an object, decorator only changes its responsibilities.
* A decorator can be viewed as a composite with only one component, but is not intended for object aggregation.
* Strategy lets you change the inner workings of an object, while the decorator changes its skin :D


### Composite
Intent: composite objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformaly: as if they all were individual objects.

`Component` declares the interface for objects in the compositions, and contains a common operation. It potentially implements the default behavior (when implemented as an abstract class).

`Leaf` represents an object in the composition that has no children. It defines behavior for primitive objects in the composition.

`Composite` stores child components and defines behavior for components having children.

`Client` manipulates objects in the composition through the Component interface.

* Component abstract base can, if needed, define an operation to get a specific child by index.
* Similarly add/remove operations do not have to be defined by Component, but exist on Composite directly.
* Composition makes the client simple.
* It is easy to add new kinds of components: open/closed principle.
* The overall system can become too generic - harder to restrict the components of a composite.

Related patterns:
* Leaf component can pass a request through a chain of all parent components.
* Iterator can be used to traverse composites.
* Visitor can be used to execute an operation over the full composite tree. It can localize operations and behavior that would otherwise be distributed across composite and leaf classes.


### Facade
Intent: provide a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

* Facade knows which subsystem classes are responsible for a request, and delegates client requests to appropriate subsystem objects.

Related patterns:
* Abstact factory can provide an interface for creating subsytem objects.
* Mediator also abstracts functionality of existing classes, but its purpose is abstracting communication between objects, while facade is about promoting ease of use.
* Adapter makes existing interface useable by wrapping one object, while with facade you're defining a new interface for an entire subsystem.


### Flyweight
### Proxy

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