package practice;

public class OddOrEvenSwitch {

	public static void main(String[] args) {
		int num = (int) (Math.random() * 100) + 1;
		switch (num % 2) {
//			case 0 -> {
//				System.out.println(num + " : 짝수");
//			}
//			default -> {				
//				System.out.println(num + " : 홀수");
//			}
			case 0: 
				System.out.println(num + " : 짝수");
				break;
			default: 				
				System.out.println(num + " : 홀수");
						
		}

	}

}
