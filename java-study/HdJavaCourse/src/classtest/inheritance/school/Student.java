package classtest.inheritance.school;

public class Student extends Person {
	
	private String Hakbun;

	public String getHakbun() {
		return Hakbun;
	}

	public void setHakbun(String Hakbun) {
		this.Hakbun = Hakbun;
	}

	public Student() {
		this("", 0, "");
	}
	
	public Student(String name, int age, String Hakbun) {
		this.setName(name);
		this.setHakbun(Hakbun);
		this.setAge(age);
	}
	
}
