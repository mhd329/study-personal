package classtest.abstractClass.game;

public class GameApp {
	public static void main(String[] args) {
		MapleStory ms = new MapleStory("춘식이");
		ms.connect();
		ms.play();
		
	}
}
