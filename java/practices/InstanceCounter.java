public class InstanceCounter{
    private static int numInstance = 0;
    protected static int getInstances(){
        return numInstance;
    }
    private static void addInstances(){
        numInstance++;
    }
    InstanceCounter(){
        InstanceCounter.addInstances();
    }
    public static void main(String[] args){
        System.out.println("Starting with " + InstanceCounter.getInstances() + " Instances");
        for(int i = 0; i < 500; i++){
            new InstanceCounter();
        }
        System.out.println("Counter " + InstanceCounter.getInstances() + " Instances");
    }
}
