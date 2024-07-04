package ch08.sec08;

public class SmartTelevision implements RemoteControl, Searchable {
	@Override
	public void turnOn() {
		System.out.println("tv 켜기");
	}
	@Override
	public void turnOff() {
		System.out.println("tv 끄기");
	}
	@Override
	public void search(String url) {
		System.out.printf("%s 검색\n", url);
	}
}
