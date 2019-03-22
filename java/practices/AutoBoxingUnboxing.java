public class AutoBoxingUnboxing{
    public static void main(String[] args){
        Integer inObj = 5;
        Object boolObj = true;
        int it = inObj;
        System.out.println("it value is: " + it);
        if(boolObj instanceof Boolean){
            Boolean b = (Boolean)boolObj;
            System.out.println("b value is: " + b);
        }
    }
}
