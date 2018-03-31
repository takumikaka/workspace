public class Puppy{
    int puppyAge;
    public Puppy(String name){
        System.out.println("Puppy's name:" + name);
    }
    public void setAge(int age){
        puppyAge = age;
    }
    public int getAge(){
        System.out.println("Puppy's age:" + puppyAge);
        return puppyAge;
    }
    public static void main(String[] args){
        Puppy mypuppy = new Puppy("Tommy");
        mypuppy.setAge(2);
        mypuppy.getAge();
        System.out.println("value:" + mypuppy.puppyAge);
    }
}
