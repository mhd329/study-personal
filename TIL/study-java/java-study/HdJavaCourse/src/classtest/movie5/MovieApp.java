package classtest.movie5;

public class MovieApp {

	public static void main(String[] args) {
		Actor[] actorArray = new Actor[3];
        actorArray[0] = Actor.makeActor("톰 크루즈", "남자", "1962.07.03", "미국");
        actorArray[1] = Actor.makeActor("마일즈 텔러", "남자", "1987.02.20", "미국");
        actorArray[2] = Actor.makeActor("모니카 바바로", "여자", "1990.06.18", "미국");
        
        String title = "탑건 매버릭";
        String category = "액션";
        String director = "조셉 코신스키";
        int runningTime = 130;

        Movie m = new Movie(title, category, director, runningTime, actorArray);
        m.printInfo();
	}
}
