@FunctionalInterface
interface Mytest{
    String test(String a, int b, int c);
}

public class MethodRefer2{
    public static void main(String[] args){
        Mytest mt = (a, b, c) -> a.substring(b, c);
        String str = mt.test("I Love Python", 2, 8);
        System.out.println(str);
    }
}
