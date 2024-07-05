package classtest.interfaceTest.car;

public abstract class Car {
	private String carName;

	public String getCarName() {
		return carName;
	}

	public void setCarName(String carName) {
		this.carName = carName;
	}
	
	public Car(String carName) {
		this.carName = carName;
	}
	
}
