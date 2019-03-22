class Transport{
    public Transport(){

    }
}

class Bus extends Transport{
    private String color;
    private String brand;
    private double price;

    public Bus(){
        this.color = "Blue";
        this.brand = "Hexie";
        this.price = 0.0;
    }
    public Bus(String color, String brand){
        this.color = color;
        this.brand = brand;
    }
    public Bus(String color, String brand, double price){
        this(color, brand);
        this.price = price;
    }

    public void setColor(String color){
        this.color = color;
    }
    public String getColor(){
        return this.color;
    }
}

public class TransportTest{
    public static void main(String[] args){
        Bus bus = new Bus("Red", "BMW");
        System.out.println(bus.getColor());
    }
}
