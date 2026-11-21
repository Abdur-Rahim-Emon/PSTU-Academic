
package JF;
import javax.swing.*;
import java.awt.*;

 class TwoPanelsExample {
    public static void main(String[] args) {
        // Create the main frame
        JFrame frame = new JFrame("Two JPanels Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Create the first panel with a red background
        JPanel panel1 = new JPanel();
        panel1.setBackground(Color.RED);
        panel1.setPreferredSize(new Dimension(200, 150));

        // Add a label to the first panel
        panel1.add(new JLabel("Panel 1"));

        // Create the second panel with a blue background
        JPanel panel2 = new JPanel();
        panel2.setBackground(Color.BLUE);
        panel2.setPreferredSize(new Dimension(200, 150));

        // Add a label to the second panel
        panel2.add(new JLabel("Panel 2"));

        // Add both panels to the frame using a layout
        frame.setLayout(new FlowLayout());
        frame.add(panel1);
        frame.add(panel2);

        // Make the frame visible
        frame.setVisible(true);
    }
}

