package classtest.interfaceTest.car;

public class Sedan extends Car implements PassengerModel {
	
	public Sedan(String carName) {
		super(carName);
	}
	
	public void getOn() {
		System.out.printf("%s에 타다.\n", this.getCarName());
	}
	
	public void getOff() {
		System.out.printf("%s에서 내리다.\n", this.getCarName());
	}
	
}
