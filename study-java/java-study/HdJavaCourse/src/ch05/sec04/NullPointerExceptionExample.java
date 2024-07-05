package ch05.sec04;

public class NullPointerExceptionExample {

	public static void main(String[] args) {
//		int[] intArr = null;
		int[] intArr = {1, 2, 3};
		intArr[0] = 10;
		
//		String str = null;
		String str = "abcde";
		System.out.println(str.length());

	}

}
