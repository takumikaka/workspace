class Person{
    public String name;
    public static int eyesNum;
}
public class PersonTestTwo{
    public static void main(String[] args){
        System.out.println("EyesNum class variable values of Person: " + Person.eyesNum);

        Person p = new Person();
        System.out.println("The value of the name variable of the P variable: " + p.name + " The value of the eyesNum variable of the P variable: " + p.eyesNum);
        p.name = "Gonku";
        p.eyesNum = 2;
        System.out.println("The value of the name variable of the P variable: " + p.name + " The value of the eyesNum variable of the P variable: " + p.eyesNum);

        System.out.println("EyesNum class variable values of Person: " + Person.eyesNum);

        Person p2 = new Person();
        System.out.println("EyesNum class variable values of p2: " + p2.eyesNum);
    }
}
