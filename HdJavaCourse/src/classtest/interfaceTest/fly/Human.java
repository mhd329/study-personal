package classtest.interfaceTest.fly;

public class Human extends Animal {
	
	private String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public Human(int age, String name) {
		super(age);
		this.name = name;
	}
	
	@Override
	public void eat() {
		System.out.println("Human.eat()");
	}
	
	@Override
	public void printInfo() {
		System.out.printf("나이=%d : 이름=%s\n", this.getAge(), this.getName());
	}
	
}
