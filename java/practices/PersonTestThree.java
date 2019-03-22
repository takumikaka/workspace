public class PersonTestThree{
    public static void main(String[] args){
        PersonThree pt = new PersonThree();
        //pt.age = 1000;
        pt.setAge(1000);
        System.out.println("When the member variables of the setAge are not set: " + pt.getAge());
        pt.setAge(6);
        System.out.println(pt.getAge());
        pt.setName("Lou");
        System.out.println(pt.getName());
    }
}
