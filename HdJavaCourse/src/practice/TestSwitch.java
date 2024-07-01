package practice;

public class TestSwitch {

	public static void main(String[] args) {
		int k = 88;
		int e = 92;
		int m = 100;
		int sum = k + e + m;
		int avg = sum / 3;
		int res = avg / 10;
		
		switch (res) {
			case 9 -> {
				System.out.println("A");
				System.out.println(avg);
			}
			case 8 -> {
				System.out.println("B");
				System.out.println(avg);
			}
			case 7 -> {
				System.out.println("C");
				System.out.println(avg);
			}
			default -> {
				System.out.println("D");
				System.out.println(avg);
			}

		}

	}

}
