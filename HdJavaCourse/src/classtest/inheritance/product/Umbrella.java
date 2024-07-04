package classtest.inheritance.product;

public class Umbrella extends Fashion {

	private int weight;

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		if (weight < 1) {
			System.out.println("무게는 1보다 작을 수 없습니다.");
			this.weight = 1;
			return;
		}
		this.weight = weight;
	}
	
	public Umbrella(String name, int price, int weight, String asNum) {
		super(name, price, asNum);
		this.weight = weight;
	}
	
	public void printInfo() {
		super.printInfo();
		System.out.printf("| 무게=%-20d| A/S=%-20s\n", this.weight, super.getAsNum());
	}
	
}
