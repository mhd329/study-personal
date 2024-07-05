package ch08.sec08;

public class MultipleInterfaceImplExample {

	public static void main(String[] args) {
		RemoteControl rc = new SmartTelevision();
		rc.turnOn();
		rc.turnOff();
		Searchable s = new SmartTelevision();
		s.search("https://www.youtube.com/");
	}

}
