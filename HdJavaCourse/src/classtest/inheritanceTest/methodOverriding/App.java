package classtest.inheritanceTest.methodOverriding;

public class App {

	public static void main(String[] args) {

		System.out.println("===== Person =====");
		Person p = new Person("Lee", 30);
		p.printInfo();

		System.out.println("\n===== Student =====");
		Student s = new Student("Park", 20, "2020-001");
		s.printInfo();

		System.out.println("\n===== Teacher =====");
		Teacher t = new Teacher("Hong", 25, "music");
		t.printInfo();

	}

}
