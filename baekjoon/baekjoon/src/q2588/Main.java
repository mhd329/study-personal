package q2588;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		sc.close();
		int x = Integer.parseInt(a);
		int y = Integer.parseInt(b);
		StringBuffer sb = new StringBuffer(b);
		b = sb.reverse().toString();
		
		for (int i = 0; i < 3; i++) {
			int s = Integer.parseInt(a);
			char c = b.charAt(i);
			int j = c - '0';
			int res = s * j;
			System.out.println(res);
		}
		
		System.out.println(x * y);
		
	}

}
