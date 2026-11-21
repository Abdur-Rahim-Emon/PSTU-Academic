
package W;
class c{
    int i;
    void getValue(int x){
        i=x;
    }
}
class d{
    int j;
    c c;
    d(int x,c c){
        this.c=c;
        j=x;
        
    }
    void display(){
        System.out.println("x = "+j+" y : "+c.i);
    }
}
public class B {
    
    
    public static void main(String[] args) {
        c c=new c();
        c.getValue(10);
        d d1=new d(10,c);
        d1.display();
        
    }
    
}
