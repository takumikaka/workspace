public class LocalInnerClass{
    public static void main(String[] args){
        class InnerBase{
            int a;
        }
        class InnerSub extends InnerBase{
            int b;
        }
        InnerSub is = new InnerSub();
        is.a = 5;
        is.b = 6;
        System.out.println(is.a + is.b);
    }
}
