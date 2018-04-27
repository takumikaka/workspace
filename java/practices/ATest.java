interface A{
    public void test();
}
public class ATest{
    public static void main(String[] args){
        int age = 9;
        A a = new A()
        {
            public void test(){
                System.out.println(age);
            }
        };
        a.test();
    }
}
