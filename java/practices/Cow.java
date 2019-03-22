public class Cow{
    private double weight;
    public Cow(){}
    public Cow(double weight){
        this.weight = weight;
    }
    private class CowLeg{
        private double length;
        private String color;
        public CowLeg(){}
        public CowLeg(double length, String color){
            this.length = length;
            this.color = color;
        }
        public void setLength(double length){
            this.length = length;
        }
        public double getLength(){
            return length;
        }
        public void setColor(String color){
            this.color = color;
        }
        public String color(){
            return color;
        }
        public void info(){
            System.out.println("The color of cow'leg is: " + color + ". The length of cow's leg is: " + length);
            System.out.println("The weight of cow is: " + weight);
        }
    }
    public void test(){
        CowLeg cl = new CowLeg(1.7, "Write");
        cl.info();
    }
    public static void main(String[] args){
        Cow c = new Cow(123.4);
        c.test();
    }
}
