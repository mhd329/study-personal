package classtest.interfaceTest.dog;

public class DogApp {

	public static void main(String[] args) {

		// ========================================
		// # Animal 클래스
		// 메서드 : walk()
		// # Pet 인터페이스
		// 메서드 : gotoDogCafe()
		// # 상속
		// Animal(클래스), Pet(인터페이스) <- Dog
		// ========================================

		System.out.println("===== Dog =====");
		Dog d = new Dog();
		d.walk();
		d.gotoDogCafe();

	}

}
