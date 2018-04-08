public class Num2Rmb{
    private String[] hanArr = {"\u96F6", "\u58F9", "\u8D30", "\u53C1", "\u8086", "\u4F0D", "\u9646", "\u67D2", "\u634C", "\u7396", "\u62FE"};
    private String[] unitArr = {"\u5341", "\u767E", "\u5343", "\u4E07", "\u4EBF"};
    private String[] divide(double num){
        long zheng = (long)num;
        long xiao = Math.round((num - zheng) * 100);
        return new String[]{zheng + "", String.valueOf(xiao)};
    }
    private String toHanStr(String numStr){
        String result = "";
        int numLen = numStr.length();
        for(int i = 0; i < numLen; i++){
            int num = numStr.charAt(i) - 48;
            if(i != numLen - 1 && num != 0){
                result += hanArr[num] + unitArr[numLen - 2- i];
            }else{
                result += hanArr[num];
            }
        }
        return result;
    }
    public static void main(String[] args){
        Num2Rmb nr = new Num2Rmb();
        //System.out.println(Arrays.toString(nr.divide(1234.56789)));
        System.out.println(nr.toHanStr("123456") + "\u5143");
    }
}
