
package W4;

public class Square extends Rectangle {
    double r;
  Square(double x,double y,double r){
      super(x,y);
      this.r=r;
  }
  void sarea(){
      System.out.println("sqare area : "+(r*r));
  }
    
    
    
}
