public class TestArray{
    public static void main(String[] args){
        int size = 10;
        double[] arrayList = new double[size];

        arrayList[0] = 1;
        arrayList[1] = 2;
        arrayList[2] = 3;
        arrayList[3] = 4;
        arrayList[4] = 5;
        arrayList[5] = 6;
        arrayList[6] = 7;
        arrayList[7] = 8;
        arrayList[8] = 9;

        double total = 0;
        for(int i = 0; i < size; i++){
            total = total + arrayList[i];
        }
        System.out.println(total);
    }
}
