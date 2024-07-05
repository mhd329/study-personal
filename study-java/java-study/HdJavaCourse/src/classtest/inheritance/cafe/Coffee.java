package classtest.inheritance.cafe;

public class Coffee extends Menu {

	private String beanType;
	
	public String getBeanType() {
		return beanType;
	}

	public void setBeanType(String beanType) {
		this.beanType = beanType;
	}

	public Coffee(String name, int price, String beanType) {
		super(name, price);
		this.setBeanType(beanType);;
	}
	
	@Override
	protected void printInfo() {
		super.printInfo();
		System.out.printf("| 원두=%-10s", this.beanType);
	}
	
}
