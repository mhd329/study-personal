package classtest.inheritance.cafe;

public class Menu {
	protected String name;
	protected int price;
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
		this.price = price;
	}
	
	protected void printInfo() {
		System.out.printf("메뉴=%-5s\t| 가격=%-4d\t", this.name, this.price);
	}
	
	public Menu(String name, int price) {
		this.setName(name);
		this.setPrice(price);
	}
	
}
