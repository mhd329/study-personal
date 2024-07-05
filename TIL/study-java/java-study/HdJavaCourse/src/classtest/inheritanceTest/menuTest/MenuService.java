package classtest.inheritanceTest.menuTest;

public class MenuService {
	public static Coffee makeCoffee(String name, int price, String ingredient) {
		Coffee coffee = new Coffee(name, price, ingredient);
		return coffee;
	}
	public static Ade makeAde(String name, int price, String ingredient) {
		Ade ade = new Ade(name, price, ingredient);
		return ade;
	}
}
