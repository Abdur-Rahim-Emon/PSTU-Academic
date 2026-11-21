
package W3;


public class Employee extends Member{
    //String specilaization;
    String department;
    public void getValue(String name,int age,String phonenumber,String address,double salary,String department){
        this.name=name;
        this.age=age;
        this.phonenumber=phonenumber;
        this.address=address;
        this.salary=salary;
        this.department=department;
        
    }
    public void show(){
        System.out.println("Name : "+name);
        System.out.println("age ; "+age);
        System.out.println("phone number : "+ phonenumber);
        System.out.println("Address  : "+address );
        System.out.println("salary:  "+salary);
        System.out.println("respectivity : "+department);
        
    }
}
