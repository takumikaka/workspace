public enum Operation{
    PLUS{
        public double eval(double x, double y){
            return x + y;
        }
    },
    MINUS{
        public double eval(double x, double y){
            return x - y;
        }
    },
    TIMES{
        public double eval(double x, double y){
            return x * y;
        }
    },
    DIVIDE{
        public double eval(double x, double y){
            return x / y;
        }
    };
    public abstract double eval(double x, double y);
    public static void main(String[] args){
        System.out.println(Operation.PLUS.eval(1, 2));
        System.out.println(Operation.MINUS.eval(1, 2));
        System.out.println(Operation.TIMES.eval(1, 2));
        System.out.println(Operation.DIVIDE.eval(1, 2));
    }
}
