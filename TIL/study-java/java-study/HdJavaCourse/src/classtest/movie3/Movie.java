package classtest.movie3;

public class Movie {
	private String title;
	private String category;
	private String director;
	private int runningTime;
	
	public String getTitle() {
		return title;
	}
	
	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getDirector() {
		return director;
	}
	
	public void setDirector(String director) {
		this.director = director;
	}
	
	public String getCategory() {
		return category;
	}
	
	public void setCategory(String category) {
		this.category = category;
	}
	
	public int getRunningTime() {
		return runningTime;
	}
	
	public void setRunningTime(int runningTime) {
		if (runningTime < 0) {			
			System.out.println("러닝타임은 -1보다 큰 정수여야합니다.");
		} else {
			this.runningTime = runningTime;
		}
	}
	
	
	
	public Movie() {
		this("", "", "", 0);
	}
	
	public Movie(String title, String category) {
		this(title, category, "", 0);
	}
	
	public Movie(String title, String category, String director, int runningTime) {
		this.setTitle(title);
		this.setCategory(category);
		this.setDirector(director);
		this.setRunningTime(runningTime);
	}
	
	public void printInfo() {
		System.out.println(this.getTitle());
		System.out.println(this.getCategory());
		System.out.println(this.getDirector());
		System.out.println(this.getRunningTime());
	}

}