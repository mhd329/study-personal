package ch07.sec03.exam02;

public class SmartPhoneExample {

	public static void main(String[] args) {
		SmartPhone myPhone = new SmartPhone("갤럭시", "은색");
		
		System.out.printf("모델: %s\n", myPhone.model);
		System.out.printf("색상: %s\n", myPhone.color);

	}

}
