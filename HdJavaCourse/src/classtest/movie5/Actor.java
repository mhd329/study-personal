package classtest.movie5;

public class Actor {
	private String name;
	private String sex;
	private String birthdate;
	private String nationality;
	
	public static Actor makeActor(String name, String sex, String birthdate, String nationality) {
		Actor actor = new Actor(name, sex, birthdate, nationality);
		return actor;
	}
	
	private Actor(String name, String sex, String birthdate, String nationality) {
		this.name = name;
		this.sex = sex;
		this.birthdate = birthdate;
		this.nationality = nationality;
	}
	
	public void printInfo() {
		System.out.printf("이름=%s | 성별=%s | 생년월일=%s | 국적=%s\n", this.name, this.sex, this.birthdate, this.nationality);
	}
}
