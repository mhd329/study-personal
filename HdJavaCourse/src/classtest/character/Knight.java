package classtest.character;

public class Knight extends Character {
	public Knight(String name) {
		super(name, "Knight");
	}
	
	@Override
	public void attack() {
		System.out.printf("[%s / %s] %s 공격\n", this.getName(), this.getJobClass(), "근거리");
	}
}
