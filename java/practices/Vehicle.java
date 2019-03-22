class Vehicle extends CarType
{
    public Vehicle(String name, String color, double weight)
    {
        this.name = name;
        this.color = color;
        this.weight = weight;
    }

    public String getName(String name)
    {
        return this.name;
    }

    public String getColor(String color)
    {
        return this.color;
    }

    public double getWeight(double weight)
    {
        return this.weight;
    }

    public void run()
    {
        System.out.println("This is Vehicle!");
        System.out.println("The Vehicle name is: " + name);
        System.out.println("The Vehicle weight is: " + weight + "kg");
        System.out.println("The Vehicle color is: "  + color);
    }

    public static void main(String[] args)
    {
        Vehicle vehicle = new Vehicle("Haval H9", "Green", 2375);
        vehicle.run();
    }
}
