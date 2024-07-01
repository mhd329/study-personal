package ch02.sec01;

public class VariableExchangeExample {

	public static void main(String[] args) {
		int x = 3;
		int y = 5;
		System.out.println("x: " + x + ", y: "  + y);
		
		y = swap(x, x = y);
		System.out.println("x: " + x + ", y: " + y);
		
	}
	
	public static int swap(int x, int y) {
		return x;
	}

}
