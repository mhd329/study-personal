
public class Person {

	private String name;
	private int age;

	public Person() {
		System.out.println("Person()");
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