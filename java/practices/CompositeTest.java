class Animal{
    private void heart(){
        System.out.println("Heart beating...");
    }
    public void breath(){
        heart();
        System.out.println("Take a breath, Breathe a breath, breathing...");
    }
}

class Bird{
    private Animal a;
    public Bird(Animal a){
        this.a = a;
    }
    public void breath(){
        a.breath();
    }
    public void fly(){
        System.out.println("Free flying in the sky...");
    }
}

class Wolf{
    private Animal a;
    public Wolf(Animal a){
        this.a = a;
    }
    public void breath(){
        a.breath();
    }
    public void run(){
        System.out.println("Free running on the ground...");
    }
}

public class CompositeTest{
    public static void main(String[] args){
        Animal a1 = new Animal();
        Bird bird = new Bird(a1);
        bird.breath();
        bird.fly();

        Animal a2 = new Animal();
        Wolf wolf = new Wolf(a2);
        wolf.breath();
        wolf.run();
    }
}
