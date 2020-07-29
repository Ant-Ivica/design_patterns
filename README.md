# Design Patterns

## Introduction

A design pattern is a general repeatable solution to a commonly occurring problem in software design. It isn't a 
finished design that can be transformed directly into code. It is a description or template for how to solve a problem
that can be used in many different situations.

Effective software design requires considering issues that may not become visible until later in the implementation.
Reusing design patterns helps to prevent subtle issues that can cause major problems and improves code readability for
coders and architects familiar with the patterns. 

They provide general solutions, documented in a format that doesn't require specifics tied to a particular problem.
In addition, patterns allow developers to communicate using well-known, well understood names for software interactions.

## Design patterns classification

There are three types of design patterns: creational, structural and behavioral.

## 1) Creational design patterns

These design patterns are all about class instantiation. This pattern can be further divided into class-creation 
patterns, which use inheritance, and object-creational patterns, which utilize delegation. 

### 1-1) Singleton

This design pattern is used when the application needs just one instance of an object. Singleton should be considered
only if all three of the following criteria are met:
 - Ownership of that single unique instance can't be reasonably assigned
 - Lazy initialization is desirable
 - Global access is not otherwise provided for

### 1-2) Builder

Builder is a creational design pattern which allows constructing complex objects step by step. It’s especially useful
when you need to create an object with lots of possible configuration options. The Builder pattern can be recognized in
a class which has a single creation method and several methods to configure the resulting object. Builder methods often
support chaining.

### 1-3) Prototype

Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their
classes. There are two ways to go about implementation:
 - Basic implementation - The Prototype pattern delegates the cloning process to the actual objects that are being
 cloned. The pattern declares a common interface for all objects that support cloning. This interface lets you clone an
 object without coupling your code to the class of that object. Usually, such an interface contains just a single clone
 method.
 - Prototype registry implementation - The Prototype Registry provides an easy way to access frequently-used prototypes.
 It stores a set of pre-built objects that are ready to be copied. The simplest prototype registry is a name → prototype
 key-value hash map. However, if you need better search criteria than a simple name, you can build a much more robust
 version of the registry. This implementation allows us to create clones of multiple types from a single source.

### 1-4) Factory method

Factory method defines an interface for creating an object, but lets subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses. There are two main component types in this pattern, the
factory, handling the 'logistics' of the process (single source of object instances) and the products, that are
responsible for creating themselves. The latter is achieved by the 'product' class containing a static method that
returns the instance of the object it belongs to.

### 1-5) Abstract factory

The purpose of the Abstract Factory is to provide an interface for creating families of related objects, without
specifying concrete classes. It defines a Factory Method per product. Each Factory Method is responsible for its own
product classes and their creation. 

### Final note

Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used
profitably. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone
and return product objects, Builder can use one of the other patterns to implement which components get built. Abstract
Factory, Builder, and Prototype can use Singleton in their implementation. Abstract Factory, Builder, and Prototype
define a factory object that's responsible for knowing and creating the class of product objects, and make it a 
parameter of the system. Abstract Factory has the factory object producing objects of several classes. Builder has the
factory object building a complex product incrementally using a correspondingly complex protocol. Prototype has the
factory object (aka prototype) building a product by copying a prototype object.