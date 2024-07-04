package classtest.inheritanceTest.menuTest;

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
		this.setBeanType(beanType);
	}
	
	@Override
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 원두=%-10s\n", this.beanType);
	}
}
