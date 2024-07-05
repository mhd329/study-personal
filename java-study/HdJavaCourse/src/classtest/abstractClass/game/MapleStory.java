package classtest.abstractClass.game;

public class MapleStory extends Game {
	
	@Override
	public void connect() {
		System.out.printf("[%s] 로그인\n\n", this.getUserName());
		System.out.printf("[%s] %s 서버 접속 중...\n", this.getUserName(), this.getGameName());
		System.out.printf("[%s] %s 서버 접속 완료\n", this.getUserName(), this.getGameName());
		System.out.printf("!!! Welcome to MapleStory !!!\n\n");
	}
	
	@Override
	public void play() {
		System.out.printf("[%s] %s 게임 시작\n", this.getUserName(), this.getGameName());
	}
	
	public MapleStory(String name) {
		super(name);
		this.setGameName("메이플스토리");
	}
	
}
