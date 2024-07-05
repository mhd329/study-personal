package ch08.sec05;

public class Audio implements RemoteControl {
	private int volume;
	
	@Override
	public void turnOn() {
		System.out.println("ad 켜기");
	}
	@Override
	public void turnOff() {
		System.out.println("ad 끄기");
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
