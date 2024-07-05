package ch04.sec02;

public class IfDiceExample {

	public static void main(String[] args) {
		int[] numArray = new int[6];
		
		for (int i = 0; i < 6; i ++) {
			numArray[i] = i + 1;
		}

		int num = (int)(Math.random()*6) + 1;
		for (int i: numArray) {
			if (i == num) {				
				System.out.println(i + "번이 나왔습니다.");
			}
		}
		
	}

}
