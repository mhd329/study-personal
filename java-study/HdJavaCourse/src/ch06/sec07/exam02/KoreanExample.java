package ch06.sec07.exam02;

public class KoreanExample {

	public static void main(String[] args) {
		Korean k1 = new Korean("박자바", "011225-1234567");
		System.out.println(k1.getNation());
		System.out.println(k1.getName());
		System.out.println(k1.getSsn());
		System.out.println();
		
		Korean k2 = new Korean("김자바", "930525-0654321");
		System.out.println(k2.getNation());
		System.out.println(k2.getName());
		System.out.println(k2.getSsn());

	}

}
