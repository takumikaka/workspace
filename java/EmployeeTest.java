import java.io.*;

public class EmployeeTest{
    public static void main(String[] args){
        Employee empOne = new Employee("Luo shan jie");
        Employee empTwo = new Employee("Liu yi jun");

        empOne.empAge(32);
        empOne.empDesignation("Programer");
        empOne.empSalary(13200);
        empOne.printEmployee();

        empTwo.empAge(34);
        empTwo.empDesignation("Actor");
        empTwo.empSalary(13200);
        empTwo.printEmployee();

    }
}
