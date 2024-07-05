package classtest.NestedClass;

public class DrinkApp {

	public static void main(String[] args) {
	
	System.out.println("===== 외부 클래스 =====");
	Drink drink = new Drink("물");
	drink.printInfo();
	
	System.out.println("\n===== 중첩 클래스 =====");
	Drink.Coffee coffee = drink.new Coffee("아메리카노");
	
	coffee.printCoffeInfo();
	coffee.printCoffeeAllnfo();
	
	}

}