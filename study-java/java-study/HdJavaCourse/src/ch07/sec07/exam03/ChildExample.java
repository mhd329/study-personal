package ch07.sec07.exam03;

public class ChildExample {

	public static void main(String[] args) {
		Parent p = new Child();
		
		p.field1 = "data1";
		p.method1();
		p.method2();

		Child c = (Child) p;
		c.field2 = "data2";
		c.method3();
		
	}

}
