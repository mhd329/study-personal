package classtest.inheritance.animal;

public class Zoo {

	public static void main(String[] args) {

		System.out.println("===== Animal =====");
		Animal a = new Animal("동물", "콩이", 1, 'F');
		a.printInfo();

		System.out.println("\n===== Cat =====");
		Cat c = new Cat("양이", 5, 'F', 3);
		c.printInfo();
		c.sleep();

		System.out.println("\n===== Eagle =====");
		Eagle e = new Eagle("나비", 4, 'M', 2);
		e.printInfo();
		e.fly();

	}

}
