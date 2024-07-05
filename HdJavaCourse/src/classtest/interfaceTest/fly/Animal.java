package classtest.interfaceTest.fly;

public abstract class Animal {
	abstract void eat();
	abstract void printInfo();
	
	private int age;
	
	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public Animal(int age) {
		this.age = age;
	}
	
}
