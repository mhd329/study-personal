package classtest.inheritanceTest.noArgsTest;

public class Student extends Person {

	private String hakbun;

	public Student() {
		System.out.println("Student()");
	}

	public String getHakbun() {
		return hakbun;
	}

	public void setHakbun(String hakbun) {
		this.hakbun = hakbun;
	}

}