package ch09.sec07.exam02;

public class HomeExample {

	public static void main(String[] args) {
		Home h = new Home();
		
		h.use1();
		h.use2();
		h.use3(new RemoteControl() {
			@Override
			public void turnOn() {
				System.out.println("난방 켜기");
			}
			@Override
			public void turnOff() {
				System.out.println("난방 끄기");
			}
		});

	}

}
