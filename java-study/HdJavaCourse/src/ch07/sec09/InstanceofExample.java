package ch07.sec09;

public class InstanceofExample {
	public static void personInfo(Person p) {
		System.out.printf("이름 : %s\n", p.name);
		p.walk();
	
		if (p instanceof Student) {
			Student std_p = (Student) p;
			System.out.printf("학번 : %d\n", std_p.studentNo);
			std_p.study();
		}
	}
	
	public static void main(String[] args) {
		Person p1 = new Person("홍길동");
		personInfo(p1);
		System.out.println();
		Person p2 = new Student("김길동", 10);
		personInfo(p2);
	}
}
