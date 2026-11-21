
package W8;


public class Circle extends shape{
    @Override
    public void getPerimeter(double r){
        System.out.println("perimeter : "+(2*Math.PI*r));
        
    }
    @Override
    public void getArea(double r){
        
        System.out.println("area : "+(Math.PI*r*r));
    }
  
    
}
