
package Test;



public class w {
    public static void main(String[] args) {
       int first =0,secend=1;
       int i=0,sum=0;
       
      while(i!=7){
          if(i==0){
              System.out.println("0");
          }
          else if(i==1){
              System.out.println("1");
          }
          else{
          
          sum=first+secend;
              System.out.println(sum);
              first=secend;
              secend=sum;
          }
          
      }
    }   
}
