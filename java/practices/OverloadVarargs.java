public class OverloadVarargs{
    public void test(String msg){
        System.out.println("A test method with only one string parameter!");
    }
    public void test(String... books){
        System.out.println("****Test method with variable number of parameters!****");
    }

    public static void main(String[] args){
        OverloadVarargs olv = new OverloadVarargs();
        olv.test();
        olv.test("aaa", "bbb");
        olv.test("ccc");
        olv.test(new String[] {"ddd"});
    }
}
