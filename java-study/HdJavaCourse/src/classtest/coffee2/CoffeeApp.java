package classtest.coffee2;

public class CoffeeApp {

	public static void main(String[] args) {
		System.out.println("c1");
		Coffee c1 = new Coffee();
		c1.setName("아메리카노");
		c1.setPrice(4000);
		c1.printInfo();
		
		System.out.println("c2");
		Coffee c2 = new Coffee("카푸치노", 5000);
		c2.printInfo();
		
	}

}
