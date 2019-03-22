public class Primitive2String{
    public static void main(String[] args){

        String intStr = "117";
        int it1 = Integer.parseInt(intStr);
        int it2 = new Integer(intStr);
        System.out.println("it1 is: " + it1);
        System.out.println("it2 is: " + it2);

        String floatStr = "1.234";
        float fs1 = Float.parseFloat(floatStr);
        float fs2 = new Float(floatStr);
        System.out.println("fs1 is: " + fs1);
        System.out.println("fs2 is: " + fs2);

        String ftStr = String.valueOf("1.234f");
        System.out.println("float to String: " + ftStr);

        String dbStr = String.valueOf("1.234");
        System.out.println("double to String: " + dbStr);

        String boolStr = String.valueOf("true");
        System.out.println("boolean to String: " + boolStr);
    }
}
