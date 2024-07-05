package classtest.inheritanceTest.menuTest;

public class MenuApp {

	public static void main(String[] args) {
		Menu m = new Menu("녹차", 5000);
		m.printInfo();
		
		System.out.println("\n\n===== Menu =====\n");
		Menu[] menuArray = new Menu[3];
		menuArray[0] = MenuService.makeCoffee("아메리카노", 3000, "에티오피아 예가체프");
		menuArray[1] = MenuService.makeCoffee("카푸치노", 3500, "케냐 오클랜드");
		menuArray[2] = MenuService.makeAde("레몬에이드", 4000, "레몬, 시럽");

		for (int i = 0; i < menuArray.length; i ++) {
			System.out.printf("%d. ", i + 1);
			menuArray[i].printInfo();
		}
		
	}

}
