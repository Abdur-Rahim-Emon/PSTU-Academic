
package W4;

public class Rectangle {
    double lenth;
    double brendth;
    Rectangle(double lenth,double brendth){
        this.lenth=lenth;
        this.brendth=brendth;
        
    }
    public void area(){
        System.out.println("area of reactangle  : "+(lenth*brendth));
        
    }
    public void perimeter(){
        System.out.println("peimeter of reactangle : "+(2*(lenth+brendth)));
        
    }
}
