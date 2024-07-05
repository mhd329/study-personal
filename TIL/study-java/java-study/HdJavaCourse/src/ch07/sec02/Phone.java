package ch07.sec02;

public class Phone {
	protected String model;
	protected String color;
	
	public void bell() {
		System.out.println("벨 울림.");
	}
	public void sendVoice(String message) {
		System.out.printf("나: %s\n", message);
	}
	public void receiveVoice(String message) {
		System.out.printf("너: %s\n", message);
	}
	public void hangUp() {
		System.out.println("전화 끊기.");
	}
	
}
