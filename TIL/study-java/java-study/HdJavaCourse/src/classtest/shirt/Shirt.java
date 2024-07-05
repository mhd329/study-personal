package classtest.shirt;

public class Shirt {
	private String name;
	private String color;
	private String company;
	private char size;
	private int price;
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setColor(String color) {
		this.color = color;
	}
	
	public void setCompany(String company) {
		this.company = company;
	}
	
	public void setSize(char size) {
		switch (size) {
			case 'l', 'L' -> {
				this.size = size;
			}
			case 'm', 'M' -> {
				this.size = size;
			}
			case 's', 'S' -> {
				this.size = size;
			}
			default -> {
				System.out.println("사이즈 범위를 초과했거나 입력이 잘못되었습니다.");
			}
		}
		
	}
	
	public void setPrice(int price) {
		if (price < 0) {
			System.out.println("값은 음수가 될 수 없습니다.");
			return;
		}
		this.price = price;
	}
	
	public Shirt() {
		this("", "", "", 's', 0);
	}
	
	public Shirt(String name, String color, int price) {
		this(name, color, "", 's', price);
	}
	
	public Shirt(String name, String color, String company, char size, int price) {
		this.setName(name);
		this.setColor(color);
		this.setCompany(company);
		this.setSize(size);
		this.setPrice(price);
	}
	
	public void printInfo() {
		System.out.println(this.name);
		System.out.println(this.color);
		System.out.println(this.company);
		System.out.println(this.size);
		System.out.println(this.price);
	}
	
}
