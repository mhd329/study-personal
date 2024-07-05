package classtest.inheritance.product;
import classtest.DecimalUtil;

public class Product {

	private String name;
	private int price;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		if (price < 0) {
			System.out.println("값은 음수가 될 수 없습니다.");
			this.price = 0;
			return;
		}
		this.price = price;
	}
	
	public Product(String name, int price) {
		this.setName(name);
		this.setPrice(price);
	}
	
	public void printInfo() {
		System.out.printf("제품명=%-20s\t| 가격=%-20s\t", this.name, DecimalUtil.decimalComma(this.price));
	}
	
}
