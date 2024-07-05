package ch07.sec04.exam01;

public class ComputerExample {

	public static void main(String[] args) {
		int r = 10;
		
		Calculator calc = new Calculator();
		System.out.println(calc.areaCircle(r));
		System.out.println();
		
		Computer comp = new Computer();
		System.out.println(comp.areaCircle(r));
		System.out.println();

	}

}
