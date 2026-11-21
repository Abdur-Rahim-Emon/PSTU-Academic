package ActionLisener;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Tes extends JFrame {
    Container c;
   // ImageIcon icon;
    JLabel l;
    JTextField tf;
    Tes(){
        initComponents();

    }
    void initComponents() {
        c=new Container();
        c=this.getContentPane();
        c.setLayout(null);

        c.setBackground(Color.cyan);
        Font f=new Font("Serif",Font.BOLD,20);
        l=new JLabel("Are : ");
        l.setBounds(10,20,50,40);
        l.setFont(f);
        c.add(l);
        tf=new JTextField();
        tf.setBounds(60,20,100,40);
        tf.setFont(f);
        c.add(tf);
        tf.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                String s=tf.getText();
                if(s.isEmpty()){
                    JOptionPane.showMessageDialog(null,"Please enter a number","Error",JOptionPane.ERROR_MESSAGE);
                }
                else{
                    JOptionPane.showMessageDialog(null,s,"Error",2);
                }
            }
        }
        );

    }
    public static void main(String[] args) {
        Tes t = new Tes();
        t.setVisible(true);
        t.setBounds(100, 100, 650, 500);
        t.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        t.setResizable(false);
        t.setTitle("ActionLisener");
        ImageIcon icon=new ImageIcon("src/main/java/ActionLisener/IMG_20210824_223735.jpg");
        t.setIconImage(icon.getImage());
        t.setTitle("ActionLisener");
    }
}
