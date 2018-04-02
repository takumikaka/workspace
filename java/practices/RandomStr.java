public class RandomStr{
    public static void main(String[] args){
        String result = "";
        for(int i = 0; i < 6; i++){
            int randomValue = (int)(Math.random() * 25 + 97);
            result = result + (char)randomValue;

            double testRandom = Math.random();
            System.out.println(testRandom);
        }
        System.out.println(result);
    }
}
