package classtest.inheritance.animal;

public class Cat extends Animal {

	private int legsCnt;
	
	public int getLegsCnt() {
		return legsCnt;
	}
	public void setLegsCnt(int legsCnt) {
		this.legsCnt = legsCnt;
	}
	
	public Cat(String name, int age, char sex, int legsCnt) {
		super("고양이", name, age, sex);
		this.legsCnt = legsCnt;
	}
	
	public void sleep() {
		System.out.println("sleep() :: 양이");
	}
	
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 다리=%-2d(개)\n", this.legsCnt);
	}
	
}
