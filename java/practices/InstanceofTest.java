public class InstanceofTest{
    public static void main(String[] args){
        Object hello = "Hello";

        System.out.println("Whether a string is an instance of a object class. " + (hello instanceof Object));
        System.out.println("Whether a string is an instance of a string class. " + (hello instanceof String));
        System.out.println("Whether a string is an instance of a Math class. " + (hello instanceof Math));
        System.out.println("Whether a string is an instance of a comparable class. " + (hello instanceof Comparable));
        System.out.println("Whether a string is an instance of a object class. " + (hello instanceof Object));

        String a = "Hello";
        //System.out.println("Whether a string is an instance of a Math class. " + (a instanceof Math));
    }
}
