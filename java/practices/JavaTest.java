public class JavaTest{
    public static void main(String[] args){
        String numStr = "123.456";
        int lenStr = numStr.length();
        System.out.println("The str len is: " + lenStr);
        for(int i = 0; i < lenStr; i++){
            int num = numStr.charAt(i) - 48;
            System.out.println(num);
            System.out.println("\u5341\u4E07");
            if(i == lenStr - 1){
                System.out.println(i);
            }
        }
    }
}
