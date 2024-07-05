package classtest.interfaceTest.car;

public class Suv extends Car implements PassengerModel, TruckModel {

	public Suv(String carName) {
		super(carName);
	}
	
	public void getOn() {
		System.out.printf("%s에 타다.\n", this.getCarName());
	}
	
	public void getOff() {
		System.out.printf("%s에서 내리다.\n", this.getCarName());
	}
	
	public void load() {
		System.out.printf("%s에 짐을 싣다.\n", this.getCarName());
	}
	
	public void unload() {
		System.out.printf("%s에서 짐을 내리다.\n", this.getCarName());
	}
	
}
