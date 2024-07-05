package ch08.sec10.exam02;

public class CastingExample {

	public static void main(String[] args) {
		Vehicle v = new Bus();
		
		v.run();
		
		Bus vBus = (Bus) v;
		
		vBus.run();
		vBus.checkFare();

	}

}
