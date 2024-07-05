package classtest.movie4;

public class Actor {
	private String name;
	private String sex;
	private String birthdate;
	private String nationality;
	
	public Actor(String name, String sex, String birthdate, String nationality) {
		this.name = name;
		this.sex = sex;
		this.birthdate = birthdate;
		this.nationality = nationality;
	}
	
	public void printInfo() {
		System.out.println(this.name);
		System.out.println(this.sex);
		System.out.println(this.birthdate);
		System.out.println(this.nationality);
	}
	
}
