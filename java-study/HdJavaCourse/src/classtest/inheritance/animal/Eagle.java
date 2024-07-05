package classtest.inheritance.animal;

public class Eagle extends Animal {

	private int wingsCnt;
	
	public int getWingsCnt() {
		return wingsCnt;
	}
	public void setWingsCnt(int wingsCnt) {
		this.wingsCnt = wingsCnt;
	}
	
	public Eagle(String name, int age, char sex, int wingsCnt) {
		super("독수리", name, age, sex);
		this.wingsCnt = wingsCnt;
	}
	
	public void fly() {
		System.out.println("fly() :: 나비");
	}
	
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 날개=%-2d(개)\n", this.wingsCnt);
	}
	
}
