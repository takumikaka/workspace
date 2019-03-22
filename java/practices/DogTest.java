public class DogTest{
    public void jump(){
        System.out.println("The jump method is being executed..");
    }
    public void run(){
        this.jump();
        System.out.println("The run method is being executed..");
    }

    public static void main(String[] args){
        DogTest dog = new DogTest();
        dog.run();
    }
}
