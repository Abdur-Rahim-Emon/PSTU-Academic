
package W7;


public class employee  extends person{
    void getEmployeeId(int id){
        System.out.println("employee Id: "+id);
    }
    
    @Override
   public  void getLastName(String name){
        System.out.println("Employee type  : "+name);
        
    }
    
}
