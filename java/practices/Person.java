public class Person{
    int broAge;
    public Person(String name){
        System.out.println("bro's name:" + name);
    }
    public void setAge(int age){
        broAge = age;
    }
    public int getAge(){
        System.out.println("bro's age:" + broAge);
        return broAge;
    }
    public static void main(String[] args){
        Person myperson = new Person("Luo shan jie");
        myperson.setAge(34);
        myperson.getAge();
        System.out.println("The value's:" + myperson.broAge);
    }
}
