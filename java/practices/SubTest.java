class Base{
    public Base(){
        test();
    }
    public void test(){
        System.out.println("The method of rewriting the quilt.");
    }
}

public class SubTest extends Base{
    private String name;
    public void test(String name){
        System.out.println("The method of subclass rewriting the parent class." + " name length is: " + name.length());
    }
    public static void main(String[] args){
        SubTest st = new SubTest();
        st.test("Hello Jave.");
    }
}
