package ch06.sec07.exam01;

public class Car {
	private String model;
	private String color;
	private int maxSpeed;
	Car(String model, String color, int maxSpeed) {
		this.model = model;
		this.color = color;
		if (maxSpeed > 0) {			
			this.maxSpeed = maxSpeed;
		}
	}
	public String getModel() {
		return this.model;
	}
	public String getColor() {
		return this.color;
	}
	public int getMaxSpeed() {
		return this.maxSpeed;
	}
}
