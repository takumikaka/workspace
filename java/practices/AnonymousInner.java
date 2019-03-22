abstract class Device{
    private String name;
    public abstract double getPrice();
    public Device(){}
    public Device(String name){
        this.name = name;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
}
public class AnonymousInner{
    public void test(Device d){
        System.out.println("Buy: " + d.getName() + ". Cost: " + d.getPrice());
    }
    public static void main(String[] args){
        AnonymousInner ai = new AnonymousInner();
        ai.test(new Device("Java"){
            public double getPrice(){
                return 9.99;
            }
        }
        );
        Device d = new Device()
        {
            public double getPrice(){
                return 8.88;
            }
            public String getName(){
                return "Python";
            }
        };
        ai.test(d);
    }
}
