package algoritmische_mathe.Praktika.Praktikum1.Aufgabe3;

import java.util.Scanner;

public class MinMax {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();

        if (a > b) {
            System.out.println(a);
        } else {
            System.out.println(b);
        }

    }
}
