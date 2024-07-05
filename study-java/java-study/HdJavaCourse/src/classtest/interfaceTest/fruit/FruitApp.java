package classtest.interfaceTest.fruit;

public class FruitApp {

	public static void main(String[] args) {

		// ========================================
		// 인터페이스
		// ========================================
//		Fruit fruit = new Fruit();	// Error. 인터페이스는 객체 생성 불가

		// ========================================
		// 클래스
		// ========================================
		Apple apple = new Apple();
		apple.printInfo();

		// Polymorphism
		// - 인터페이스 타입으로 객체 생성
		Fruit fa = new Apple();

		// ========================================
		// 추상 클래스
		// - 인터페이스를 구현한 클래스가 인터페이스 메서드를 구현하지 않으면 추상클래스가 된다.
		// ========================================
//		TropicalFruit tf = new TropicalFruit();	// Error. 추상 클래스는 객체 생성 불가

	}

}
