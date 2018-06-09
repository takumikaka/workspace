public class GcTest
{
    public static void main(String[] args)
    {
        for(int i = 1; i < 4; i++)
        {
            new GcTest();
            Runtime.getRuntime().gc();
        }
    }
    public void finalize()
    {
        System.out.println("The system is cleaning up the resources of the GcTest object...");
    }
}
