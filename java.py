import streamlit as st


def main():
	
	st.write("file opening Swing")
	st.code("""import java.awt.*;
import java.applet.*;
import java.awt.event.*;
import javax.swing.*;

/* <applet code = "SwingExample" width = 300 height = 300>
   <param name = width value = 200>
   <param name = height value = 200>
</applet> */

public class SwingExample extends JApplet implements ActionListener {
    JFrame f;
    JTextArea text;
    JMenuBar mBar;
    JMenu file;
    JMenuItem menuItem1, menuItem2;
    Container c;

    public void init() {
        int width = Integer.parseInt(getParameter("width"));
        int height = Integer.parseInt(getParameter("height"));

        f = new JFrame("Menu Demo");
        f.setSize(width, height);
        c = f.getContentPane();
        text = new JTextArea("", 80, 40);
        c.add(text);

        mBar = new JMenuBar();
        setJMenuBar(mBar);
        file = new JMenu("file");
        mBar.add(file);

        menuItem1 = new JMenuItem("new");
        file.add(menuItem1);
        menuItem1.addActionListener(this);

        menuItem2 = new JMenuItem("open");
        file.add(menuItem2);
        menuItem2.addActionListener(this);

        f.setVisible(true);
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == menuItem1) {
            text.append("File -> New option selected\n");
        }
        if (ae.getSource() == menuItem2) {
            text.append("File -> Open option selected\n");
        }
    }

	}""")
	st.write("EX1 swing")
	st.code("""// Program to illustrate RadioButton control
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/* <applet code ="SwingExample" width = 400 height = 300 ></applet> */

public class SwingExample extends JApplet implements ActionListener {
    JTextField jtf;
    ImageIcon normalIcon, rolloverIcon, selectedIcon;
    JRadioButton rb1, rb2;
    ButtonGroup bg;
    Container c;

    public void init() {
        c = getContentPane();
        c.setLayout(new FlowLayout());

        normalIcon = new ImageIcon("web.gif");
        rolloverIcon = new ImageIcon("mmc.gif");
        selectedIcon = new ImageIcon("help.gif");

        rb1 = new JRadioButton("Idly", normalIcon);
        rb1.setRolloverIcon(rolloverIcon);
        rb1.setSelectedIcon(selectedIcon);
        rb1.addActionListener(this);
        c.add(rb1);

        rb2 = new JRadioButton("Dosa", normalIcon);
        rb2.setRolloverIcon(rolloverIcon);
        rb2.setSelectedIcon(selectedIcon);
        rb2.addActionListener(this);
        c.add(rb2);

        bg = new ButtonGroup();
        bg.add(rb1);
        bg.add(rb2);

        jtf = new JTextField(5);
        c.add(jtf);
    }

    public void actionPerformed(ActionEvent ae) {
        String caption = ae.getActionCommand();
        jtf.setText(caption);
    }
	}""")