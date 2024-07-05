package classtest.footballPlayer;

public class FootballPlayer {
	private String name;
	private String uniformNumber;
	private String teamName;
	private int speed;
	private int tech;
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setUniformNumber(String uniformNumber) {
		this.uniformNumber = uniformNumber;
	}
	
	public void setTeamName(String teamName) {
		this.teamName = teamName;
	}
	
	public void setSpeed(int speed) {
		this.speed = speed;
	}
	
	public void setTech(int tech) {
		this.tech = tech;
	}
	
	public void printInfo() {
		System.out.println(this.name);
		System.out.println(this.teamName);
		System.out.println(this.uniformNumber);
		System.out.println(this.speed);
		System.out.println(this.tech);
	}
	
	FootballPlayer() {
		
	}
	
	FootballPlayer(String name, String uniformNumber, String teamName, int speed, int tech) {
		this.setName(name);
		this.setUniformNumber(uniformNumber);
		this.setTeamName(teamName);
		this.setSpeed(speed);
		this.setTech(tech);
	}
	
}
