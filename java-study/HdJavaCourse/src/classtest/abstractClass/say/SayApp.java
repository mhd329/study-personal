package classtest.abstractClass.say;

public class SayApp {

	public static void main(String[] args) {
		SayHello sh = new SayHello();
		
		SayGoodbye sb = new SayGoodbye();
		sh.say();
		sb.say();

	}

}
