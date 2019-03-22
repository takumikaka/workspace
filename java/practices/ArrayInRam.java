public class ArrayInRam{
    public static void main(String[] args){
        int[] a = {1, 2, 3};
        int[] b = new int[4];
        System.out.println("b length is: " + b.length);
        for(int i = 0, len_a = a.length; i < len_a; i++){
            System.out.println("a[i] is: " + a[i]);
        }
        for(int j = 0, len_b = b.length; j < len_b; j++){
            System.out.println("b[i] is: " + b[j]);
        }
    }
}
