import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 두 문자열 입력 받기
        String str1 = scanner.nextLine();
        String str2 = scanner.nextLine();
        
        // 각 문자열의 알파벳 빈도 수를 저장할 배열
        int[] count1 = new int[26]; // str1의 알파벳 빈도
        int[] count2 = new int[26]; // str2의 알파벳 빈도

        // str1에서 각 알파벳 빈도 계산
        for (char c : str1.toCharArray()) {
            count1[c - 'a']++;
        }

        // str2에서 각 알파벳 빈도 계산
        for (char c : str2.toCharArray()) {
            count2[c - 'a']++;
        }

        // 두 문자열의 빈도 차이를 계산하여 제거해야 하는 문자 수 구하기
        int removeCount = 0;
        for (int i = 0; i < 26; i++) {
            removeCount += Math.abs(count1[i] - count2[i]);
        }

        // 결과 출력
        System.out.println(removeCount);

        scanner.close();
    }
}
