package algoritmische_mathe.Praktika.Praktikum1.Aufgabe2;

import java.util.Scanner;

public class EingabeAusgabe {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Geben Sie zwei ganze Zahlen ein");

        int a = sc.nextInt();
        int b = sc.nextInt();

        int summe = a + b;
        int produkt = a * b;

        System.out.println("Die summe beider Zahlen lautet " + summe);
        System.out.println("Die summe beider Zahlen lautet " + (a * b));

    }

}