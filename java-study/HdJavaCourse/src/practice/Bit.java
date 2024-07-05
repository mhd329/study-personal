package practice;

public class Bit {

	public static void main(String[] args) {
		int a = 1073741824;
		int b = a << 1;
		String c = Integer.toBinaryString(b);
		if (c.charAt(0) == '1') {
			System.out.println("Overflow");
		}
		System.out.println(b);
		System.out.println(c);
		
	}

}
