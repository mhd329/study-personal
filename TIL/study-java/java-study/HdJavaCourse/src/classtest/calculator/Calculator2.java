package classtest.calculator;

public class Calculator2 {
	
	private int val1;
	private int val2;
	
	Calculator2(int val1, int val2) {
		this.val1 = val1;
		this.val2 = val2;
	}
	
	public void plus() {
		int result = this.val1 + this.val2;
		System.out.println(result);
	}
	public void minus() {
		int result = this.val1 - this.val2;
		System.out.println(result);
	}
	public void multiply() {
		int result = this.val1 * this.val2;
		System.out.println(result);
	}
	public void divide() {
		int result = this.val1 / this.val2;
		System.out.println(result);
	}
	public void rest() {
		int result = this.val1 % this.val2;
		System.out.println(result);
	}
	
	public void printInfo() {
		System.out.println(this.val1 + ", " + this.val2);
	}
	
	public void clear() {
		this.val1 = 0;
		this.val2 = 0;
		System.out.println("클리어");
	}
	
}
