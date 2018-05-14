public class GenderBetterInterTest{
    public static void main(String[] args){
        GenderBetterInter gbi = GenderBetterInter.valueOf("Male");
        gbi.setName("Nan");
        gbi.info();
        System.out.println(gbi + " means: " + gbi.getName());
        gbi.setName("Nv");
    }
}
