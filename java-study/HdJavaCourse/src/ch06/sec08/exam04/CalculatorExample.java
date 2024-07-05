package ch06.sec08.exam04;

public class CalculatorExample {

	public static void main(String[] args) {
		Calculator calc = new Calculator();
		double res1 = calc.areaRectangle(10);
		double res2 = calc.areaRectangle(10, 20);
		
		System.out.println(res1);
		System.out.println(res2);
	}

}
