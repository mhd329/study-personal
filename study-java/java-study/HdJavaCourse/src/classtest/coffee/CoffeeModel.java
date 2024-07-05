package classtest.coffee;

public class CoffeeModel {
	private String coffee = "에스프레소";
	private int price = 3000;
	private String order = "샷추가";
	
	String getCoffee() {
		return this.coffee;
	}
	
	void setCoffee(String coffee) {
		this.coffee = coffee;
	}
	
	int getPrice() {
		return this.price;
	}
	
	void setPrice(int price) {
		this.price = price;
	}
	
	String getOrder() {
		return this.order;
	}
	
	void setOrder(String order) {
		this.order = order;
	}
	
	void printInfo() {
		System.out.println(this.getCoffee());
		System.out.println(this.getPrice());
		System.out.println(this.getOrder());
	}
}
