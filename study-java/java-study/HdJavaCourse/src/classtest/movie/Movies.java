package classtest.movie;

public class Movies {

	public static void main(String[] args) {
		MovieModel m1 = new MovieModel();
		m1.title = "탑건:매버릭";
		m1.category = "액션";
		m1.director = "조셉 코신스키";
		m1.runningTime = 132;
		
		m1.printInfo();

	}

}
