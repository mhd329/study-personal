package ch06.sec07.exam05;

public class CarExample {

	public static void main(String[] args) {
		Car c1 = new Car("자가용");
		Car c2 = new Car("자가용", "빨강");
		Car c3 = new Car("택시", "검정", 200);
		System.out.println("c1");
		System.out.println(c1.company);
		System.out.println(c1.model);
		System.out.println("c2");
		System.out.println(c2.company);
		System.out.println(c2.model);
		System.out.println(c2.color);
		System.out.println("c3");
		System.out.println(c3.company);
		System.out.println(c3.model);
		System.out.println(c3.color);
		System.out.println(c3.maxSpeed);

	}

}
