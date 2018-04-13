class Student{
    public String name;
    public int age;
    public String gender;
    public String phone;
    public String address;
    public String email;

    public Student(){
        this.name = "Nobody";
        this.age = 0;
        this.gender = "Male";
        this.phone = "10086";
        this.address = "address";
        this.email = "admin@163.com";
    }
    public Student(String name, int age, String gender, String phone, String address, String email){
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.phone = phone;
        this.address = address;
        this.email = email;
    }

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        //System.out.println("name is: " + name);
        return this.name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        //System.out.println("age is: " + age);
        return this.age;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public String getGender(){
        //System.out.println("gender is: " + gender);
        return this.gender;
    }
    public void setPhone(String phone){
        this.phone = phone;
    }
    public String getPhone(){
        //System.out.println("phone is: " + phone);
        return this.phone;
    }
    public void setAddress(String address){
        this.address = address;
    }
    public String getAddress(){
        //System.out.println("address is: " + address);
        return this.address;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public String getEmail(){
        //System.out.println("email is: " + email);
        return this.email;
    }

    public void eat(){
        System.out.println("eat...eat...");
    }
    public void drink(){
        System.out.println("drink...drink...");
    }
    public void play(){
        System.out.println("play...play...");
    }
    public void sleep(){
        System.out.println("sleep...sleep...");
    }

}
