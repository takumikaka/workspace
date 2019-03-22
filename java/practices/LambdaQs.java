interface Eatable{
    public void taste();
}
interface Flyable{
    public void fly(String weather);
}
interface Addable{
    public int add(int a, int b);
}
public class LambdaQs{
    public void eat(Eatable e){
        System.out.println(e);
        e.taste();
    }
    public void drive(Flyable f){
        System.out.println("I'm drive: " + f);
        f.fly("[Blue sky is like the sunny day]");
    }
    public void test(Addable add){
        System.out.println("5 add 3 is: " + add.add(5, 3));
    }
    public static void main(String[] args){
        LambdaQs lq = new LambdaQs();
        lq.eat(() -> System.out.println("Apple tastes delicious."));
        lq.drive(weather -> {
            System.out.println("The weather is: " + weather);
            System.out.println("Helicopter flight stability.");
        });
        lq.test((a, b) -> a + b);
    }
}
