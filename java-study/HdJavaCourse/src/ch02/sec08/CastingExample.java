package ch02.sec08;

public class CastingExample {

	public static void main(String[] args) {
		int a = 10;
		byte b = (byte) a;
		System.out.println(b);
		
		long c = 300;
		int d = (int) c;
		System.out.println(d);
		
		int e = 65;
		char f = (char) e;
		System.out.println(f);
		
		double g = 3.14;
		int h = (int) g;
		System.out.println(h);

	}

}
