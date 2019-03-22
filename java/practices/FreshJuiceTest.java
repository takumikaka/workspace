class FreshJuice{
    enum FreshjuiceSize { SMALL, MEDIL, LARGE }
    FreshjuiceSize size;
}

public class FreshJuiceTest {
    public static void main(String []args) {
        FreshJuice juice = new FreshJuice();
        juice.size = FreshJuice.FreshjuiceSize.SMALL;
    }
}
