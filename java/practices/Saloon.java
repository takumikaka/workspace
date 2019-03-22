class Saloon extends CarType
{
    public Saloon(String name, String color, double weight)
    {
        this.weight = weight;
        this.color = color;
        this.name = name;
    }

    public double getWeight(double weight)
    {
        return this.weight;
    }

    public String getColor(String color)
    {
        return this.color;
    }

    public String getName(String name)
    {
        return this.name;
    }

    public void run()
    {
        System.out.println("This is Saloon!");
        System.out.println("The Saloon name is: " + name);
        System.out.println("The Saloon weight is: " + weight + "kg");
        System.out.println("The Saloon color is: "  + color);
    }

    public static void main(String[] args)
    {
        Saloon saloon = new Saloon("Audi A8", "Blue", 1890);
        saloon.run();
    }
}
