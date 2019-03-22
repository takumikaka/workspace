/*
遗留问题：
1、中间两个零
2、最前面为零
3、最后面为零
*/
public class Num2Rmb{
    private String[] hanArr = {"\u96F6", "\u58F9", "\u8D30", "\u53C1", "\u8086", "\u4F0D", "\u9646", "\u67D2", "\u634C", "\u7396", "\u62FE"};
    private String[] zheng_unitArr = {"\u5341", "\u767E", "\u5343", "\u4E07", "\u5341", "\u767E", "\u5343", "\u4EBF"};
    private String[] xiao_unitArr = {"\u5206", "\u89D2"};
    private String zhengDivide(double num){
        long zheng = (long)num;
        String zheng_num = Long.toString(zheng);
        return zheng_num;
    }
    private String xiaoDivide(double num){
        long zheng = (long)num;
        long xiao = Math.round((num - zheng) * 100);
        String xiao_num = Long.toString(xiao);
        return xiao_num;
    }
    private String zhengToHanStr(String numStr){
        String result = "";
        int numLen = numStr.length();
        for(int i = 0; i < numLen; i++){
            int num = numStr.charAt(i) - 48;
            if(i != numLen - 1 && num != 0){
                result += hanArr[num] + zheng_unitArr[numLen - 2- i];
            }else{
                result += hanArr[num];
            }
        }
        return result;
    }
    private String xiaoToHanStr(String numStr){
        String result = "";
        int numLen = numStr.length();
        for(int i = 0; i < numLen; i++){
            int num = numStr.charAt(i) - 48;
            if(i != numLen - 1 && num != 0){
                result += hanArr[num] + xiao_unitArr[numLen - 1 - i];
            }else{
                result += hanArr[num];
            }
        }
        return result;
    }
    public static void main(String[] args){
        Num2Rmb nr = new Num2Rmb();
        //System.out.println(Arrays.toString(nr.divide(1234.56789)));
        String zheng_num = nr.zhengDivide(123.4567);
        String xiao_num = nr.xiaoDivide(123.4567);
        String zheng_han = nr.zhengToHanStr(zheng_num) + "\u5143";
        String xiao_han = nr.xiaoToHanStr(xiao_num) + "\u5206";
        System.out.println(zheng_han + xiao_han);
    }
}
