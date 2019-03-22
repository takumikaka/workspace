public class Ostrich extends Bird{
    public void fly(){
        System.out.println("Can running.");
    }

    public static void main(String[] args){
        Ostrich bird = new Ostrich();
        bird.fly();
    }
}
