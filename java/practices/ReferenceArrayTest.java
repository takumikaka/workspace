class Person{
    public int age;
    public double height;
    public String name;
    public void info(){
        System.out.println(name + " age is: " + age);
        System.out.println(name + " height is: " + height + "cm");
    }
}

public class ReferenceArrayTest{
    public static void main(String[] args){
        Person[] students;
        students = new Person[2];
        Person Lou = new Person();
        Lou.name = "Lou";
        Lou.age = 32;
        Lou.height = 181;
        Person Liu = new Person();
        Liu.name = "Liu";
        Liu.age = 32;
        Liu.height = 182;
        students[0] = Lou;
        students[1] = Liu;
        Lou.info();
        Liu.info();
    }
}
