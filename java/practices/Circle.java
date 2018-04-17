public class Circle extends Shape{
    private double pi = Math.PI;
    private double r;
    public Circle(String color, double r){
        super(color);
        this.r = r;
    }
    public double callPerimeter(){
        return 2 * pi * r;
    }
    public String getType(){
        return "Circle.";
    }

    public static void main(String[] args){
        Shape triangle = new Triangle("Red", 3, 4, 5);
        Shape circle = new Circle("Blue", 2);
        System.out.println("Triangle's callPerimeter: " + triangle.callPerimeter());
        System.out.println("Circle's callPerimeter: " + circle.callPerimeter());
        System.out.println("Triangle's Type: " + triangle.getType());
        System.out.println("Circle's Type: " + circle.getType());
    }
}
