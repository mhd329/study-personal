public class App {

	public static void main(String[] args) {

		System.out.println("===== Person =====");
		System.out.println("----- p1 -----");
		Person p1 = new Person();

		System.out.println("\n----- p2 -----");
		Person p2 = new Person("Kim", 20);

		System.out.println("\n===== Student =====");
		System.out.println("----- s1 -----");
		Student s1 = new Student();

		System.out.println("\n----- s2 -----");
		Student s2 = new Student("Park", 25, "2024-001");

		System.out.println("\n===== Teacher =====");
		System.out.println("----- t1 -----");
		Teacher t1 = new Teacher();

		System.out.println("\n----- t2 -----");
		Teacher t2 = new Teacher("Lee", 35, "music");

	}

}
