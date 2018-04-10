public class SubStringByBytes{
    public static String subStringByBytes(String str, int end){
        if(str.length() * 2 < end){
            return str;
        }

        char[] chArr = str.toCharArray();

        int lenByte = 0;
        for(int i = 0; i < chArr.length; i++){
            if(chArr[i] > 255){
                lenByte += 2;
            }else{
                ++lenByte;
            }
            if(lenByte >= end){
                if(lenByte == end){
                    return str.substring(0,i);
                }
                return str.substring(0,i - 1);
            }
        }
        return str;
    }

    public static void main(String[] args){
        System.out.println(subStringByBytes("abcdefg", 3));
    }
}
