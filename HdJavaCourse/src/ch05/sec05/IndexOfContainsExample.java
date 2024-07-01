package ch05.sec05;

public class IndexOfContainsExample {

	public static void main(String[] args) {
		String subject = "자바 프로그래밍";
		
		int location = subject.indexOf("프로그래밍");
		System.out.println(location);
		String substring = subject.substring(location);
		System.out.println(substring);
		
		location = subject.indexOf("자바");
		if (location != -1) {
			System.out.println("관련 있음.");
		} else {
			System.out.println("관련 없음.");			
		}
		
		boolean res = subject.contains("자바");
		if (res) {
			System.out.println("관련 있음.");
		} else {
			System.out.println("관련 없음.");			
		}
		
	}

}
