public class PupTest{
    public void pupAge(){
        int age = 0;
        age = age + 9;
        System.out.println("Puppy's age:" + age);
    }
    public static void main(String[] args){
        PupTest puppy = new PupTest();
        puppy.pupAge();
    }
}
