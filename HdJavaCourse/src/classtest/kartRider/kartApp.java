package classtest.kartRider;

public class kartApp {

	public static void main(String[] args) {
		Kart kart = new Kart("버스트", "Green");
		
		System.out.println("카트 정보");
		kart.printKartInfo();

		System.out.println("시작");
		kart.speedUp();
		kart.speedUp();
		kart.pickupBooster();
		kart.pickupBooster();
		kart.useBooster();
		kart.useBooster();
		kart.speedDown();
		kart.speedDown();
	}

}
