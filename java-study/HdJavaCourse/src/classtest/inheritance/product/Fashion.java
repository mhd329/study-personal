package classtest.inheritance.product;

public class Fashion extends Product {
	
	private String asNum;

	public String getAsNum() {
		return asNum;
	}

	public void setAsNum(String asNum) {
		this.asNum = asNum;
	}
	
	public Fashion(String name, int price, String asNum) {
		super(name, price);
		this.asNum = asNum;
	}
	
}
