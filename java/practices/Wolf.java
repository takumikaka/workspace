class Creature{
    public Creature(){
        System.out.println("Creature nonparametric constructor.");
    }
}

class Animal extends Creature{
    public Animal(String name){
        System.out.println("Animal with one parameter constructor. " + "Animal's name is: " + name);
    }
    public Animal(String name, int age){
        this(name);
        System.out.println("Animal with two parameter constructor. " + "Animal's age is: " + age);
    }
}

public class Wolf extends Animal{
    public Wolf(){
        super("wolf", 3);
        System.out.println("Wolf nonparametric constructor.");
    }

    public static void main(String[] args){
        new Wolf();
    }
}
