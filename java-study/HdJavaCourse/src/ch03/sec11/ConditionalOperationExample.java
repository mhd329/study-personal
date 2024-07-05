package ch03.sec11;

public class ConditionalOperationExample {

	public static void main(String[] args) {
		int s = 85;
		char g = (s > 90) ? 'A' : ((s > 80) ? 'B' : 'C');
		System.out.println(s + " : " + g);

	}

}
