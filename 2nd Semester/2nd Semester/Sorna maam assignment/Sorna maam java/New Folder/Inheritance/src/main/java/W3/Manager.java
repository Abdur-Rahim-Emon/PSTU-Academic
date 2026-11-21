
package W3;

public class Manager extends Member {
    String speciliztion;
     public void getValue1(String name,int age,String phonenumber,String address,double salary,String speciliztion){
        this.name=name;
        this.age=age;
        this.phonenumber=phonenumber;
        this.address=address;
        this.salary=salary;
        this.speciliztion=speciliztion;
        
    }
    public void show1(){
        System.out.println("Name : "+name);
        System.out.println("age ; "+age);
        System.out.println("phone number : "+ phonenumber);
        System.out.println("Address  : "+address );
        System.out.println("salary:  "+salary);
        System.out.println("respectivity : "+speciliztion);
        
    }
}
