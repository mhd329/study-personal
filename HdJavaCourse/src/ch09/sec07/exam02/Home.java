package ch09.sec07.exam02;

public class Home {
	
	private RemoteControl rc = new RemoteControl() {
		@Override
		public void turnOn() {
			System.out.println("TV 켜기");
		}
		@Override
		public void turnOff() {
			System.out.println("TV 끄기");
		}
	};
	
	public void use1() {
		rc.turnOn();
		rc.turnOff();
	}
	
	public void use2() {
		RemoteControl rc = new RemoteControl() {
			@Override
			public void turnOn() {
				System.out.println("에어컨 켜기");
			}
			@Override
			public void turnOff() {
				System.out.println("에어컨 끄기");
			}
		};
		rc.turnOn();
		rc.turnOff();
	}
	
	public void use3(RemoteControl rc) {
		rc.turnOn();
		rc.turnOff();
	}
	
}
