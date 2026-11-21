package PasswordField;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Test extends JFrame {
    Container c;
    JPasswordField jpf;
    Test(){
        initComponents();
    }
    void initComponents() {
        c=new Container();
        c = getContentPane();
        c.setLayout(null);
        jpf=new JPasswordField();
        jpf.setBounds(10, 10, 100, 50);
        jpf.setEchoChar('*');
        jpf.setBackground(Color.darkGray);
        jpf.setForeground(Color.white);
        c.add(jpf);
        jpf.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                String pwd=jpf.getText();
                JOptionPane.showMessageDialog(null,pwd);
            }
        });



    }
    public static void main(String[] args) {
        Test test = new Test();
        test.setVisible(true);
        test.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        test.setBounds(10, 30, 450, 500);
        test.setBackground(Color.cyan);

    }
}
