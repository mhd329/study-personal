public class ProductApp {

	public static void main(String[] args) {

		// ==================================================
		// # 추상 클래스
		// ==================================================
//		Product p = new Product(); // Error
//		Fruit f = new Fruit();// Error

		// ==================================================
		// # 일반 클래스
		// 추상 메서드를 구현해야만 일반 클래스가 된다.
		// ==================================================
		FrozenFruit ff = new FrozenFruit();
		ff.printInfo();

	}

}
