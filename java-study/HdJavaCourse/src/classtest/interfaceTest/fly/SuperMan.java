package classtest.interfaceTest.fly;

public class SuperMan extends Human implements Flyer {
	
	@Override
	public void eat() {
		System.out.println("SuperMan.eat()");
	}
	
	@Override
	public void takeOff() {
		System.out.println("SuperMan.takeOff()");
	}
	
	@Override
	public void fly() {
		System.out.println("SuperMan.fly()");
	}
	
	@Override
	public void land() {
		System.out.println("SuperMan.land()");
	}
	
	public SuperMan(int age, String name) {
		super(age, name);
	}
	
}
