package classtest.interfaceTest.car;

public class Truck extends Car implements TruckModel {
	
	public Truck(String carName) {
		super(carName);
	}
	
	public void load() {
		System.out.printf("%s에 짐을 싣다.\n", this.getCarName());
	}
	
	public void unload() {
		System.out.printf("%s에서 짐을 내리다.\n", this.getCarName());
	}
	
}
