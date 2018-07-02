class Tractor extends CarType
{
    public Tractor(double weight, String color, String name)
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
        System.out.println("This is Tractor!");
        System.out.println("The Tractor name is: " + name);
        System.out.println("The Tractor weight is: " + weight + "kg");
        System.out.println("The Tractor color is: "  + color);
    }

    public static void main(String[] args)
    {
        Tractor tractor = new Tractor(2296, "red", "dongfanghong");
        tractor.run();
    }
}
