package ch08.sec05;

public interface RemoteControl {
	int MAX_VOLUME = 10;
	int MIN_VOLUME = 0;
	
	void turnOn();
	void turnOff();
	void setVolume(int v);
	
	default void setMute(boolean mute) {
		if (mute) {
			System.out.println("무음");
			setVolume(MIN_VOLUME);
			return;
		}
		System.out.println("소리");
	}
}
