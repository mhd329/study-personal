package ch07.sec04.exam02;

public class SupersonicAirplane extends Airplane {

	protected static final int NORMAL = 1;
	protected static final int SUPERSONIC = 2;
	
	protected int flyMode = NORMAL;
	
	@Override
	protected void fly() {
		if (flyMode == SUPERSONIC) {
			System.out.println("초음속 비행.");
		} else {
			super.fly();
		}
	}
	
}
