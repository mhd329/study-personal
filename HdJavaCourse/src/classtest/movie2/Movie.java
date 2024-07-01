package classtest.movie2;

public class Movie {
	private String title;
	private String category;
	private String director;
	private int runningTime;
	
	String getTitle() {
		return title;
	}
	
	void setTitle(String title) {
		this.title = title;
	}
	
	String getDirector() {
		return director;
	}
	
	void setDirector(String director) {
		this.director = director;
	}
	
	String getCategory() {
		return category;
	}
	
	void setCategory(String category) {
		this.category = category;
	}
	
	int getRunningTime() {
		return runningTime;
	}
	
	void setRunningTime(int runningTime) {
		if (runningTime > 0) {			
			this.runningTime = runningTime;
		} else {
			System.out.println("러닝타임은 0보다 커야합니다.");
		}
	}
	
	void printInfo() {
		System.out.println(title);
		System.out.println(category);
		System.out.println(director);
		System.out.println(runningTime);
	}

}
