package classtest.inheritanceTest.PersonTest2;

public class Student extends Person {

	private String hakbun; // 학번

	public Student() {
	}

	public Student(String hakbun) {
		this.hakbun = hakbun;
	}

	public Student(String name, int age, String hakbun) {
		super(name, age);
		this.hakbun = hakbun;
	}

	public String getHakbun() {
		return hakbun;
	}

	public void setHakbun(String hakbun) {
		this.hakbun = hakbun;
	}

	@Override
	public void printInfo() {
		System.out.print("이름=" + getName());
		System.out.print(" | 나이=" + getAge());
		System.out.println(" | 학번=" + hakbun);
	}
}