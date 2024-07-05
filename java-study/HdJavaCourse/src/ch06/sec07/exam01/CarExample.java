package ch06.sec07.exam01;

public class CarExample {

	public static void main(String[] args) {
		Car car = new Car("그랜저", "검정", 250);
		System.out.println(car.getModel());
		System.out.println(car.getMaxSpeed());
//		Car car = new Car();
	}

}
