package classtest.inheritanceTest.methodOverriding;

public class Teacher extends Person {

	private String lesson;

	public Teacher() {
	}

	public Teacher(String name, int age, String lesson) {
		super(name, age);
		this.lesson = lesson;
	}

	public String getLesson() {
		return lesson;
	}

	public void setLesson(String lesson) {
		this.lesson = lesson;
	}

	@Override
	public void printInfo() {
		super.printInfo();
		System.out.printf(" | 과목=%s", this.lesson);
	}
	
}
