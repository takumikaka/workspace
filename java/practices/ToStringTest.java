class Apple{
    private String color;
    private double weight;
    public Apple(String color, double weight){
        this.color = color;
        this.weight = weight;
    }

    public String getColor(String color){
        return this.color;
    }
    public double getWeight(double weight){
        return this.weight;
    }

    public String toString(){
        return "app color is: " + color + " .apple weight is: " + weight;
    }
}

public class ToStringTest{
    public static void main(String[] args){
        Apple apple = new Apple("Red", 1.23);
        System.out.println(apple);
    }
}
