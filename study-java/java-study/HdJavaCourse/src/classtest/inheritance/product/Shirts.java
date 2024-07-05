package classtest.inheritance.product;

public class Shirts extends Fashion {

	private String size;

	public String getSize() {
		return size;
	}

	public void setSize(String size) {
		this.size = size;
	}
	
	public Shirts(String name, int price, String size, String asNum) {
		super(name, price, asNum);
		this.size = size;
	}
	
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 크기=%-20s| A/S=%-20s\n", this.size, super.getAsNum());
	}
	
}
