
package JF;

import java.awt.*;
import javax.swing.*;

public class JFrameTest extends JFrame {
 Container c;
 JLabel label1;
 JLabel label2;
 ImageIcon icon;
 JTextField textField;
    JFrameTest(){
        c=new Container();
icon=new ImageIcon("src/main/java/JF/download.png");
        addComponent();
    }
    void addComponent(){

        c=this.getContentPane();
        c.setLayout(null);
        c.setBackground(Color.CYAN);
        //making a jlabel
        label1=new JLabel();
        label1.setText("ARE : ");
        label1.setBounds(10, 10, 100, 20);
        label1.setOpaque(true);
        label1.setBackground(Color.BLACK);
        label1.setForeground(Color.RED);
        label1.setFont(new Font("Serif", Font.BOLD, 20));
        label1.setToolTipText("Hello World");
       String s= label1.getText();
        c.add(label1);
        System.out.println(s);

        // adding new photo
        label2 =new JLabel(icon);
        label2.setBounds(10, 50, icon.getIconWidth(), icon.getIconHeight());
        c.add(label2);
        // adding image to the location
        label2=new JLabel(icon);
        label2.setBounds(20+icon.getIconWidth(), 50, icon.getIconWidth(), icon.getIconHeight());
        c.add(label2);
        // jTextfield
        textField=new JTextField("abdur");
        textField.setBounds(130, 10,100, 20);
        c.add(textField);




    }

    public static void main(String[] args) {
        JFrameTest jf=new JFrameTest();
        jf=new JFrameTest();
        jf.setVisible(true);
        jf.setBackground(Color.yellow);
        jf.setBounds(50,100, 800,800);
        jf.setResizable(false);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
    
}
