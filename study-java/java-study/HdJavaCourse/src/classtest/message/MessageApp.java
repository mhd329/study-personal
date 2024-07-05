package classtest.message;

public class MessageApp {

	public static void main(String[] args) {
		Message msg = new Message();
		
		msg.printInfo("Hello");
		msg.printInfo(50);
		msg.printInfo("World", 60);
		msg.printInfo(60, "World");

	}

}
