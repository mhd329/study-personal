public class Student extends Person {

	private String hakbun;

	public Student() {
		System.out.println("Student()");
	}

	public Student(String name, int age, String hakbun) {
		super(name, age);

		this.hakbun = hakbun;
		System.out.println("Student(String name, int age, String hakbun) ");
	}

	public String getHakbun() {
		return hakbun;
	}

	public void setHakbun(String hakbun) {
		this.hakbun = hakbun;
	}

}