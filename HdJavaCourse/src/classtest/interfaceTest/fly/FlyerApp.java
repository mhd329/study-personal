package classtest.interfaceTest.fly;

public class FlyerApp {

	public static void main(String[] args) {
		System.out.println("===== Human =====");
		Animal human = new Human(29, "James");
		human.printInfo();
		human.eat();
		
		System.out.println("===== Bird =====");
		Bird bird = new Bird(5, 2);
		bird.printInfo();
		bird.eat();
		bird.takeOff();
		bird.land();
		bird.fly();
		
		System.out.println("===== SuperMan =====");
		SuperMan superman = new SuperMan(30, "Song");
		superman.printInfo();
		superman.eat();
		superman.takeOff();
		superman.land();
		superman.fly();
		
		System.out.println("===== Airplane =====");
		Airplane air = new Airplane();
		air.load();
		air.takeOff();
		air.fly();
		air.land();
		air.unload();
		
	}

}
