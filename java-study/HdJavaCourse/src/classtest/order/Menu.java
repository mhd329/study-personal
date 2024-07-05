package classtest.order;

public class Menu {
	// new Menu("빅맥세트", 5500);
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
		this.price = price;
	}

	public Menu(String name, int value) {
		this.setName(name);
		this.setPrice(value);
	}
	
}
