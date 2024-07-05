package classtest.character;

public class GameApp {

	public static void main(String[] args) {
		System.out.println("===== Character =====");
		Character character = new Character("Paige", "요정");
		character.printInfo();
		
		Archer archer = new Archer("신궁");
		archer.printInfo();
		Knight knight = new Knight("호영");
		knight.printInfo();
		Wizard wizard = new Wizard("메르세데스");
		wizard.printInfo();
		
		System.out.println("\n===== attack() =====");
		character.attack();
	
		System.out.println("\n===== Game : attack() =====");
		Game game = new Game();
		game.attack(archer);
		game.attack(knight);
		game.attack(wizard);
	
	}

}
