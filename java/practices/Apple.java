public class Apple{
    public String name;
    public String color;
    public double weight;

    public Apple(String name, String color){
        this.name = name;
        this.color = color;
    }

    public Apple(String name, String color, double weight){
        this(name, color);
        this.weight = weight;
    }

    public static void main(String[] args){
        Apple apple = new Apple("Big Apple", "Red", 0.5);
        System.out.println("apple.name is: " + apple.name + " apple.color is: " + apple.color + " apple.weight is: " + apple.weight);
    }
}
