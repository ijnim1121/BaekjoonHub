import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int A = scanner.nextInt();
        int B = scanner.nextInt();

        System.out.println(A + B);  // 덧셈
        System.out.println(A - B);  // 뺄셈
        System.out.println(A * B);  // 곱셈
        System.out.println(A / B);  // 나눗셈
        System.out.println(A % B);  // 나머지

        scanner.close();
    }
}
