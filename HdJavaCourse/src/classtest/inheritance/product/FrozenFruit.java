package classtest.inheritance.product;

public class FrozenFruit extends Fruit {
	
	public FrozenFruit(String name, int price) {
		super(name, price, "냉동(종이포장)");
	}
	
	public FrozenFruit(String name, int price, String frozenPackingType) {
		super(name, price, frozenPackingType);
	}
	
}
