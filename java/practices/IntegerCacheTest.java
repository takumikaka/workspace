public class IntegerCacheTest{
    public static void main(String[] args){
        Integer int1 = new Integer(9);
        Integer int2 = Integer.valueOf(9);
        Integer int3 = Integer.valueOf(9);
        System.out.println(int1 == int2);
        System.out.println(int2 == int3);

        Integer int4 = Integer.valueOf(200);
        Integer int5 = Integer.valueOf(200);
        System.out.println(int4 == int5);
    }
}
