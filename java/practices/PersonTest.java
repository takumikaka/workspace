public class PersonTest{
    public String name;
    public int age;
    public void say(String content){
        System.out.println(content);
    }

    public static void main(String[] args){
        PersonTest p = new PersonTest();
        p.name = "Luo";
        p.age = 45;
        System.out.println(p.name);
        System.out.println(p.age);
        p.say("Hello java!");

    }
}
