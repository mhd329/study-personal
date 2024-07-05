package ch02.sec10;

public class PrimitiveAndStringConversationExample {

	public static void main(String[] args) {
		int a = Integer.parseInt("10");
		double b = Double.parseDouble("3.14");
		boolean c1 = Boolean.parseBoolean("true");
		boolean c2 = Boolean.parseBoolean("True");
		
		System.out.println(a);
		System.out.println(b);
		System.out.println(c1);
		System.out.println(c2);
		
		String d = String.valueOf(10);
		String e = String.valueOf(3.14);
		String f = String.valueOf(true);
		
		System.out.println(d);
		System.out.println(e);
		System.out.println(f);

	}

}
