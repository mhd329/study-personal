package classtest.inheritance.school;

public class Person {
	protected String name;
	protected int age;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		if (age < 0) {
			System.out.println("나이는 0보다 작을 수 없습니다.");
			return;
		}
		this.age = age;
	}
	
}
