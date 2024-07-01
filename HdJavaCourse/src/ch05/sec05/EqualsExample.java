package ch05.sec05;

public class EqualsExample {

	public static void main(String[] args) {
		String s1 = "홍길동";
		String s2 = "홍길동";
		
		if (s1 == s2) { 
			System.out.println("s1 == s2");
		} else {
			System.out.println("s1 != s2");			
		}
		
		if (s1.equals(s2)) {			
			System.out.println("s1 equals s2");			
		} else {			
			System.out.println("s1 !equals s2");			
		}
		
		String s3 = new String("홍길동");
		String s4 = new String("홍길동");
		
		if (s3 == s4) { 
			System.out.println("s3 == s4");
		} else {
			System.out.println("s3 != s4");			
		}
		
		if (s3.equals(s4)) {			
			System.out.println("s3 equals s4");			
		} else {			
			System.out.println("s3 !equals s4");			
		}
		
	}

}
