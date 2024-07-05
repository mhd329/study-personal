package classtest.interfaceTest.fly;

public class Bird extends Animal implements Flyer {
	private int wingsCnt;

	public int getWingsCnt() {
		return wingsCnt;
	}

	public void setWingsCnt(int wingsCnt) {
		this.wingsCnt = wingsCnt;
	}
	
	public Bird(int age, int wingsCnt) {
		super(age);
		this.wingsCnt = wingsCnt;
	}
	
	@Override
	public void eat() {
		System.out.println("Bird.eat()");
	}
	@Override
	public void printInfo() {
		System.out.printf("나이=%d : 날개수=%d\n", this.getAge(), this.getWingsCnt());
	}
	@Override
	public void takeOff() {
		System.out.println("Bird.takeOff()");
	}
	@Override
	public void fly() {
		System.out.println("Bird.fly()");
	}
	@Override
	public void land() {
		System.out.println("Bird.land()");
	}
	
}
