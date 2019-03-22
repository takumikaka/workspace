public class TestArrayTwo{
    public static void main(String[] args){
        double[] arrayList = {1.9, 2.1, 3.0, 4.5};

        for(int i = 0; i < arrayList.length; i++){
            System.out.println(arrayList[i]);
        }

        double total = 0;
        for(int i = 0; i < arrayList.length; i++){
            total = total + arrayList[i];
        }
        System.out.println("The total is:" + total);

        double max = arrayList[0];
        for(int i = 0; i < arrayList.length; i ++){
            if(arrayList[i] > max){
                max = arrayList[i];
            }
        }
        System.out.println("The max is:" + max);
    }
}
