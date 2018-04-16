class Person{
    private String name;
    private String idstr;
    public Person(){
        this.name = "No name";
        this.idstr = "No ID";
    }
    public Person(String name, String idstr){
        this.name = name;
        this.idstr = idstr;
    }

    public String getName(){
        return this.name;
    }
    public String getIdstr(){
        return this.idstr;
    }

    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj != null && obj.getClass() == Person.class){
            Person personObj = (Person)obj;
            if(this.getIdstr().equals(personObj.getIdstr())){
                return true;
            }
        }
        return false;
        }
    }

public class OverrideEqualRight{
    public static void main(String[] args){
        Person p1 = new Person("Goku", "117");
        Person p2 = new Person("Saiya", "117");
        Person p3 = new Person("Jack", "007");
        System.out.println("p1 equal p2? " + p1.equals(p2));
        System.out.println("p1 equal p3? " + p1.equals(p3));
    }
}
