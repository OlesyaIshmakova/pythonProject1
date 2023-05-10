 abstract class Figure
      {
            public Figure(string n)
            }
            private string name;
            public abstract void Draw();
            public abstract void Square();
            public void ShowName()
            {
                Console.WriteLine(name);
            }
        }
        class Rectangle : Figure
        {
            int width;
            int height;
            public Rectangle(int height, int width)
                : base("Прямоугольник")
            {
                this.width = width;
                this.height = height;
            }
            public override void Draw()
            {
                for (int i = 0; i < height; i++)
                {
                    for (int j = 0; j < width; j++)
                    {
                        Console.Write("*");
                    }
                    Console.WriteLine();
                }
            }
            public override void Square()
            {
                Console.WriteLine("Площадь прямоугольника равна {0} ",width * height);
            }
        }
        class Triangle : Figure
        {
            int length;
            public Triangle(int length)
                : base("Треугольник")
            {
                this.length = length;
            }
            public override void Draw()
            {
                for (int i = 0; i < length; i++)
                {
                    Console.Write("*");
                    for (int j = 0; j < i; j++)
                    {
                        Console.Write(" * ");
                    }
                    Console.WriteLine();
                }
            }
            public override void Square()
            {
                double s = Math.Pow(length,2) * Math.Sqrt(3) / 4;
                Console.WriteLine("Площадь треугольника равна {0} ",  s);
            }
        }
        static void Main(string[] args)
        {
            try
            {
                Rectangle myRect = new Rectangle(7, 10);
                myRect.ShowName();
                myRect.Draw();
                myRect.Square();
                Triangle myTriangle = new Triangle(6);
                myTriangle.ShowName();
                myTriangle.Draw();
                myTriangle.Square();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
...