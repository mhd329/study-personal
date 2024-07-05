package classtest.calculator;

public class Calculator3 {
	public void none() {
		// 경고 없애기용
	}
	
	public static void plus(int val1, int val2) {
		int result = val1 + val2;
		System.out.println(result);
	}
	public static void minus(int val1, int val2) {
		int result = val1 - val2;
		System.out.println(result);
	}
	public static void multiply(int val1, int val2) {
		int result = val1 * val2;
		System.out.println(result);
	}
	public static void divide(int val1, int val2) {
		int result = val1 / val2;
		System.out.println(result);
	}
	public static void rest(int val1, int val2) {
		int result = val1 % val2;
		System.out.println(result);
	}
}
