package ch07.sec02;

public class SmartPhoneExample {

	public static void main(String[] args) {
		SmartPhone myPhone = new SmartPhone("갤럭시", "은색");
		
		System.out.printf("모델: %s\n", myPhone.model);
		System.out.printf("색상: %s\n", myPhone.color);
		
		System.out.printf("와이파이 상태: %b\n", myPhone.wifi);

		myPhone.bell();
		myPhone.sendVoice("hi");
		myPhone.receiveVoice("hello");
		myPhone.sendVoice("world");
		myPhone.hangUp();
		
		myPhone.setWifi(true);
		myPhone.internet();
		
	}

}
