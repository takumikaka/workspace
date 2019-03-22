class Name{
    private String firstName;
    private String lastName;
    public Name(){}
    public Name(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    public void setFirstName(String firstName){
        this.firstName = firstName;
    }
    public String getFirstName(){
        return this.firstName;
    }
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    public String getLastName(){
        return this.lastName;
    }
}

public class PersonAnotherTest{
    private final Name name;
    public PersonAnotherTest(Name name){
        this.name = new Name(name.getFirstName(), name.getLastName());
    }
    public Name getPersonName(){
        return new Name(name.getFirstName(), name.getLastName());
    }
    public static void main(String[] args){
        Name n = new Name("Goku", "Son");
        PersonAnotherTest person = new PersonAnotherTest(n);
        System.out.println(person.getPersonName().getFirstName());
        n.setFirstName("Gohan");
        System.out.println(person.getPersonName().getFirstName());
    }
}
