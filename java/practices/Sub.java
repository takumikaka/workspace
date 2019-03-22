class Base{
    public double size;
    public String name;
    public Base(double size, String name){
        this.size = size;
        this.name = name;
    }
}

public class Sub extends Base{
    public String color;
    public Sub(double size, String name, String color){
        super(size, name);
        this.color = color;
    }

    public static void main(String[] args){
        Sub su = new Sub(1.2, "Apple", "Red");
        System.out.println(su.size);
        System.out.println(su.name);
        System.out.println(su.color);
    }
}
