import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
    
    //Variables    
    double x; //x side
    double y; //y side
    double z; //hypotenus

    Scanner scanner = new Scanner(System.in);

    //Input
    System.out.println("Enter side x: ");
    x = scanner.nextDouble();
    System.out.println("Enter side y: ");
    y = scanner.nextDouble();
    
    //Result
    z = Math.sqrt((x*x)+(y*y));
    System.out.println("The hypotenus is: "+z);

    scanner.close();


    }
}
