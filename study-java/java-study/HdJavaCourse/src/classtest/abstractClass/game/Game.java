package classtest.abstractClass.game;

public abstract class Game {
	private String gameName;
	private String userName;
	
	public String getGameName() {
		return gameName;
	}
	
	public void setGameName(String gameName) {
		this.gameName = gameName;
	}
	
	public String getUserName() {
		return userName;
	}
	public void setUserName(String userName) {
		this.userName = userName;
	}
	
	public Game(String userName) {
		this.userName = userName;
	}
	
	public abstract void connect();
	public abstract void play();
}
