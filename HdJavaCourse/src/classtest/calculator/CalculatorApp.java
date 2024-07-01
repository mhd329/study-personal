package classtest.calculator;

public class CalculatorApp {

	public static void main(String[] args) {
		Calculator cal = new Calculator();
		
		int val1 = 10;
		int val2 = 6;
		double val3 = 19.2;
		double val4 = 6.7;
		System.out.println("int");
		cal.plus(val1, val2);
		cal.minus(val1, val2);
		cal.multiply(val1, val2);
		cal.divide(val1, val2);
		cal.rest(val1, val2);
		System.out.println("double");
		cal.plus(val3, val4);
		cal.minus(val3, val4);
		cal.multiply(val3, val4);
		cal.divide(val3, val4);
		cal.rest(val3, val4);
		
	}

}
