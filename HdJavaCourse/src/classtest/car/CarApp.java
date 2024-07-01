package classtest.car;

public class CarApp {

	public static void main(String[] args) {
		System.out.println("=====회사 정보=====");
		String name = "Hyundai";
		String biz = "자동차";
		Company company = new Company(name, biz);
		company.printInfo();
		
		System.out.println("\n=====자동차 정보=====");
		String model = "Santafe";
		String color = "white";
		String type = "SUV";
		
		Car car = new Car(model, color, type, company);
		car.printInfo();

	}

}
