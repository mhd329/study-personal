package classtest.anonymous.character;

public class CharacterApp {

	public static void main(String[] args) {
		System.out.println("===== Anonymous Object =====");
		System.out.println("----- 1 -----");
		Character c1 = new Character() {
			@Override
			public void attack() {
				System.out.print("근거리 ");
				super.attack();
			}
		};
		c1.attack();
	
		System.out.println("\n----- 2 -----");
		Character c2 = new Character("에이스") {
			@Override
			public void attack() {
				System.out.print("소총 ");
				super.attack();
			}
		};
		c2.attack();
		System.out.println(c2.getName());
		
		System.out.println("\n----- 3 -----");
		Character c3 = new Character("제임스", "라이플맨") {
			@Override
			public void attack() {
				System.out.print("소총 ");
				super.attack();
			}
		};
		c3.attack();
		c3.printInfo();
		
	}

}
