package classtest.inheritanceTest.methodOverriding;

public class Student extends Person {

	private String hakbun;

	public Student() {
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
		super.printInfo();
		System.out.printf(" | 학번=%s", this.hakbun);
	}

}