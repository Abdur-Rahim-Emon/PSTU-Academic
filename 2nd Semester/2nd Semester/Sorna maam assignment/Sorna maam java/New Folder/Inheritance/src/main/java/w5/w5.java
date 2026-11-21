
package w5;

class square{
    int i;
    int  show(int i)
    {
        
    this.i=i;
    return i*i;
    
    }
    
    
   
}
public class w5 {
    public static void main(String[] args) {
        square[] dis=new square[5];
        for (int i = 0; i <dis.length; i++) {
             dis[i]=new square();
        }
        for (int i = 0; i <dis.length; i++) {
            System.out.println(dis[i].show(i));
        }
       
    }
}
