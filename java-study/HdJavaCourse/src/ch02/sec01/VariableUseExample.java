package ch02.sec01;

public class VariableUseExample {

	public static void main(String[] args) {
		int h = 3;
		int m = 5;
		System.out.println(h + "시간 " + m + "분");
		
		int total = h * 60 + m;
		System.out.println("총 " + total + "분");

	}

}
