public class FinalVariableTest{
    final int a = 6;

    final String str;
    final int b;
    final static double d;

    {
        str = "Hello.";
    }
    static{
        d = 11.7;
    }
    public FinalVariableTest(){
        b = 9;
    }

    public static void main(String[] args){
        FinalVariableTest fat1 = new FinalVariableTest();
        FinalVariableTest fat2 = new FinalVariableTest();
        FinalVariableTest fat3 = new FinalVariableTest();
        FinalVariableTest fat4 = new FinalVariableTest();
        System.out.println(fat1.a);
        System.out.println(fat2.str);
        System.out.println(fat3.b);
        System.out.println(fat4.d);
    }

}
