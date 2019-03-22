class DataWrap{
    int a;
    int b;
}

public class ReferenceTransferTest{
    public static void swap(DataWrap dw){
        int tmp = dw.a;
        dw.a = dw.b;
        dw.b = tmp;
        System.out.println("In the swap method, the value of the a member variable: " + dw.a + " the value of the b member variable: " + dw.b);
    }

    public static void main(String[] args){
        DataWrap dw = new DataWrap();
        dw.a = 6;
        dw.b = 9;
        swap(dw);
        System.out.println("After the end of the exchange, the value of the a member variable: " + dw.a + " the value of the a member variable: " + dw.b);
    }
}
