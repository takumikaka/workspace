public class ConstructorTest{
    public String name;
    public int num;

    public ConstructorTest(String name, int num){
        this.name = name;
        this.num = num;
    }

    public static void main(String[] args){
        ConstructorTest ct = new ConstructorTest("Hello Java", 117);
        System.out.println(ct.name);
        System.out.println(ct.num);
    }
}
