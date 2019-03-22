public class Outer{
    private int outProp = -9;
    class Inner{
        private int outProp = -5;
        public void accessOuterProp(){
             System.out.println("outProp of outClass: " + Outer.this.outProp);
        }
    }
    public void accessInnerProp(){
        System.out.println("outProp of innerClass: " + new Inner().outProp);
        new Inner().accessOuterProp();
    }
    public static void main(String[] args){
        Outer o = new Outer();
        o.accessInnerProp();
    }
}
