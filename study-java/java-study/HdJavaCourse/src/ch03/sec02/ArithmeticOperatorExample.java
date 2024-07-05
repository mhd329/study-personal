package ch03.sec02;

public class ArithmeticOperatorExample {

	public static void main(String[] args) {
		byte v1 = 10;
		byte v2 = 4;
//		int v3 = 5;
		long v4 = 10L;
		
		int res1 = v1 + v2;
		System.out.println(res1);
		
		long res2 = v1 + v2 + v4;
		System.out.println(res2);
		
		double res3 = (double) v1 / v2;
		System.out.println(res3);
		
		int res4 = v1 % v2;
		System.out.println(res4);

	}

}
