import javax.swing.JOptionPane;

public class Main {
    
    public static void main(String[] args) {
        //Input for name
        String name = JOptionPane.showInputDialog("Enter your Name");
        JOptionPane.showMessageDialog(null, "Hello "+name);
    
        //Input for age
        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your Age"));
        JOptionPane.showMessageDialog(null, "You are "+age+" years old");

        //Input for Height
        Double Height = Double.parseDouble(JOptionPane.showInputDialog("Enter your Height"));
        JOptionPane.showMessageDialog(null, "Your Height is "+Height );

    }
}
