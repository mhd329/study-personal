package practice;

public class OddOrEven {

	public static void main(String[] args) {
		int num = (int) (Math.random() * 100) + 1;
		
		if (num % 2 > 0) {
			System.out.println(num + " : 홀수");
		} else {
			System.out.println(num + " : 짝수");
		}

	}

}
