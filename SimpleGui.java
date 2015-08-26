import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

/** 
 * Code adapted from Head First Java by Sierra and Bates
 */

public class SimpleGui implements ActionListener {
    public JButton button;

    public static void main(String[] args) {
        SimpleGui gui = new SimpleGui();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        button = new JButton("click me like you mean it");
        button.addActionListener(this);
        frame.getContentPane().add(BorderLayout.EAST, button);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent event) {
        button.setText("I've been clicked!");
    }
}