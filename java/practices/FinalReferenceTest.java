import java.util.Arrays;

class Person{
    private int age;
    public Person(){
        this.age = 0;
    }
    public Person(int age){
        this.age = age;
    }

    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        return this.age;
    }
}

public class FinalReferenceTest{
    public static void main(String[] args){
        final int[] iArr = {11, 7, 4, 5};
        System.out.println(Arrays.toString(iArr));
        Arrays.sort(iArr);
        System.out.println(Arrays.toString(iArr));
        iArr[2] = -8;
        System.out.println(Arrays.toString(iArr));
        final Person p = new Person(45);
        System.out.println(p.getAge());
        p.setAge(4);
        System.out.println(p.getAge());
    }

}
