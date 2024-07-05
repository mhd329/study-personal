package classtest.coffee2;

public class Coffee {
	private String name;
	private int price;
	
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getPrice() {
		return this.price;
	}
	
	public void setPrice(int price) {
		if (price < 0) {
			System.out.println("가격은 양수여야 합니다.");
			return;
		}
		this.price = price;
	}
	
	public Coffee() {
		this("", 0);
	}
	
	public Coffee(String name, int price) {
		this.name = name;
		this.price = price;
	}
	
	public void printInfo() {
		System.out.println(this.getName());
		System.out.println(this.getPrice());;
	}
}
