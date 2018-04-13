class Animal{
    private void heart(){
        System.out.println("Heart beating...");
    }
    public void breath(){
        heart();
        System.out.println("Take a breath, Breathe a breath, breathing...");
    }
}

class Bird extends Animal{
    public void fly(){
        System.out.println("Free flying in the sky...");
    }
}

class Wolf extends Animal{
    public void run(){
        System.out.println("Free running on the ground...");
    }
}

public class InheritTest{
    public static void main(String[] args){
        Bird bird = new Bird();
        bird.breath();
        bird.fly();

        Wolf wolf = new Wolf();
        wolf.breath();
        wolf.run();
    }
}
