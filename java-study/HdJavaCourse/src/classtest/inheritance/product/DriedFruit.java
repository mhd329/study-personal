package classtest.inheritance.product;

public class DriedFruit extends Fruit {
	
	public DriedFruit(String name, int price) {
		super(name, price, "상온(종이포장)");
	}
	
	public DriedFruit(String name, int price, String driedPackingType) {
		super(name, price, driedPackingType);
	}

}
