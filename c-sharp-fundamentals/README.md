# C# Fundamentals

## Versions
 C# 10, .NET 6

## Creating console applications

.NET SDK:
```
dontnet new console -n "FirstProgram"
dotnet build
dotnet run
```

## Documentation
https://docs.microsoft.com/en-us/dotnet/csharp/
https://docs.microsoft.com/en-us/dotnet/api/?view=net-6.0

### Types
.NET types:
* Value data type
* Reference data type

User-defined types:
* Enumeration (value type)
* Struct (value type)
  * No need to use 'new': `WorkTask task;`
* Class
* Interface
* Delegate

Nullable value types:
```cs
int? a = null;
if (a.HasValue)
{
  Console.WriteLine($"a is {a.Value}");
}

int? c = null;
int d = c ?? -1;
```
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types

### VS
View-> Object-browser (right click -> View Namespaces)

Global using statements

Manage NuGet Packages via project right click.

F12: to go to the definition of the method

Add an assembly via:
project right click -> Add -> Project Reference...

Renaming: Ctrl + RR

### Misc

```cs
#region
//collapsed code
#endregion
```

# Garbage collection
```cs
employees.Clear()
employees = null;

GC.Collect();
```

### OO
Encapsulation
- Information is contained within the object, and only certain - exposed
- Properties, e.g.,
`public string Name { get; private set; } = "unknown";` (starts with capital letter)

Abstraction
Inheritance
Polymorphism



### Unit tests