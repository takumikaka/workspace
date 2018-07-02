class Truck extends CarType
{
    public Truck(String name, String color, double weight)
    {
        this.name = name;
        this.color = color;
        this.weight = weight;
    }

    public String getName(String name)
    {
        return this.name;
    }

    public String color(String color)
    {
        return this.color;
    }

    public double weight(double weight)
    {
        return this.weight;
    }

    public void run()
    {
        System.out.println("This is Truck!");
        System.out.println("The Truck name is: " + name);
        System.out.println("The Truck weight is: " + weight + "kg");
        System.out.println("The Truck color is: "  + color);
    }

    public static void main(String[] args)
    {
        Truck truck = new Truck("Ford f150", "Blue", 3198);
        truck.run();
    }
}
