package classtest.interfaceTest.fly;

public class Airplane implements Flyer, Transport {
	@Override
	public void load() {
		System.out.println("Airplane.load()");
	}
	@Override
	public void takeOff() {
		System.out.println("Airplane.takeOff()");
	}
	@Override
	public void fly() {
		System.out.println("Airplane.fly()");
	}
	@Override
	public void land() {
		System.out.println("Airplane.land()");
	}
	@Override
	public void unload() {
		System.out.println("Airplane.unload()");
	}
}
