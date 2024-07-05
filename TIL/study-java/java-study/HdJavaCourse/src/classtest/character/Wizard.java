package classtest.character;

public class Wizard extends Character {
	public Wizard(String name) {
		super(name, "Wizard");
	}
	
	@Override
	public void attack() {
		System.out.printf("[%s / %s] %s 공격\n", this.getName(), this.getJobClass(), "마법");
	}
}
