public class NarrowConversion{
    public static void main(String[] args){
        int iValue = 117;
        byte bValue = (byte)iValue;
        System.out.println(bValue);

        double dValue = 1.314;
        int tol = (int)dValue;
        System.out.println(tol);
    }
}
