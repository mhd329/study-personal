package classtest.character;

public class Archer extends Character {
	public Archer(String name) {
		super(name, "Archer");
	}
	
	@Override
	public void attack() {
		System.out.printf("[%s / %s] %s 공격\n", this.getName(), this.getJobClass(), "원거리");
	}
}
