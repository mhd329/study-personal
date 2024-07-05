package classtest.footballPlayer;

public class FootballPlayerApp {

	public static void main(String[] args) {
		System.out.println("fp1");
		FootballPlayer fp1 = new FootballPlayer();
		fp1.setName("손흥민");
		fp1.setUniformNumber("7");
		fp1.setTeamName("토트넘");
		fp1.setSpeed(5);
		fp1.setTech(5);
		fp1.printInfo();

		System.out.println("fp2");
		FootballPlayer fp2 = new FootballPlayer("이강인", "PSG", "19", 4, 5);
		fp2.printInfo();
		
	}

}
