package classtest.character;

public class Character {
	private String name;
	private String jobClass;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getJobClass() {
		return jobClass;
	}
	public void setJobClass(String jobClass) {
		this.jobClass = jobClass;
	}
	
	public void attack() {
		System.out.println("공격");
	}
	
	public void printInfo() {
		System.out.printf("이름=%s | 캐릭터=%s\n", this.name, this.jobClass);
	}
	
	public Character(String name, String jobClass) {
		this.name = name;
		this.jobClass = jobClass;
	}
	
}
