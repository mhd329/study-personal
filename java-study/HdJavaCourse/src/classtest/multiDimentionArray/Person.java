package classtest.multiDimentionArray;

public class Person {
	private String name;
	private int age;
	
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getAge() {
		return this.age;
	}
	
	public void setAge(int age) {
		if (age < 0) {
			System.out.println("나이는 0보다 작을 수 없습니다.");
			return;
		}
		this.age = age;
	}
	
	public Person() {
		this("", 0);
	}
	
	public Person(String name, int age) {
		this.setName(name);
		this.setAge(age);
	}
	
	public void printInfo() {
		System.out.printf("이름=%s | 나이=%d\n", this.getName(), this.getAge());
	}
}
	
