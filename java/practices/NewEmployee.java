import java.io.*;

public class NewEmployee{
    public String name;
    private double salary;
    private String designation;
    public NewEmployee(String empName){
        name = empName;
    }
    public void empSalary(double empSal){
        salary = empSal;
    }
    public void empDesig(String empDesig){
        designation = empDesig;
    }
    public void printEmp(){
        System.out.println("name:" + name);
        System.out.println("salary:" + salary);
        System.out.println("designation:" + designation);
    }
    public static void main(String[] args){
        NewEmployee empOne = new NewEmployee("Luo shanjie");
        empOne.empSalary(12000);
        empOne.empDesig("Programer");
        empOne.printEmp();

        NewEmployee empTwo = new NewEmployee("Liu yijun");
        empTwo.empSalary(12000);
        empTwo.empDesig("Actor");
        empTwo.printEmp();
    }
}
