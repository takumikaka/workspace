public class ConversionTest{
    public static void main(String[] args){
        double d = 13.4;
        long l = (long)d;
        System.out.println(l);

        Object obj = "Hello";
        String objstr = (String)obj;
        System.out.println(objstr);

        Object objPri = new Integer(5);
        if(objPri instanceof String){
            String str = (String)objPri;
            System.out.println(str);
        }
    }
}
