class Address{
    private final String detail;
    private final String postCode;
    public Address(){
        this.detail = "";
        this.postCode = "";
    }
    public Address(String detail, String postCode){
        this.detail = detail;
        this.postCode = postCode;
    }

    public String getDetail(){
        return this.detail;
    }
    public String getPostCode(){
        return this.postCode;
    }

    public boolean equal(Object obj){
        if(this == obj){
            return true;
        }
        if(obj != null && obj.getClass() == Address.class){
            Address ad = (Address)obj;
            if(this.getDetail().equals(ad.getDetail()) && this.getPostCode().equals(ad.getPostCode())){
                return true;
            }
        }
        return false;
    }
}

public class AddressTest{
    public static void main(String[] args){
        Address ad1 = new Address("1st street", "10086");
        Address ad2 = new Address("1st street", "10086");
        System.out.println(ad1.equal(ad2));
    }
}
