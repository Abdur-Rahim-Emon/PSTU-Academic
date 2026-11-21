
package W;
class B{
    int x=10;
    String un="Pstu";
}
public class A {
    B dis;
    String name;
    void getInfo(String name,B dis){
        this.name=name;
        this.dis=dis;
    }
    
    void show(){
        System.out.println("class A ");
    }
    public static void main(String[] args) {
        
       A d=new A();
       d.show();
       
        
    }
    
}
