
package Test;

import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class w1 extends JFrame{
    Container c;
    JLabel jl;
    JTextField jt;
    ImageIcon img;
    Font f;
    w1(){
        i();
    }
    void i(){
        c=new Container();
        c=this.getContentPane();
        c.setLayout(null);
        c.setBackground(Color.red);
        // create font object 
        f=new Font("Arial",Font.ITALIC,15);
        img=new ImageIcon("F:\\Sorna maam java\\Inheritance1\\src\\main\\java\\Test\\2659360.png");
        //c.add(.getImage());
        this.setIconImage(img.getImage());
        // adding textLabel 
        jl=new JLabel("enter your information");
        jl.setBounds(50,10,250,10);
        jl.setFont(f);
        c.add(jl);
        jl=new JLabel("enter your name ");
        jl.setBounds(10,30,100,20);
        jl.setForeground(Color.black);
        jl.setOpaque(true);
        jl.setBackground(Color.YELLOW);
       jl.setToolTipText("name");
        c.setFont(f);
        c.add(jl);
        jt=new JTextField();
        jt.setBounds(120,30,100,20);
        jt.setFont(f);
        c.add(jt);
        
        
    }
    
    
    public static void main(String[] args) {
        w1 jf=new w1();
        jf.setVisible(true);
        jf.setBounds(300,300,400,450);
        jf.setResizable(false);
        
        
        
    }
   
}
