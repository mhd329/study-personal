package classtest.car;

public class Car {
	private String model;
	private String color;
	private String type;
	private Company company;
	
	public String getModel() {
		return this.model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getColor() {
		return this.color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getType() {
		return this.type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public Company getCompany() {
		return this.company;
	}

	public void setCompany(Company company) {
		this.company = company;
	}

	public Car(String model, String color, String type, Company company) {
		this.setModel(model);
		this.setColor(color);
		this.setType(type);
		this.setCompany(company);
	}
	
	public void printInfo() {
		System.out.printf("모델=%s | 색상=%s | 타입=%s\n", this.getModel(), this.getColor(), this.getType());
		this.company.printInfo();
	}
}
