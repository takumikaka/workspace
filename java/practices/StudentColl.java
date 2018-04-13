public class StudentColl{
    public Student[] students;
    public StudentColl(){
        students = new Student[3];

        Student stu1 = new Student();
        stu1.setName("Ding yunlong");
        stu1.setEmail("ding@163.com");
        stu1.setAddress("1st dulituan street");

        Student stu2 = new Student();
        stu2.setName("Aqiang");
        stu2.setEmail("qiang@163.com");
        stu2.setAddress("2sd dog street");

        Student stu3 = new Student();
        stu3.setName("Luo shanjie");
        stu3.setEmail("Luo@163.com");
        stu3.setAddress("3th montinpig street");
        setStudent(stu1, stu2, stu3);
    }

    public void setStudent(Student stu1, Student stu2, Student stu3){
        students[0] = stu1;
        students[1] = stu2;
        students[2] = stu3;
    }

    public void getStudent(String str){
        int flagFind = 0;
        for(int i = 0; i < students.length; i++){
            Student stu = students[i];
            if(str.equals(stu.getName()) || str.equals(stu.getEmail()) || str.equals(stu.getAddress())){
                System.out.println("you find one student: " + stu.getName());
                flagFind++;
            }
        }

        if(flagFind == 0){
            System.out.println("the student didn't exist!");
        }
    }

    public static void main(String[] args){
        StudentColl stc = new StudentColl();
        stc.getStudent("Aqiang");
    }
}
