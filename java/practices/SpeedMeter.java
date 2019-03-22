public abstract class SpeedMeter{
    private double turnRate;
    public SpeedMeter(){

    }
    public void setTurnRate(double turnRate){
        this.turnRate = turnRate;
    }
    public abstract double getRadius();
    public double getSpeed(){
        return java.lang.Math.PI * 2 * getRadius() * turnRate;
    }
}
