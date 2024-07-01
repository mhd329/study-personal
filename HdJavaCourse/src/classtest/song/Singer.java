package classtest.song;

public class Singer {
	private String name;
	private char sex;
	private String birthdate;
	private String companyt;
	
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public char getSex() {
		return this.sex;
	}

	public void setSex(char sex) {
		this.sex = sex;
	}

	public String getBirthdate() {
		return this.birthdate;
	}

	public void setBirthdate(String birthdate) {
		this.birthdate = birthdate;
	}

	public String getCompanyt() {
		return this.companyt;
	}

	public void setCompanyt(String companyt) {
		this.companyt = companyt;
	}

	public Singer(String name, char sex, String birthdate, String companyt) {
		this.setName(name);
		this.setSex(sex);
		this.setBirthdate(birthdate);
		this.setCompanyt(companyt);
	}
	
	public void printInfo() {
		System.out.printf("이름=%s | 성별=%c | 생년월일=%s | 소속사=%s\n", this.getName(), this.getSex(), this.getBirthdate(), this.getCompanyt());
	}
	
}
