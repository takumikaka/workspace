public abstract class Shape{
    private String color;
    public abstract double callPerimeter();
    public abstract String getType();
    public Shape(String color){
        this.color = color;
    }
    public void setColor(String color){
        this.color = color;
    }
    public String getColor(){
        return color;
    }
}
