interface Product{
    public double getPrice();
    public String getName();
}

public class AnonymouseTest{
    public void test(Product p){
        System.out.println("Purchase the name of the goods: " + p.getName() + ". It tooks off: " + p.getPrice());
    }
    public static void main(String[] args){
        AnonymouseTest at = new AnonymouseTest();
        at.test(new Product()
        {
            public double getPrice(){
                return 567.8;
            }
            public String getName(){
                return "Apple";
            }
        }
        );
    }
}
