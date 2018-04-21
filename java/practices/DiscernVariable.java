public class DiscernVariable{
    private String prop = "Hello java from outClass.";
    private class InClass{
        private String prop = "Hello java from innerClass.";
        public void info(){
            String prop = "Hello java.";
            System.out.println(DiscernVariable.this.prop);
            System.out.println(this.prop);
            System.out.println(prop);
        }
    }
    public void test(){
        InClass ic = new InClass();
        ic.info();
    }
    public static void main(String[] args){
        DiscernVariable dv = new DiscernVariable();
        dv.test();
    }
}
