package ch03.sec06;

public class CompareOperatorExample {

	public static void main(String[] args) {
		int n1 = 10;
		int n2 = 10;
		
		boolean res1 = (n1 == n2);
		boolean res2 = (n1 != n2);
		boolean res3 = (n1 <= n2);
		System.out.println(res1);
		System.out.println(res2);
		System.out.println(res3);
		
		char char1 = 'A';
		char char2 = 'B';
		boolean res4 = (char1 < char2);
		System.out.println(res4);
		
		int n3 = 1;
		double n4 = 1.0;
		boolean res5 = (n3 == n4);
		System.out.println(res5);
		
		float n5 = 0.1f;
		double n6 = 0.1;
		boolean res6 = (n5 == n6);
		boolean res7 = (n5 == (float) n6);
		System.out.println(res6);
		System.out.println(res7);
		
		String str1 = "자바";
		String str2 = "Java";
		boolean res8 = str1.equals(str2);
		boolean res9 = !str1.equals(str2);
		System.out.println(res8);
		System.out.println(res9);

	}

}
