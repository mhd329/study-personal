package classtest.inheritance.cafe;

public class CafeApp {

	public static void main(String[] args) {

		System.out.println("===== Menu =====");
		Menu m = new Menu("녹차", 3500);
		m.printInfo();

		System.out.println("\n===== Coffee =====");
		Coffee c = new Coffee("아메리카노", 3000, "에티오피아 예가체프");
		c.printInfo();

		System.out.println("\n===== Ade =====");
		Ade a = new Ade("레몬에이드", 4000, "레몬, 시럽");
		a.printInfo();

	}

}
