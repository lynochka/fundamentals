using System.Text;

namespace BuilderPattern
{
    /// <summary>
    /// Product class
    /// </summary>
    public class Car
    {
        private readonly List<string> _parts = new();
        private readonly string _carType;

        public Car(string carType)
        {
            _carType = carType;
        }

        public void AddPart(string part)
        {
            _parts.Add(part);
        }

        public override string ToString()
        {
            var sb = new StringBuilder();
            foreach (string part in _parts)
            {
                sb.Append($"Car of type {_carType} has part {part}. ");
            }

            return sb.ToString();
        }
    }

    /// <summary>
    /// Builder abstract class:
    /// Becomes responsible for constructing complex objects.
    /// </summary>
    public abstract class CarBuilder
    {
        public Car Car { get; private set; }

        public CarBuilder(string carType)
        {
            Car = new Car(carType);
        }
        public abstract void BuildEngine();
        public abstract void BuildFrame();
    }

    /// <summary>
    /// ConcreteBuilder1 class, i.e., complex object to build.
    /// </summary>
    public class MiniBuilder : CarBuilder
    {
        public MiniBuilder()
            : base("Mini")
        {
        }

        public override void BuildEngine()
        {
            Car.AddPart("'not a V8'");
        }

        public override void BuildFrame()
        {
            Car.AddPart("'3-door with stripes'");
        }
    }

    /// <summary>
    /// ConcreteBuilder2 class, i.e., complex object to build.
    /// </summary>
    public class BMWBuilder : CarBuilder
    {
        // Invoke base class constructor
        public BMWBuilder()
            : base("BMW")
        {
        }

        public override void BuildEngine()
        {
            Car.AddPart("'a fancy V8 engine'");
        }

        public override void BuildFrame()
        {
            Car.AddPart("'5-door with metallic finish'");
        }
    }

    /// <summary>
    /// Director.
    /// Is not repsonsible for constructing complex objects.
    /// </summary>
    public class Garage
    {
        private CarBuilder? _builder;

        public Garage()
        {
        }

        public void Construct(CarBuilder builder)
        {
            _builder = builder;

            _builder.BuildEngine();
            _builder.BuildFrame();
        }

        // variation: the show method on the director instead of on the product.
        public void Show()
        {
            Console.WriteLine(_builder?.Car.ToString());
        }
    }
}
