package ch07.sec08.exam01;

public class CarExample {

	public static void main(String[] args) {
		Car mc = new Car();
		
		mc.tire = new Tire();
		mc.run();
		mc.tire = new HankookTire();
		mc.run();
		mc.tire = new KumhoTire();
		mc.run();

	}

}
