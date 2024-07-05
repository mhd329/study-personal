package ch08.sec04;

public class Television implements RemoteControl {
	private int volume;
	
	@Override
	public void turnOn() {
		System.out.println("tv 켜기");
	}
	@Override
	public void turnOff() {
		System.out.println("tv 끄기");
	}
	@Override
	public void setVolume(int v) {
		if (v > RemoteControl.MAX_VOLUME) {
			this.volume = RemoteControl.MAX_VOLUME;
		} else if (v < RemoteControl.MIN_VOLUME) {
			this.volume = RemoteControl.MIN_VOLUME;
		} else {
			this.volume = v;
		}
		System.out.printf("볼륨: %d\n", this.volume);
	}
}