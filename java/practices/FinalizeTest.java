public class FinalizeTest
{
    private static FinalizeTest ft = null;
    public void info()
    {
        System.out.println("Finalize method for testing resource cleaning");
    }
    public static void main(String[] args) throws Exception
    {
        new FinalizeTest();
        System.gc();
        System.runFinalization();
        ft.info();
    }
    public void finalize()
    {
        ft = this;
    }
}
