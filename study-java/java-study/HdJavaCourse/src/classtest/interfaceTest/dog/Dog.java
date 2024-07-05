package classtest.interfaceTest.dog;

public class Dog extends Animal implements Pet {

	@Override
	void walk() {
		System.out.println("Dog.walk()");
	}

	@Override
	public void gotoDogCafe() {
		System.out.println("Dog.gotoDogCafe()");

	}

}
