package ch12.sec03.exam05;

public class MemberApp {

	public static void main(String[] args) {
		Member m1 = new Member();
		
		System.out.println("----- 생성 -----");
		System.out.println(m1.getId());
		System.out.println(m1.getName());
		System.out.println(m1.getAge());
		
		System.out.println("\n----- Setter -----");
		m1.setId("morning");
		m1.setName("James");
		m1.setAge(30);
		
		System.out.println(m1.getId());
		System.out.println(m1.getName());
		System.out.println(m1.getAge());
		
	}

}
