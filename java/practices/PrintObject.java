class Person{
    private String name;
    public Person(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
}

public class PrintObject{
    public static void main(String[] args){
        Person p = new Person("Goku");
        //System.out.println(p.toString());
        System.out.println(p.getName());
    }
}
