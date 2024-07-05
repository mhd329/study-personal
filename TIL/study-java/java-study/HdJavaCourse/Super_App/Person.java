public class Person {

	private String name;
	private int age;

	public Person() {
		System.out.println("Person()");
	}

	public Person(String name) {
		this.name = name;
		System.out.println("Person(String name)");
	}

	public Person(int age) {
		this.age = age;
		System.out.println("Person(int age)");
	}

	public Person(String name, int age) {
		this.name = name;
		this.age = age;
		System.out.println("Person(String name, int age)");
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

}