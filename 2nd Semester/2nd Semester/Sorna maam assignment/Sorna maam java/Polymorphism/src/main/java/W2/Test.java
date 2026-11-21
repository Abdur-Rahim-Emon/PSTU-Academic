
package W2;

import java.util.Scanner;


 class superclass {
   private int data1;
  
    superclass(int data1){//data 1 local 
        this.data1=data1;
      
    }
    void setdata1(int x){
        data1=x;
    }
   int  getdata1(){
       //System.out.println(data1);
       return data1;
   }   
}
class subclass extends superclass {
   private int data2;
    subclass(int x,int y){
        super(x);
        data2=y;
    }
    void setdata2(int y){
        data2=y;
    }
    int  getdata2(){
        //System.out.println("data1 is  : "+getdata1()+"\n"+"data2 is : "+data2);
        return data2;
    }
    public boolean cheeckCondition(){
        if( getdata1()==10 && data2==15){
            return true;
        }
       else
            return false;
    }
   
}


public class Test {
    public static void main(String[] args) {
        subclass dis=new subclass(10,15);
        System.out.println("data1 and data2 are equal : "+dis.cheeckCondition());
        System.out.println("data 1 : "+dis.getdata1());
        System.out.println("data 2 : "+dis.getdata2());
        
       dis.setdata1(30);
       dis.setdata2(40);
        System.out.println("after assigning data : ");
       System.out.println("data 1 : "+dis.getdata1());
        System.out.println("data 2 : "+dis.getdata2());
        System.out.println("data1 and data2 are equal : "+dis.cheeckCondition());
        Scanner in = new Scanner(System.in);
        int x,y;
         System.out.println("enter how many test case : ");
        int n=in.nextInt();
          for (int i = 0; i <n; i++) {
        System.out.println("enter data 1  : ");
        x=in.nextInt();

        System.out.println("enter data 2 ");
        y=in.nextInt();
        dis.setdata1(x);
       dis.setdata2(y);
        System.out.println("after assigning data : ");
       System.out.println("data 1 : "+dis.getdata1());
        System.out.println("data 2 : "+dis.getdata2());
        System.out.println("data1 and data2 are equal : "+dis.cheeckCondition());
        }
       
    }
}
