package classtest.calculator;

public class Calculator3App {

	public static void main(String[] args) {
		Calculator3 cal3 = new Calculator3();
		cal3.none();
		
		int val1 = 10;
		int val2 = 6;

		Calculator3.plus(val1, val2);
		Calculator3.minus(val1, val2);
		Calculator3.multiply(val1, val2);
		Calculator3.divide(val1, val2);
		Calculator3.rest(val1, val2);

	}

}
