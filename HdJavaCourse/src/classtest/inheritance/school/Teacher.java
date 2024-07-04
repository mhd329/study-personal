package classtest.inheritance.school;

public class Teacher extends Person {

	private String lesson;

	public String getLesson() {
		return lesson;
	}

	public void setLesson(String lesson) {
		this.lesson = lesson;
	}

	public Teacher() {
		this("", 0, "");
	}
	
	public Teacher(String name, int ageString, String lesson) {
		this.setName(name);
		this.setAge(ageString);
		this.setLesson(lesson);
	}
	
}
