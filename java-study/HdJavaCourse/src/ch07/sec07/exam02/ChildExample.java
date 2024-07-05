package ch07.sec07.exam02;

public class ChildExample {

	public static void main(String[] args) {
		Child c = new Child();
		
		Parent p = c;
		
		p.method1();
		p.method2();

	}

}
