# C# Fundamentals

## Versions
 C# 10, .NET 6

## Documentation
https://docs.microsoft.com/en-us/dotnet/csharp/
https://docs.microsoft.com/en-us/dotnet/api/?view=net-6.0


## Creating console applications
.NET SDK:
```
dontnet new console -n "FirstProgram"
dotnet build
dotnet run
```

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

Debug:
- Authos window - shows variables in scope, allows to 'Add (items to) watch'
- Debug > Windows > Output

### Misc
```cs
#region
//collapsed code
#endregion
```

### Garbage collection
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
- Public, private, protected

Inheritance
- Is-A relation vs. Has-A relation (Composition)

Polymorphism
- Overriding a base class implementation
- Uses virtual and override keywords

Interface
- As a contract

### Unit tests

Unit Test as a separate project.

- NUnit
- xUnit

## Next
### Working with DBs
ADO.NET (older), Entity Framework Core (an ORM, object-relational mapper)

### Linq (Language-Integrated Query)

### Async coding

### Deskop Applications
WPF, WinForms (older)

### Web
ASP.NET Core
- Server-side UI: MVC, Razor Pages
- Client-side UI: Blazor

### API
ASP.NET Core

### Mobile
Xamarin, Maui