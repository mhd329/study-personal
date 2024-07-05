public class App {

	public static void main(String[] args) {

		System.out.println("===== cry() =====");
		Animal animal = new Animal();
		Bird bird = new Bird();
		Cow cow = new Cow();

		animal.cry();
		bird.cry();
		cow.cry();

		System.out.println("\n===== Polymorphic Argument =====");
		Biz biz = new Biz();

		System.out.println("----- biz.cryAnimal() -----");
//		biz.cryAnimal(animal);
//		biz.cryAnimal(bird); 
//		biz.cryAnimal(cow); 

		System.out.println("\n----- biz.cryBird() -----");
//		biz.cryBird(animal); 
//		biz.cryBird(bird);
//		biz.cryBird(cow); // Error

		System.out.println("\n----- biz.cryCow() -----");
//		biz.cryCow(animal);
//		biz.cryCow(bird);
//		biz.cryCow(cow);

	}
}
