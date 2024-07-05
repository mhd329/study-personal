package classtest.inheritance.product;

public class Fruit extends Product {
	
	private String packingType;

	public String getPackingType() {
		return packingType;
	}

	public void setPackingType(String packingType) {
		this.packingType = packingType;
	}
	
	public Fruit(String name, int price, String packingType) {
		super(name, price);
		this.packingType = packingType;
	}
	
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 포장타입=%-20s\n", this.packingType);
	}
	
}
